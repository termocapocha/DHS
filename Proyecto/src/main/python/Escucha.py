from antlr4 import TerminalNode
from antlr4 import ErrorNode
from compiladorParser import compiladorParser
from compiladorListener import compiladorListener
from TablaSimbolos import *

class Escucha (compiladorListener) :
    
    indent = 1          #variables
    declaracion = 0     
    profundidad = 0     
    numNodos = 0        
    tabla = None        # Tabla de simbolos    
    
    def enterPrograma(self, ctx:compiladorParser.ProgramaContext):
        # Solo imprime una vez y previene la re-ejecucion
        if not hasattr(self, '_parsing_started'):
            print("Comienza el parsing")
            self._parsing_started = True
        
        if self.tabla is None:
            
            self.tabla = TablaSimbolos()  #aca se inicializa la tabla

    def enterFuncion(self, ctx:compiladorParser.FuncionContext):
        # Imprime linea adicional solicitada por el formato esperado
        print("  Comienza funcion")
        self.indent += 1
        # Crear contexto para parametros/alcance de la funcion
        if self.tabla:
            self.tabla.agregarContexto()

    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):

        print("Fin del parsing")
        # Marcar `main` como utilizada automaticamente si existe (punto de entrada)
        try:
            if self.tabla and self.tabla.devolverID('main'):
                self.tabla.marcarUtilizada('main')
        except Exception:
            pass
        self.reporteVariablesNoUtilizadas()

    def enterBloque(self, ctx:compiladorParser.BloqueContext): #"{"

        print("  "*self.indent + "Abriendo Bloque")
        
        self.tabla.agregarContexto()  # Nuevo contexto
        
        print(f"Contextos activos: {self.tabla.getNumeroContextos()}")
        self.indent += 1

    def exitBloque(self, ctx:compiladorParser.BloqueContext): #"}"

        self.indent -= 1
        print("  "*self.indent + "Fin Bloque")
        
        contextoActual = self.tabla.getContextoActual()  # Snapshot antes de eliminar el contexto
        
        if contextoActual:
            
            print("Variables del contexto:")
            
            for nombre, simbolo in contextoActual.items():
                
                print(f"- {nombre}: {simbolo.getTipo()}")
                
        else:
            
            print("Contexto vacio")
            
        # Eliminar el contexto al salir del bloque
        try:
            self.tabla.quitarContexto()
        except Exception:
            pass

        print(f"Contextos restantes: {self.tabla.getNumeroContextos()}")

    def enterIwhile(self, ctx:compiladorParser.IwhileContext):

        print("  "*self.indent + "Comienza while")
        self.indent += 1

    def exitIwhile(self, ctx:compiladorParser.IwhileContext):

        self.indent -= 1
        print("  "*self.indent + "Fin while")

    def enterDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        print("Declaracion ENTER -> <" + ctx.getText() + ">")
        print("Cant. hijos = " + str(ctx.getChildCount()))
        # linea adicional con formato esperado
        print("Declaracion ENTER -> <>")
    
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):

        print("Declaracion EXIT  -> <" + ctx.getText() + ">")
        

        tipo = ctx.getChild(0).getText() # tipo variable  
        id_nombre = ctx.getChild(1).getText()  # nombre de variable
        if tipo != 'int' and tipo != 'double':
            print(f"ERROR SEMANTICO: Tipo de dato {tipo} no reconocido por el compilador")
            return
        
        # checkea si hay doble declaracion
        if self.tabla.buscarId(id_nombre):
            print(f"ERROR SEMANTICO: La variable {id_nombre} ya existe")
            
        else:
            
            variable = ID(id_nombre, tipo)
            self.tabla.agregarId(variable)
            print(f"Se declaro variable {id_nombre} de tipo {tipo}")
            # impresion adicional con pipes y prefijo
            print(f"  -- Se declaro la variable <{id_nombre}> de tipo <{tipo}>")
            # Incrementar contador de declaraciones
            self.declaracion += 1
        

    
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        self.profundidad += 1

    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        print("ListaVar(%d) Cant. hijos  = %d" % (self.profundidad, ctx.getChildCount()))
        self.profundidad -= 1
        if ctx.getChildCount() == 4 :
            # obtiene el nombre de la variable (hijo en posicion 1)
            varNombre = ctx.getChild(1).getText()
            print("      hoja ID --> %s" % varNombre)
            
            # obtiene el tipo desde el contexto padre (la declaracion)
            # Buscamos el contexto de declaracion que contiene el tipo
            parent_ctx = ctx
            while parent_ctx and not isinstance(parent_ctx, compiladorParser.DeclaracionContext):
                parent_ctx = parent_ctx.parentCtx
            
            if parent_ctx and parent_ctx.tipo():
                tipoVar = parent_ctx.tipo().getText()
                
                # Verificar si la variable ya existe
                if self.tabla.buscarId(varNombre):
                    print(f"ERROR SEMANTICO: Variable {varNombre} ya declarada")
                else:
                    # Crear y agregar la variable a la tabla
                    variable = VariableCompilador(varNombre, tipoVar)
                    self.tabla.agregarId(variable)
                    print(f"Se declaro variable {varNombre} de tipo {tipoVar}")
                    # impresion adicional con formato solicitado
                    print(f"  -- ListaVar({self.profundidad+1}) Cant. hijos  = {ctx.getChildCount()}")
                    print(f"  -- Se declaro la variable <{varNombre}> de tipo <{tipoVar}>")


     
    def __str__(self):

        return "Se hicieron " + str(self.declaracion) + " declaraciones\n" + \
                "Se visitaron " + str(self.numNodos) + " nodos"

    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):

        if ctx.ID():  # checkea si hay una ID
            varNombre = ctx.ID().getText()
            if not self.tabla.buscarId(varNombre):
                print(f"ERROR SEMANTICO: Variable {varNombre} no declarada")
            else:
                # Comprobacion de tipos simple: obtener tipo LHS
                lhs = self.tabla.devolverID(varNombre)
                lhs_tipo = lhs.getTipo() if lhs else None

                # Determinar tipo RHS si es simple ID o NUMERO o llamada
                rhs_tipo = None
                if hasattr(ctx, 'opal') and ctx.opal():
                    opal = ctx.opal()
                    # Caso ID
                    if hasattr(opal, 'ID') and opal.ID():
                        idname = opal.ID().getText()
                        entry = self.tabla.devolverID(idname)
                        if entry:
                            rhs_tipo = entry.getTipo()
                    # Caso numero literal
                    elif hasattr(opal, 'NUMERO') and opal.NUMERO():
                        numtxt = opal.NUMERO().getText()
                        rhs_tipo = 'double' if '.' in numtxt else 'int'
                    # Caso llamada a funcion
                    elif hasattr(opal, 'llamada') and opal.llamada():
                        llamada = opal.llamada()
                        if hasattr(llamada, 'ID') and llamada.ID():
                            funcName = llamada.ID().getText()
                        else:
                            funcName = None
                        if funcName:
                            funcEntry = self.tabla.devolverID(funcName)
                            if funcEntry:
                                rhs_tipo = funcEntry.getTipo()

                # Si se pudo determinar ambos tipos, exigir igualdad estricta
                if lhs_tipo and rhs_tipo and lhs_tipo != rhs_tipo:
                    print(f"ERROR SEMANTICO: Incompatibilidad de tipos al asignar {rhs_tipo} a {lhs_tipo}")
                else:
                    # imprimir formato extra de exit asignacion
                    print(">>> EXIT ASIGNACION EJECUTADO <<<")
                    self.tabla.marcarUtilizada(varNombre)  # Marcar como utilizada
                    print(f"Asignacion valida a variable {varNombre}")
                    print(f"  -- Se asigna un valor a la variable <{varNombre}>")

    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        # impresion solicitada al entrar en asignacion (formato dinamico)
        print("Asignacion ENTER -> <>")
    
    def exitFactor(self, ctx:compiladorParser.FactorContext):

        if ctx.ID():
            varNombre = ctx.ID().getText()
            
            if not self.tabla.buscarId(varNombre):
                print(f"ERROR SEMANTICO: Variable {varNombre} no declarada")
            else:
                self.tabla.marcarUtilizada(varNombre)  # Marcar como utilizada
                print(f"Uso valido de variable {varNombre}")

    def enterIif(self, ctx:compiladorParser.IifContext):
        print("  " * (self.indent - 1) + "Comienza if")
        self.indent += 1

    def exitIif(self, ctx:compiladorParser.IifContext):
        self.indent -= 1
        print("  " * (self.indent - 1) + "Fin if")

    def exitProto(self, ctx:compiladorParser.ProtoContext):

        print("  "*self.indent + "PROTOTIPO DE FUNCION")
        
        if ctx.tipo() and ctx.ID():
            tipoRetorno = ctx.tipo().getText()
            nombreFuncion = ctx.ID().getText()
            
            print(f"Prototipo: {tipoRetorno} {nombreFuncion}(...)")
            
            if self.tabla.buscarId(nombreFuncion):
                print(f"ERROR SEMANTICO: Funcion {nombreFuncion} ya declarada")
            else:
                funcion = FuncionCompilador(nombreFuncion, tipoRetorno, [])
                # Registrar prototipo en contexto global
                try:
                    self.tabla.agregarIdGlobal(funcion)
                except Exception:
                    self.tabla.agregarId(funcion)
                print(f"Se declaro funcion {nombreFuncion}")
                # Imprimir formato adicional solicitado
                print(f"  -- Se declara funcion <{nombreFuncion}> como prototipo")
        else:
            print(f"ERROR: Prototipo mal formado")

    def exitFuncion(self, ctx:compiladorParser.FuncionContext):
        print("  "*self.indent + "DEFINICION DE FUNCION")
        
        if ctx.tipo() and ctx.ID():
            tipoRetorno = ctx.tipo().getText()
            nombreFuncion = ctx.ID().getText()
            
            print(f"Definicion: {tipoRetorno} {nombreFuncion}(...)")
            
            # Verificar si ya existe como prototipo o redefinicion
            funcionExistente = self.tabla.devolverID(nombreFuncion)
            
            if funcionExistente and funcionExistente.getVarFunc() == "funcion":
                
                print(f"Funcion {nombreFuncion} ya declarada como prototipo")
                # Actualizar la firma/tipo de la funcion pero preservar el objeto
                funcionExistente.setTipo(tipoRetorno)
                # Preservar el estado de utilizada si ya fue marcada
                if funcionExistente.getUtilizada():
                    print(f"  (funcion {nombreFuncion} ya estaba marcada como utilizada)")
                
            elif funcionExistente:
                print(f"ERROR SEMANTICO: {nombreFuncion} ya existe pero no es una funcion")
            else:
                
                # Nueva funcion
                funcion = FuncionCompilador(nombreFuncion, tipoRetorno, [])
                # Registrar la definicion en contexto global (no en el contexto de parametros)
                try:
                    self.tabla.agregarIdGlobal(funcion)
                except Exception:
                    self.tabla.agregarId(funcion)
                print(f"Se declaro funcion {nombreFuncion}")
                # Imprimir formato adicional solicitado
                print(f"  -- Se declara funcion <{nombreFuncion}>")
            
            # Marcar como utilizada cuando se define (la definicion es una forma de uso)
            self.tabla.marcarUtilizada(nombreFuncion)
            # Al salir de la funcion, quitar el contexto de parametros (si existe)
            try:
                self.tabla.quitarContexto()
            except Exception:
                pass

    def exitArgumento(self, ctx:compiladorParser.ArgumentoContext):
        # maneja el primer parametro de una funcion en la declaracion
        
        if ctx.tipo() and ctx.ID():
            tipoParam = ctx.tipo().getText()
            nombreParam = ctx.ID().getText()
            
            print(f"Parametro principal: {tipoParam} {nombreParam}")
            
            # Si este argumento pertenece a un prototipo (ProtoContext), no registrar parametros
            parent_ctx = ctx
            in_proto = False
            while parent_ctx is not None:
                if isinstance(parent_ctx, compiladorParser.ProtoContext):
                    in_proto = True
                    break
                if isinstance(parent_ctx, compiladorParser.FuncionContext):
                    break
                parent_ctx = getattr(parent_ctx, 'parentCtx', None)

            if in_proto:
                # No agregar parametros para prototipos
                return

            # verificar si el parametro ya existe en el contexto actual
            if self.tabla.existeEnContextoActual(nombreParam):
                print(f"ERROR SEMANTICO: Parametro {nombreParam} ya declarado en este contexto")
            else:
                # Crea y agrega el parametro a la tabla (contexto actual)
                parametro = VariableCompilador(nombreParam, tipoParam)
                self.tabla.agregarId(parametro)
                print(f"Se declaro parametro {nombreParam} de tipo {tipoParam}")


    def exitListaParametros(self, ctx:compiladorParser.ListaParametrosContext):
        # maneja parametros adicionales en la lista de parametros de una funcion
        
        if ctx.getChildCount() == 4:  # COMA tipo ID listaParametros
            tipoParam = ctx.getChild(1).getText()  # tipo
            nombreParam = ctx.getChild(2).getText()  # ID
            
            print(f"Parametro adicional: {tipoParam} {nombreParam}")
            
            # Si este argumento pertenece a un prototipo (ProtoContext), no registrar parametros
            parent_ctx = ctx
            in_proto = False
            while parent_ctx is not None:
                if isinstance(parent_ctx, compiladorParser.ProtoContext):
                    in_proto = True
                    break
                if isinstance(parent_ctx, compiladorParser.FuncionContext):
                    break
                parent_ctx = getattr(parent_ctx, 'parentCtx', None)

            if in_proto:
                return

            # Verificar si el parametro ya existe en el contexto actual
            if self.tabla.existeEnContextoActual(nombreParam):
                print(f"ERROR SEMANTICO: Parametro {nombreParam} ya declarado en este contexto")
            else:
                # Crear y agrega el parametro a la tabla (contexto actual)
                parametro = VariableCompilador(nombreParam, tipoParam)
                self.tabla.agregarId(parametro)
                print(f"Se declaro parametro {nombreParam} de tipo {tipoParam}")

    def exitLlamada(self, ctx:compiladorParser.LlamadaContext):

        print("  "*self.indent + "LLAMADA A FUNCION")
        
        if ctx.ID():
            
            nombreFuncion = ctx.ID().getText()
            
            funcion = self.tabla.devolverID(nombreFuncion)#si esta declarado
            if not funcion:
                print(f"ERROR SEMANTICO: Funcion {nombreFuncion} no declarada")
            elif funcion.getVarFunc() != "funcion":
                print(f"ERROR SEMANTICO: {nombreFuncion} no es una funcion")
            else:
                self.tabla.marcarUtilizada(nombreFuncion)  # Marcar funcion como utilizada
                print(f"Llamada valida a funcion {nombreFuncion}")
                # Imprimir formato adicional solicitado
                print(f"  -- Llamada valida a <{nombreFuncion}>")
        else:
            print(f"ERROR: Llamada mal formada")

    def reporteVariablesNoUtilizadas(self):

        print("\n=== REPORTE FINAL ===")
        print("Analisis completado exitosamente")
        
        # Marcar main como utilizada automaticamente (es el punto de entrada)
        self.tabla.marcarUtilizada("main")
        
        # Detectar variables/funciones no utilizadas
        noUtilizadas = self.tabla.obtenerNoUtilizadas()
        
        if noUtilizadas:
            print("\n=== VARIABLES/FUNCIONES DECLARADAS PERO NO UTILIZADAS ===")
            for item in noUtilizadas:
                print(f"- {item['nombre']} ({item['tipo']}) - {item['varFunc']} en contexto {item['contexto']}")
        else:
            print("\n=== TODAS LAS VARIABLES/FUNCIONES FUERON UTILIZADAS ===")
        

    def visitErrorNode(self, node: ErrorNode):

        print(" ---> ERROR")
        
    def enterEveryRule(self, ctx):

        self.numNodos += 1
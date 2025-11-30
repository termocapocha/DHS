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
    
    def enterFor(self, ctx:compiladorParser.ForContext):
 
        print("Comienza el parsing")
        
        if self.tabla is None:
            
            self.tabla = TablaSimbolos()  #aca se inicializa la tabla

    def exitFor(self, ctx:compiladorParser.ForContext):

        print("Fin del parsing")
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
            
        self.tabla.quitarContexto()  # eliminador de contexto
        
        print(f"Contextos restantes: {self.tabla.getNumeroContextos()}")

    def enterIwhile(self, ctx:compiladorParser.IwhileContext):

        print("  "*self.indent + "Comienza while")
        self.indent += 1

    def exitIwhile(self, ctx:compiladorParser.IwhileContext):

        self.indent -= 1
        print("  "*self.indent + "Fin while")

    def enterDeclaracion(self, ctx:compiladorParser.DeclaracionContext):

        self.declaracion += 1
        print("Declaracion ENTER -> <" + ctx.getText() + ">")
        print("Cant. hijos = " + str(ctx.getChildCount()))
    
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
        

    
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        self.profundidad += 1

    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        print("ListaVar(%d) Cant. hijos  = %d" % (self.profundidad, ctx.getChildCount()))
        self.profundidad -= 1
        if ctx.getChildCount() == 4 :
            # Obtener el nombre de la variable (hijo en posición 1)
            varNombre = ctx.getChild(1).getText()
            print("      hoja ID --> %s" % varNombre)
            
            # Obtener el tipo desde el contexto padre (declaracion)
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
                    self.declaracion += 1

    # def visitTerminal(self, node: TerminalNode):
    #     print(" ---> Token: " + node.getText())
        # self.numTokens += 1
     
    def __str__(self):

        return "Se hicieron " + str(self.declaracion) + " declaraciones\n" + \
                "Se visitaron " + str(self.numNodos) + " nodos"

    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):

        if ctx.ID():  # checkea si hay una ID
            varNombre = ctx.ID().getText()
            
            if not self.tabla.buscarId(varNombre):
                print(f"ERROR SEMANTICO: Variable {varNombre} no declarada")
            else:
                print(f"Asignacion valida a variable {varNombre}")
    
    def exitFactor(self, ctx:compiladorParser.FactorContext):

        if ctx.ID():
            varNombre = ctx.ID().getText()
            
            if not self.tabla.buscarId(varNombre):
                print(f"ERROR SEMANTICO: Variable {varNombre} no declarada")
            else:
                print(f"Uso valido de variable {varNombre}")

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
                self.tabla.agregarId(funcion)
                print(f"Se declaro funcion {nombreFuncion}")
        else:
            print(f"DEBUG: Prototipo mal formado: {ctx.getText()}")

    def exitFuncion(self, ctx:compiladorParser.FuncionContext):
        print("  "*self.indent + "DEFINICION DE FUNCION")
        
        if ctx.tipo() and ctx.ID():
            tipoRetorno = ctx.tipo().getText()
            nombreFuncion = ctx.ID().getText()
            
            print(f"Definicion: {tipoRetorno} {nombreFuncion}(...)")
            
            # Verificar si ya existe como prototipo o redefinición
            funcionExistente = self.tabla.devolverID(nombreFuncion)
            
            if funcionExistente and funcionExistente.getVarFunc() == "funcion":
                
                print(f"Funcion {nombreFuncion} ya declarada como prototipo")
                
            elif funcionExistente:
                print(f"ERROR SEMANTICO: {nombreFuncion} ya existe pero no es una funcion")
            else:
                
                # Nueva función
                funcion = FuncionCompilador(nombreFuncion, tipoRetorno, [])
                self.tabla.agregarId(funcion)
                print(f"Se declaro funcion {nombreFuncion}")

    def exitArgumento(self, ctx:compiladorParser.ArgumentoContext):
        # Maneja el primer parametro de una funcion en la declaracion
        
        if ctx.tipo() and ctx.ID():
            tipoParam = ctx.tipo().getText()
            nombreParam = ctx.ID().getText()
            
            print(f"Parametro principal: {tipoParam} {nombreParam}")
            
            # Verificar si el parametro ya existe en el contexto actual
            if self.tabla.buscarId(nombreParam):
                
                print(f"ERROR SEMANTICO: Parametro {nombreParam} ya declarado")
                
            else:
                
                # Crea y agrega el parametro a la tabla
                parametro = VariableCompilador(nombreParam, tipoParam)
                self.tabla.agregarId(parametro)
                print(f"Se declaro parametro {nombreParam} de tipo {tipoParam}")
                self.declaracion += 1

    def exitListaParametros(self, ctx:compiladorParser.ListaParametrosContext):
        # Maneja parametros adicionales en la lista de parametros de una funcion
        
        if ctx.getChildCount() == 4:  # COMA tipo ID listaParametros
            tipoParam = ctx.getChild(1).getText()  # tipo
            nombreParam = ctx.getChild(2).getText()  # ID
            
            print(f"Parametro adicional: {tipoParam} {nombreParam}")
            
            # Verificar si el parametro ya existe en el contexto actual
            if self.tabla.buscarId(nombreParam):
                
                print(f"ERROR SEMANTICO: Parametro {nombreParam} ya declarado")
                
            else:
                
                # Crear y agregar el parametro a la tabla
                parametro = VariableCompilador(nombreParam, tipoParam)
                self.tabla.agregarId(parametro)
                print(f"Se declaro parametro {nombreParam} de tipo {tipoParam}")
                self.declaracion += 1

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
                print(f"Llamada valida a funcion {nombreFuncion}")
        else:
            print(f"DEBUG: Llamada sin ID")

    def reporteVariablesNoUtilizadas(self):

        print("\n=== REPORTE FINAL ===")
        print("Analisis completado exitosamente")
        

    def visitErrorNode(self, node: ErrorNode):

        print(" ---> ERROR")
        
    def enterEveryRule(self, ctx):

        self.numNodos += 1
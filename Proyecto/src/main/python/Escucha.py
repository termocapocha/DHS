from antlr4 import TerminalNode
from antlr4 import ErrorNode
from compiladorParser import compiladorParser
from compiladorListener import compiladorListener
from TablaSimbolos import *

class Escucha (compiladorListener):
    
    indent = 1
    declaracion = 0
    profundidad = 0
    numNodos = 0
    tabla = None
    parametrosFuncion = []
    parametrosAgregados = False
    
    def enterPrograma(self, ctx):
        if not hasattr(self, 'parsing_started'):
            print("Comienza el parsing")
            self.parsing_started = True
        if self.tabla is None:
            self.tabla = TablaSimbolos()

    def enterFuncion(self, ctx):
        print("  Comienza funcion")
        self.indent += 1
        self.parametrosFuncion = []
        self.parametrosAgregados = False

    def exitPrograma(self, ctx):
        print("Fin del parsing")
        try:
            if self.tabla and self.tabla.devolverID('main'):
                self.tabla.marcarUtilizada('main')
        except Exception:
            pass
        self.reporteVariablesNoUtilizadas()

    def determinarTipoContexto(self, ctx):
        tipoContexto = "bloque"
        padre = ctx.parentCtx
        if padre:
            if isinstance(padre, compiladorParser.FuncionContext):
                tipoContexto = "funcion"
            elif isinstance(padre, compiladorParser.IifContext):
                tipoContexto = "if"
            elif isinstance(padre, compiladorParser.IelseContext):
                tipoContexto = "else"
            elif isinstance(padre, compiladorParser.IwhileContext):
                tipoContexto = "while"
            else:
                ancestro = padre.parentCtx
                while ancestro:
                    if isinstance(ancestro, compiladorParser.IelseContext):
                        tipoContexto = "else"
                        break
                    elif isinstance(ancestro, compiladorParser.IifContext):
                        tipoContexto = "if"
                        break
                    elif isinstance(ancestro, compiladorParser.IwhileContext):
                        tipoContexto = "while"
                        break
                    ancestro = ancestro.parentCtx
        return tipoContexto

    def enterBloque(self, ctx):
        print("  "*self.indent + "Abriendo Bloque")
        tipoContexto = self.determinarTipoContexto(ctx)
        self.tabla.agregarContexto(tipoContexto)
        
        if self.parametrosFuncion and not self.parametrosAgregados:
            for parametro in self.parametrosFuncion:
                nombreParam = parametro.getNombre()
                if not self.tabla.existeEnContextoActual(nombreParam):
                    parametro.setEsParametro(True)
                    self.tabla.agregarId(parametro)
                    print(f"Se declaro parametro {nombreParam} de tipo {parametro.getTipo()}")
            self.parametrosAgregados = True
        
        print(f"Contextos activos: {self.tabla.getNumeroContextos()}")
        self.indent += 1

    def exitBloque(self, ctx):
        self.indent -= 1
        print("  "*self.indent + "Fin Bloque")
        
        contextoActual = self.tabla.getContextoActual()
        if contextoActual:
            print("Variables del contexto:")
            for nombre, simbolo in contextoActual.items():
                tipoItem = "parametro" if simbolo.esParametro else "variable"
                print(f"- {nombre}: {simbolo.getTipo()} ({tipoItem})")
        else:
            print("Contexto vacio")
            
        try:
            self.tabla.quitarContexto()
        except Exception:
            pass
        print(f"Contextos restantes: {self.tabla.getNumeroContextos()}")

    def enterIwhile(self, ctx):
        print("  "*self.indent + "Comienza while")
        self.indent += 1

    def exitIwhile(self, ctx):
        self.indent -= 1
        print("  "*self.indent + "Fin while")

    def enterDeclaracion(self, ctx):
        print("Declaracion ENTER -> <" + ctx.getText() + ">")
        print("Cant. hijos = " + str(ctx.getChildCount()))
        print("Declaracion ENTER -> <>")
    
    def exitDeclaracion(self, ctx):
        print("Declaracion EXIT  -> <" + ctx.getText() + ">")
        
        if ctx.getChildCount() < 2:
            return
            
        tipo = ctx.getChild(0).getText()
        idNombre = ctx.getChild(1).getText()
        if tipo != 'int' and tipo != 'double':
            print(f"ERROR SEMANTICO: Tipo de dato {tipo} no reconocido por el compilador")
            return
        
        if self.tabla.buscarId(idNombre):
            print(f"ERROR SEMANTICO: La variable {idNombre} ya existe")
        else:
            variable = ID(idNombre, tipo)
            self.tabla.agregarId(variable)
            print(f"Se declaro variable {idNombre} de tipo {tipo}")
            print(f"  -- Se declaro la variable <{idNombre}> de tipo <{tipo}>")
            self.declaracion += 1

    def enterListavar(self, ctx):
        self.profundidad += 1

    def exitListavar(self, ctx):
        print("ListaVar(%d) Cant. hijos  = %d" % (self.profundidad, ctx.getChildCount()))
        self.profundidad -= 1
        if ctx.getChildCount() == 4:
            varNombre = ctx.getChild(1).getText()
            print("      hoja ID --> %s" % varNombre)
            
            parentCtx = ctx
            while parentCtx and not isinstance(parentCtx, compiladorParser.DeclaracionContext):
                parentCtx = parentCtx.parentCtx
            
            if parentCtx and parentCtx.tipo():
                tipoVar = parentCtx.tipo().getText()
                
                if self.tabla.buscarId(varNombre):
                    print(f"ERROR SEMANTICO: Variable {varNombre} ya declarada")
                else:
                    variable = ID(varNombre, tipoVar)
                    self.tabla.agregarId(variable)
                    print(f"Se declaro variable {varNombre} de tipo {tipoVar}")
                    print(f"  -- ListaVar({self.profundidad+1}) Cant. hijos  = {ctx.getChildCount()}")
                    print(f"  -- Se declaro la variable <{varNombre}> de tipo <{tipoVar}>")

    def __str__(self):
        return f"Se hicieron {self.declaracion} declaraciones\nSe visitaron {self.numNodos} nodos"

    def verificarVariable(self, varNombre):
        if not self.tabla.buscarId(varNombre):
            print(f"ERROR SEMANTICO: Variable {varNombre} no declarada")
            return False
        self.tabla.marcarUtilizada(varNombre)
        return True

    def exitAsignacion(self, ctx):
        if ctx.ID():
            varNombre = ctx.ID().getText()
            if self.verificarVariable(varNombre):
                lhs = self.tabla.devolverID(varNombre)
                lhsTipo = lhs.getTipo() if lhs else None

                rhsTipo = None
                if hasattr(ctx, 'opal') and ctx.opal():
                    opal = ctx.opal()
                    if hasattr(opal, 'ID') and opal.ID():
                        idname = opal.ID().getText()
                        entry = self.tabla.devolverID(idname)
                        if entry:
                            rhsTipo = entry.getTipo()
                    elif hasattr(opal, 'NUMERO') and opal.NUMERO():
                        numtxt = opal.NUMERO().getText()
                        rhsTipo = 'double' if '.' in numtxt else 'int'
                    elif hasattr(opal, 'llamada') and opal.llamada():
                        llamada = opal.llamada()
                        if hasattr(llamada, 'ID') and llamada.ID():
                            funcName = llamada.ID().getText()
                            funcEntry = self.tabla.devolverID(funcName)
                            if funcEntry:
                                rhsTipo = funcEntry.getTipo()

                if lhsTipo and rhsTipo and lhsTipo != rhsTipo:
                    print(f"ERROR SEMANTICO: Incompatibilidad de tipos al asignar {rhsTipo} a {lhsTipo}")
                else:
                    print(">>> EXIT ASIGNACION EJECUTADO <<<")
                    print(f"Asignacion valida a variable {varNombre}")
                    print(f"  -- Se asigna un valor a la variable <{varNombre}>")

    def enterAsignacion(self, ctx):
        print("Asignacion ENTER -> <>")
    
    def exitFactor(self, ctx):
        if ctx.ID():
            varNombre = ctx.ID().getText()
            if self.verificarVariable(varNombre):
                print(f"Uso valido de variable {varNombre}")

    def enterIif(self, ctx):
        print("  " * (self.indent - 1) + "Comienza if")
        self.indent += 1

    def exitIif(self, ctx):
        self.indent -= 1
        print("  " * (self.indent - 1) + "Fin if")

    def agregarParametro(self, tipoParam, nombreParam, esPrincipal=True):
        prefijo = "principal" if esPrincipal else "adicional"
        print(f"Parametro {prefijo}: {tipoParam} {nombreParam}")
        parametro = ID(nombreParam, tipoParam)
        self.parametrosFuncion.append(parametro)
        print(f"  -- Parametro acumulado: {nombreParam}")

    def exitProto(self, ctx):
        print("  "*self.indent + "PROTOTIPO DE FUNCION")
        
        if ctx.tipo() and ctx.ID():
            tipoRetorno = ctx.tipo().getText()
            nombreFuncion = ctx.ID().getText()
            
            print(f"Prototipo: {tipoRetorno} {nombreFuncion}(...)")
            
            if self.tabla.buscarId(nombreFuncion):
                print(f"ERROR SEMANTICO: Funcion {nombreFuncion} ya declarada")
            else:
                parametros = self.parametrosFuncion.copy()
                funcion = FuncionCompilador(nombreFuncion, tipoRetorno, parametros)
                try:
                    self.tabla.agregarIdGlobal(funcion)
                except Exception:
                    self.tabla.agregarId(funcion)
                print(f"Se declaro funcion {nombreFuncion}")
                print(f"  -- Se declara funcion <{nombreFuncion}> como prototipo")
        else:
            print(f"ERROR: Prototipo mal formado")
        
        self.parametrosFuncion = []

    def exitFuncion(self, ctx):
        print("  "*self.indent + "DEFINICION DE FUNCION")
        
        if ctx.tipo() and ctx.ID():
            tipoRetorno = ctx.tipo().getText()
            nombreFuncion = ctx.ID().getText()
            
            print(f"Definicion: {tipoRetorno} {nombreFuncion}(...)")
            parametros = self.parametrosFuncion.copy()
            funcionExistente = self.tabla.devolverID(nombreFuncion)
            
            if funcionExistente and funcionExistente.getVarFunc() == "funcion":
                print(f"Funcion {nombreFuncion} ya declarada como prototipo")
                funcionExistente.setTipo(tipoRetorno)
                funcionExistente.setParametros(parametros)
                if funcionExistente.getUtilizada():
                    print(f"  (funcion {nombreFuncion} ya estaba marcada como utilizada)")
            elif funcionExistente:
                print(f"ERROR SEMANTICO: {nombreFuncion} ya existe pero no es una funcion")
            else:
                funcion = FuncionCompilador(nombreFuncion, tipoRetorno, parametros)
                try:
                    self.tabla.agregarIdGlobal(funcion)
                except Exception:
                    self.tabla.agregarId(funcion)
                print(f"Se declaro funcion {nombreFuncion}")
                print(f"  -- Se declara funcion <{nombreFuncion}>")
            
            self.tabla.marcarUtilizada(nombreFuncion)
            self.parametrosFuncion = []
            self.parametrosAgregados = False

    def exitArgumento(self, ctx):
        if ctx.tipo() and ctx.ID():
            self.agregarParametro(ctx.tipo().getText(), ctx.ID().getText(), True)

    def exitListaParametros(self, ctx):
        if ctx.getChildCount() == 4:
            self.agregarParametro(ctx.getChild(1).getText(), ctx.getChild(2).getText(), False)

    def exitLlamada(self, ctx):
        print("  "*self.indent + "LLAMADA A FUNCION")
        
        if ctx.ID():
            nombreFuncion = ctx.ID().getText()
            funcion = self.tabla.devolverID(nombreFuncion)
            if not funcion:
                print(f"ERROR SEMANTICO: Funcion {nombreFuncion} no declarada")
            elif funcion.getVarFunc() != "funcion":
                print(f"ERROR SEMANTICO: {nombreFuncion} no es una funcion")
            else:
                self.tabla.marcarUtilizada(nombreFuncion)
                print(f"Llamada valida a funcion {nombreFuncion}")
                print(f"  -- Llamada valida a <{nombreFuncion}>")
        else:
            print(f"ERROR: Llamada mal formada")

    def reporteVariablesNoUtilizadas(self):
        print("\n=== REPORTE FINAL ===")
        print("Analisis completado exitosamente")
        
        self.tabla.marcarUtilizada("main")
        noUtilizadas = self.tabla.obtenerNoUtilizadas()
        
        if noUtilizadas:
            print("\n=== VARIABLES/FUNCIONES DECLARADAS PERO NO UTILIZADAS ===")
            for item in noUtilizadas:
                print(f"- {item['nombre']} ({item['tipo']}) - {item['varFunc']} en contexto {item['contexto']}")
        else:
            print("\n=== TODAS LAS VARIABLES/FUNCIONES FUERON UTILIZADAS ===")

    def visitErrorNode(self, node):
        print(" ---> ERROR")
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1

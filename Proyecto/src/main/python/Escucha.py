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
    tabla = None        # Tabla de símbolos    
    
    def enterFor(self, ctx:compiladorParser.ForContext):
 
        print("Comienza el parsing")
        
        if self.tabla is None:
            
            self.tabla = TablaSimbolos()  #aca se inicializa la tabla

    def exitFor(self, ctx:compiladorParser.ForContext):

        print("Fin del parsing")
        self.reporteVariablesNoUtilizadas()

    def enterBloque(self, ctx:compiladorParser.BloqueContext): #"{"

        print("  "*self.indent + "Abriendo Bloque")
        
        self.tabla.agregar_contexto()  # Nuevo contexto
        
        print(f"Contextos activos: {len(self.tabla.contexto)}")
        self.indent += 1

    def exitBloque(self, ctx:compiladorParser.BloqueContext): #"}"

        self.indent -= 1
        print("  "*self.indent + "Fin Bloque")
        
        contexto_actual = self.tabla.contexto[-1]  # Snapshot antes de eliminar el contexto
        
        if contexto_actual:
            
            print("Variables del contexto:")
            
            for nombre, simbolo in contexto_actual.items():
                
                print(f"- {nombre}: {simbolo.tipo}")
                
        else:
            
            print("Contexto vacio")
            
        self.tabla.quitar_contexto()  # eliminador de contexto
        
        print(f"Contextos restantes: {len(self.tabla.contexto)}")

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
        if self.tabla.buscar_ID(id_nombre):
            print(f"ERROR SEMANTICO: La variable {id_nombre} ya existe")
            
        else:
            
            variable = ID(id_nombre, tipo)
            self.tabla.agregar_ID(variable)
            print(f"Se declaro variable {id_nombre} de tipo {tipo}")
        

    
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        self.profundidad += 1

    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        print("ListaVar(%d) Cant. hijos  = %d" % (self.profundidad, ctx.getChildCount()))
        self.profundidad -= 1
        if ctx.getChildCount() == 4 :
            print("      hoja ID --> %s" % ctx.getChild(1).getText())

    # def visitTerminal(self, node: TerminalNode):
    #     print(" ---> Token: " + node.getText())
        # self.numTokens += 1
     
    def __str__(self):

        return "Se hicieron " + str(self.declaracion) + " declaraciones\n" + \
                "Se visitaron " + str(self.numNodos) + " nodos"

    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):

        if ctx.ID():  # checkea si hay una ID
            varNombre = ctx.ID().getText()
            
            if not self.tabla.buscar_ID(varNombre):
                print(f"ERROR SEMANTICO: Variable {varNombre} no declarada")
            else:
                print(f"Asignacion valida a variable {varNombre}")
    
    def exitFactor(self, ctx:compiladorParser.FactorContext):

        if ctx.ID():
            varNombre = ctx.ID().getText()
            
            if not self.tabla.buscar_ID(varNombre):
                print(f"ERROR SEMANTICO: Variable {varNombre} no declarada")
            else:
                print(f"Uso valido de variable {varNombre}")

    def exitProto(self, ctx:compiladorParser.ProtoContext):

        print("  "*self.indent + "PROTOTIPO DE FUNCION")
        
        if ctx.tipo() and ctx.ID():
            tipoRetorno = ctx.tipo().getText()
            nombreFuncion = ctx.ID().getText()
            
            print(f"Prototipo: {tipoRetorno} {nombreFuncion}(...)")
            
            if self.tabla.buscar_ID(nombreFuncion):
                print(f"ERROR SEMANTICO: Funcion {nombreFuncion} ya declarada")
            else:
                funcion = FuncionCompilador(nombreFuncion, tipoRetorno, [])
                self.tabla.agregar_ID(funcion)
                print(f"Se declaro funcion {nombreFuncion}")
        else:
            print(f"DEBUG: Prototipo mal formado: {ctx.getText()}")

    def exitLlamada(self, ctx:compiladorParser.LlamadaContext):

        print("  "*self.indent + "LLAMADA A FUNCION")
        
        if ctx.ID():
            
            nombreFuncion = ctx.ID().getText()
            
            funcion = self.tabla.devolver_ID(nombreFuncion)#si esta declarado
            if not funcion:
                print(f"ERROR SEMANTICO: Funcion {nombreFuncion} no declarada")
            elif funcion.varFunc != "funcion":
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
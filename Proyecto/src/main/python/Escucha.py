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
    tabla = None        
    
    def enterFor(self, ctx:compiladorParser.ForContext):
        print("Comienza el parsing")
        
        if self.tabla is None:
            
            self.tabla = TablaSimbolos()  #aca se inicializa la tabla

    def exitFor(self, ctx:compiladorParser.ForContext):
        print("Fin del parsing")

    def enterBloque(self, ctx:compiladorParser.BloqueContext): #"{"
        print("  "*self.indent + "Abriendo Bloque")
        self.tabla.agregar_contexto()  # Nuevo ámbito
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
            
            print("Contexto vacío")
            
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
        print("Declaracion ENTER -> |" + ctx.getText() + "|")
        print("  -- Cant. hijos = " + str(ctx.getChildCount()))
    
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        print("Declaracion EXIT  -> |" + ctx.getText() + "|")
        print("  -- Cant. hijos = " + str(ctx.getChildCount()))
    
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        self.profundidad += 1

    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        print("  -- ListaVar(%d) Cant. hijos  = %d" % (self.profundidad, ctx.getChildCount()))
        self.profundidad -= 1
        if ctx.getChildCount() == 4 :
            print("      hoja ID --> |%s|" % ctx.getChild(1).getText())

    # def visitTerminal(self, node: TerminalNode):
    #     print(" ---> Token: " + node.getText())
        # self.numTokens += 1
    
    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR")
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1
    
    def __str__(self):
        return "Se hicieron " + str(self.declaracion) + " declaraciones\n" + \
                "Se visitaron " + str(self.numNodos) + " nodos"
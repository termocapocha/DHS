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
        print("Cant. hijos = " + str(ctx.getChildCount()))
    
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        print("Declaracion EXIT  -> |" + ctx.getText() + "|")
        

        tipo = ctx.getChild(0).getText() # tipo variable  
        id_nombre = ctx.getChild(1).getText()  # nombre de variable
        
        if tipo != 'int' and tipo != 'double':
            print(f"ERROR SEMANTICO: Tipo de dato {tipo} no reconocido por el compilador")
            return
        
        # checkea si hay doble declaracion
        if self.tabla.buscar_ID(id_nombre):
            print(f"ERROR SEMANTICO: La variable {id_nombre} ya existe")
        else:
            
            variable = ID(id_nombre, tipo) # crear y agregar la variable
            
            if ctx.getChildCount() > 3:  # tiene más elementos además de tipo e ID
                variable.initialized = True
            
            self.tabla.agregar_ID(variable)
            estado_init = "inicializada" if variable.initialized else "no inicializada"
            print(f"  -- Se declaró variable |{id_nombre}| de tipo |{tipo}| ({estado_init})")
        
        # Procesar lista de variables adicionales si existe
        if ctx.getChildCount() > 3 and hasattr(ctx, 'listavar') and ctx.listavar():
            self.check_listvar(ctx.listavar(), tipo)
    
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
     
    def check_listvar(self, ctx_listavar, tipo):

        if ctx_listavar is None or ctx_listavar.getChildCount() == 0:
            return
            
        if ctx_listavar.getChildCount() >= 2:
            

            if hasattr(ctx_listavar, 'ID') and ctx_listavar.ID(): #hasattr (objeto,atriburo) =true =!false
                var_nombre = ctx_listavar.ID().getText()
                
                if self.tabla.buscar_ID(var_nombre): # si existe doble declaracion
                    
                    print(f"ERROR SEMANTICO: La variable {var_nombre} ya existe")
                else:
        
                    variable = ID(var_nombre, tipo) #crea variable
                    
                    if ctx_listavar.getChildCount() > 2:  # verifica si tiene asignacion
                        variable.initialized = True
                    
                    self.tabla.agregar_ID(variable)
                    
                    estado_init = "inicializada" if variable.initialized else "no inicializada"
                    
                    print(f"Se declaró {var_nombre} tipo |{tipo}| ({estado_init})")
            
            #recursividad (condicion=no hay mas variables en la lista)
            if hasattr(ctx_listavar, 'listavar') and ctx_listavar.listavar(): #hasattr (objeto,atriburo) =true =!false
                self.check_listvar(ctx_listavar.listavar(), tipo) 

    def __str__(self):
        return "Se hicieron " + str(self.declaracion) + " declaraciones\n" + \
                "Se visitaron " + str(self.numNodos) + " nodos"

    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR")
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1
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
        self.reporteVariableNoUtilizadas()

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
            
            if ctx.getChildCount() > 3:  # tiene mas elementos ademas de tipo e ID
                variable.initialized = True
            
            self.tabla.agregar_ID(variable)
            estado_init = "inicializada" if variable.initialized else "no inicializada"
            print(f"Se declaro variable |{id_nombre}| de tipo |{tipo}| ({estado_init})")
        
        # Procesar lista de variables adicionales si existe
        if ctx.getChildCount() > 3 and hasattr(ctx, 'listavar') and ctx.listavar():
            self.check_listvar(ctx.listavar(), tipo)
    
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        self.profundidad += 1

    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        print("ListaVar(%d) Cant. hijos  = %d" % (self.profundidad, ctx.getChildCount()))
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
                    
                    print(f"Se declaro {var_nombre} tipo |{tipo}| ({estado_init})")
            
            #recursividad (condicion=no hay mas variables en la lista)
            if hasattr(ctx_listavar, 'listavar') and ctx_listavar.listavar(): #hasattr (objeto,atriburo) =true =!false
                self.check_listvar(ctx_listavar.listavar(), tipo) 

    def __str__(self):
        return "Se hicieron " + str(self.declaracion) + " declaraciones\n" + \
                "Se visitaron " + str(self.numNodos) + " nodos"

    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):

        if ctx.ID():  # checkea si hay una ID
            var_nombre = ctx.ID().getText()
            
            if not self.tabla.buscar_ID(var_nombre):
                print(f"ERROR SEMANTICO: Variable {var_nombre} no declarada (asignacion)")
            else:
                variable = self.tabla.devolver_ID(var_nombre) #obtiene la variable
                
                if variable and variable.varFunc == "variable":
                    tipo_valor = self.inferir_tipo_expresion(ctx) #obtiene el tipo de valor
                    
                    # Validador
                    if tipo_valor and not self.validar_compatibilidad_tipos(tipo_valor, variable.tipo):
                        print(f"ERROR SEMANTICO: Incompatibilidad de tipos | no se puede asignar {tipo_valor} a {variable.tipo} en {var_nombre}")
                    else:
                        # Marcar como inicializada solo si la asignacion es valida
                        variable.initialized = True #marca la variable
                        if tipo_valor:
                            print(f"Asignacion valida: {tipo_valor} -> {variable.tipo} en {var_nombre}")
                        else:
                            print(f"Asignacion valida a variable {var_nombre}")
                else:
                    print(f"Asignacion valida a variable {var_nombre}")
    
    def exitFactor(self, ctx:compiladorParser.FactorContext):
        
        if ctx.ID():
            var_nombre = ctx.ID().getText()
            
            if not self.tabla.buscar_ID(var_nombre):
                
                print(f"ERROR SEMANTICO: Variable {var_nombre} no declarada (expresion)")
                
            else:
                
                variable = self.tabla.devolver_ID(var_nombre)
                
                if variable and variable.varFunc == "variable":

                    if not variable.initialized: #checkea si esta inicializada
                        print(f"ERROR SEMANTICO: Variable {var_nombre} usada sin inicializar")
                        
                    else:
                        print(f"uso valido de variable {var_nombre}")
                    
                    variable.used = True #marca la variable
                elif variable and variable.varFunc == "funcion":
                    print(f"uso valido de funcion {var_nombre}")
                    variable.used = True

    def enterPrototipo(self, ctx:compiladorParser.ProtoContext):
        
        print("  "*self.indent + "PROTOTIPO DE FUNCION")
        
        if ctx.getChildCount() >= 2: 

            tipo_retorno = ctx.getChild(0).getText()
            nombre_funcion = ctx.getChild(1).getText()
            
            print(f"Prototipo: {tipo_retorno} {nombre_funcion}(...)")
            
            if self.tabla.buscar_ID(nombre_funcion):  #verifica declaracion
                print(f"ERROR SEMANTICO: Funcion {nombre_funcion} ya declarada")
            else:
    
                funcion = FuncionCompilador(nombre_funcion, tipo_retorno, [])
                self.tabla.agregar_ID(funcion)
                print(f"Se declaro funcion {nombre_funcion} tipo retorno {tipo_retorno}")
        else:
            print(f"DEBUG: Prototipo con {ctx.getChildCount()} hijos: {ctx.getText()}")

    def enterLlamada(self, ctx:compiladorParser.LlamadaContext):

        print("  "*self.indent + "LLAMADA A FUNCION")
        
        if ctx.ID():
            
            nombre_funcion = ctx.ID().getText()
            
            funcion = self.tabla.devolver_ID(nombre_funcion) #si esta declarado
            if not funcion:
                print(f"ERROR SEMANTICO: Funcion {nombre_funcion} no declarada")
            elif funcion.varFunc != "funcion":
                print(f"ERROR SEMANTICO: {nombre_funcion} no es una funcion")
            else:
                print(f"Llamada valida a funcion {nombre_funcion}")
                # Marcar funcion como usada
                funcion.used = True
        else:
            print(f"DEBUG: Llamada sin ID - {ctx.getChildCount()} hijos: {ctx.getText()}")

    def reporteVariableNoUtilizadas(self):
        
        print("REPORTE FINAL DE ANALISIS SEMANTICO")
        
        variables_no_utilizadas = []
        variables_no_inicializadas = []
        funciones_no_utilizadas = []
        
        for i, contexto in enumerate(self.tabla.contexto): #recorre la tabla de simbolos
            
            for nombre, simbolo in contexto.items():
                
                if simbolo.varFunc == "variable":
                    # Verificar variables no utilizadas
                    if not simbolo.used:
                        variables_no_utilizadas.append((nombre, simbolo.tipo, i))
                    
                    # Verificar variables no inicializadas (declaradas pero nunca inicializadas)
                    if not simbolo.initialized:
                        variables_no_inicializadas.append((nombre, simbolo.tipo, i))
                        
                elif simbolo.varFunc == "funcion":
                    if not simbolo.used:
                        funciones_no_utilizadas.append((nombre, simbolo.tipo, i))
        
        
        # Reporte de variables no inicializadas
        if variables_no_inicializadas:
            
            print(f"\nWARNING: {len(variables_no_inicializadas)} variable(s) no inicializada(s):")
            
            for nombre, tipo, contexto_id in variables_no_inicializadas:
                
                print(f"  Variable '{nombre}' tipo '{tipo}' (contexto {contexto_id})")
                
        else:
            
            print("\nTodas las variables fueron inicializadas correctamente")
        
        # Reporte de variables
        if variables_no_utilizadas:
            
            print(f"\nWARNING: {len(variables_no_utilizadas)} variable(s) no utilizada(s):")
            
            for nombre, tipo, contexto_id in variables_no_utilizadas:
                
                print(f"  Variable '{nombre}' tipo '{tipo}' (contexto {contexto_id})")
                
        else:
            
            print("\nTodas las variables declaradas fueron utilizadas")
        
         
        if funciones_no_utilizadas:
            
            print(f"\nWARNING: {len(funciones_no_utilizadas)} funcion(es) no utilizada(s):")
            
            for nombre, tipo, contexto_id in funciones_no_utilizadas:
                
                print(f"Funcion '{nombre}' tipo '{tipo}' (contexto {contexto_id})")
                
        else:
            
            print("\nTodas las funciones declaradas fueron utilizadas")
        

    def validar_compatibilidad_tipos(self, tipo_origen, tipo_destino): 
        
        if tipo_origen == tipo_destino: #compatibilidad
            return True
            
        if tipo_origen == "int" and tipo_destino == "double": #int a double (aceptable)
            return True
            
        if tipo_origen == "double" and tipo_destino == "int": #double a int (no aceptable)
            return False
            
        return False #false por default

    def inferir_tipo_expresion(self, ctx):
        
        texto = ctx.getText()
        
        if any(char.isdigit() for char in texto):
            # Si contiene punto decimal, es double
            if '.' in texto:  #el "." es exclusivo del double 
                return "double"
            
            elif any(char.isdigit() for char in texto): #basicamente si no lo tiene es un int
                return "int"
        
        for i in range(ctx.getChildCount()):
            
            child = ctx.getChild(i)
            
            if hasattr(child, 'getText'):
                
                child_text = child.getText()
                
                if child_text and child_text.isalpha():
                    
                    variable = self.tabla.devolver_ID(child_text)
                    
                    if variable and variable.varFunc == "variable":
                        
                        return variable.tipo
        
        return None #default

    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR")
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1
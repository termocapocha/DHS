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
            
            variable = ID(id_nombre, tipo) # crear y agregar la variable
            
            if ctx.getChildCount() > 3:  # tiene mas elementos ademas de tipo e ID
                variable.initialized = True
            
            self.tabla.agregar_ID(variable)
            estado_init = "inicializada" if variable.initialized else "no inicializada"
            print(f"Se declaro variable {id_nombre} de tipo {tipo} ({estado_init})")
        
        # Procesar lista de variables adicionales si existe
        if ctx.getChildCount() > 3 and hasattr(ctx, 'listavar') and ctx.listavar():
            self.check_listvar(ctx.listavar(), tipo)
    
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
                    
                    print(f"Se declaro {var_nombre} tipo {tipo} ({estado_init})")
            
            #recursividad (condicion=no hay mas variables en la lista)
            if hasattr(ctx_listavar, 'listavar') and ctx_listavar.listavar(): #hasattr (objeto,atriburo) =true =!false
                self.check_listvar(ctx_listavar.listavar(), tipo) 

    def __str__(self):
        return "Se hicieron " + str(self.declaracion) + " declaraciones\n" + \
                "Se visitaron " + str(self.numNodos) + " nodos"

    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):

        if ctx.ID():  # checkea si hay una ID
            varNombre = ctx.ID().getText()
            
            if not self.tabla.buscar_ID(varNombre):
                print(f"ERROR SEMANTICO: Variable {varNombre} no declarada (asignacion)")
            else:
                variable = self.tabla.devolver_ID(varNombre) #obtiene la variable
                
                if variable and variable.varFunc == "variable":
                    tipoValor = self.inferirTipoExpresion(ctx) #obtiene el tipo de valor
                    
                    # Validador
                    if tipoValor and not self.validador(tipoValor, variable.tipo):
                        print(f"ERROR SEMANTICO: Incompatibilidad de tipos | no se puede asignar {tipoValor} a {variable.tipo} en {varNombre}")
                    else:
                        # Marcar como inicializada solo si la asignacion es valida
                        variable.initialized = True #marca la variable
                        if tipoValor:
                            print(f"Asignacion valida: {tipoValor} -> {variable.tipo} en {varNombre}")
                        else:
                            print(f"Asignacion valida a variable {varNombre}")
                else:
                    print(f"Asignacion valida a variable {varNombre}")
    
    def exitFactor(self, ctx:compiladorParser.FactorContext):
        
        if ctx.ID():
            varNombre = ctx.ID().getText()
            
            if not self.tabla.buscar_ID(varNombre):
                
                print(f"ERROR SEMANTICO: Variable {varNombre} no declarada (expresion)")
                
            else:
                
                variable = self.tabla.devolver_ID(varNombre)
                
                if variable and variable.varFunc == "variable":

                    if not variable.initialized: #checkea si esta inicializada
                        print(f"ERROR SEMANTICO: Variable {varNombre} usada sin inicializar")
                        
                    else:
                        print(f"uso valido de variable {varNombre}")
                    
                    variable.used = True #marca la variable
                elif variable and variable.varFunc == "funcion":
                    print(f"uso valido de funcion {varNombre}")
                    variable.used = True

    def exitProto(self, ctx:compiladorParser.ProtoContext):
        
        print("  "*self.indent + "PROTOTIPO DE FUNCION")
        
        if ctx.tipo() and ctx.ID():
            tipo_retorno = ctx.tipo().getText()
            nombre_funcion = ctx.ID().getText()
            
            # Extraer parámetros del prototipo
            parametros = []
            if ctx.argumento():
                parametros = self.extraerParametrosPrototipo(ctx.argumento())
            
            print(f"Prototipo: {tipo_retorno} {nombre_funcion}({', '.join([f'{p[0]} {p[1]}' for p in parametros])})")
            
            if self.tabla.buscar_ID(nombre_funcion):
                print(f"ERROR SEMANTICO: Funcion {nombre_funcion} ya declarada")
            else:
                funcion = FuncionCompilador(nombre_funcion, tipo_retorno, parametros)
                self.tabla.agregar_ID(funcion)
                print(f"Se declaro funcion {nombre_funcion} tipo retorno {tipo_retorno} con {len(parametros)} parametros")
        else:
            print(f"DEBUG: Prototipo mal formado: {ctx.getText()}")

    def exitLlamada(self, ctx:compiladorParser.LlamadaContext):

        print("  "*self.indent + "LLAMADA A FUNCION")
        
        if ctx.ID():
            
            nombreFuncion = ctx.ID().getText()
            
            funcion = self.tabla.devolver_ID(nombreFuncion) #si esta declarado
            if not funcion:
                print(f"ERROR SEMANTICO: Funcion {nombreFuncion} no declarada")
            elif funcion.varFunc != "funcion":
                print(f"ERROR SEMANTICO: {nombreFuncion} no es una funcion")
            else:
                
                argumentosLlamada = []
                if ctx.largumento(): #extrae los argumentos
                    argumentosLlamada = self.extraerArgumentosLlamada(ctx.largumento())
                
 
                if self.validarParametrosFuncion(funcion, argumentosLlamada, nombreFuncion):
                    print(f"Llamada valida a funcion {nombreFuncion}")
                    # Marcar funcion como usada
                    funcion.used = True
        else:
            print(f"DEBUG: Llamada sin ID - {ctx.getChildCount()} hijos: {ctx.getText()}")

    def reporteVariablesNoUtilizadas(self):
        
        print("REPORTE FINAL DE ANALISIS SEMANTICO")
        
        variablesNoUtilizadas = []
        variablesNoInicializadas = []
        funcionesNoUtilizadas = []
        
        for i, contexto in enumerate(self.tabla.contexto): #recorre la tabla de simbolos
            
            for nombre, simbolo in contexto.items():
                
                if simbolo.varFunc == "variable":
                    # Verificar variables (no utilizadas)
                    if not simbolo.used:
                        variablesNoUtilizadas.append((nombre, simbolo.tipo, i))
                    
                    # Verificar variables (declaradas no inicializadas)
                    if not simbolo.initialized:
                        variablesNoInicializadas.append((nombre, simbolo.tipo, i))
                        
                elif simbolo.varFunc == "funcion":
                    if not simbolo.used:
                        funcionesNoUtilizadas.append((nombre, simbolo.tipo, i))
        
        
        # Reporte de variables no inicializadas
        if variablesNoInicializadas:
            
            print(f"\nWARNING: {len(variablesNoInicializadas)} variable(s) no inicializada(s):")
            
            for nombre, tipo, contextoId in variablesNoInicializadas:
                
                print(f"  Variable '{nombre}' tipo '{tipo}' (contexto {contextoId})")
                
        else:
            
            print("\nTodas las variables fueron inicializadas correctamente")
        
        # Reporte de variables
        if variablesNoUtilizadas:
            
            print(f"\nWARNING: {len(variablesNoUtilizadas)} variable(s) no utilizada(s):")
            
            for nombre, tipo, contextoId in variablesNoUtilizadas:
                
                print(f"  Variable '{nombre}' tipo '{tipo}' (contexto {contextoId})")
                
        else:
            
            print("\nTodas las variables declaradas fueron utilizadas")
        
         
        if funcionesNoUtilizadas:
            
            print(f"\nWARNING: {len(funcionesNoUtilizadas)} funcion(es) no utilizada(s):")
            
            for nombre, tipo, contextoId in funcionesNoUtilizadas:
                
                print(f"Funcion '{nombre}' tipo '{tipo}' (contexto {contextoId})")
                
        else:
            
            print("\nTodas las funciones declaradas fueron utilizadas")
        

    def validador(self, tipo_origen, tipo_destino): 
        
        if tipo_origen == tipo_destino: #compatibilidad
            return True
            
        if tipo_origen == "int" and tipo_destino == "double": #int a double (aceptable)
            return True
            
        if tipo_origen == "double" and tipo_destino == "int": #double a int (no aceptable)
            return False
            
        return False #false por default

    def inferirTipoExpresion(self, ctx):
        
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

    def extraerParametrosPrototipo(self, ctxArgumento):
        
        parametros = []
        
        # Primer parametro
        if ctxArgumento.tipo() and ctxArgumento.ID():
            tipo = ctxArgumento.tipo().getText()
            nombre = ctxArgumento.ID().getText()
            parametros.append((tipo, nombre))
        
        # subsecuentes
        if ctxArgumento.masArgumento():
            parametros.extend(self.extraerMasArgumentos(ctxArgumento.masArgumento()))
        
        return parametros
    
    def extraerMasArgumentos(self, ctxMasArgumento):
        
        parametros = []
        
        if ctxMasArgumento.tipo() and ctxMasArgumento.ID():
            tipo = ctxMasArgumento.tipo().getText()
            nombre = ctxMasArgumento.ID().getText()
            parametros.append((tipo, nombre))
        
        if ctxMasArgumento.masArgumento():
            parametros.extend(self.extraerMasArgumentos(ctxMasArgumento.masArgumento()))
        
        return parametros
    
    def extraerArgumentosLlamada(self, ctxLargumento):
        
        argumentos = []
        
        # Primer argumento
        if ctxLargumento.opal():
            tipoArg = self.inferirTipoExpresion(ctxLargumento.opal())
            argumentos.append(tipoArg)
        
        # subsecuentes
        if ctxLargumento.masLargumento():
            argumentos.extend(self.extraerMasLargumentos(ctxLargumento.masLargumento()))
        
        return argumentos
    
    def extraerMasLargumentos(self, ctxMasLargumento):
        
        argumentos = []
        
        if ctxMasLargumento.opal():
            tipoArg = self.inferirTipoExpresion(ctxMasLargumento.opal())
            argumentos.append(tipoArg)
        
        if ctxMasLargumento.masLargumento():
            argumentos.extend(self.extraerMasLargumentos(ctxMasLargumento.masLargumento()))
        
        return argumentos
    
    def validarParametrosFuncion(self, funcion, argumentosLlamada, nombreFuncion):
        
        parametrosEsperados = funcion.parametros
        
        # Verificar cantidad
        if len(parametrosEsperados) != len(argumentosLlamada):
            print(f"ERROR SEMANTICO: Funcion {nombreFuncion} espera {len(parametrosEsperados)} parametros, pero se pasaron {len(argumentosLlamada)}")
            return False
        
        # Verificar tipos
        for i, (tipoEsperado, _) in enumerate(parametrosEsperados):
            tipoArgumento = argumentosLlamada[i]
            
            if tipoArgumento is None:
                print(f"ERROR SEMANTICO: No se pudo determinar el tipo del argumento {i+1} en llamada a {nombreFuncion}")
                return False
            
            if not self.validador(tipoArgumento, tipoEsperado):
                print(f"ERROR SEMANTICO: Parametro {i+1} de {nombreFuncion}: se esperaba {tipoEsperado}, se paso {tipoArgumento}")
                return False
        
        return True

    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR")
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1
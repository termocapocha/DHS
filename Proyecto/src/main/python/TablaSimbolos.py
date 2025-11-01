class TablaSimbolos:

    tabla_unica = None

    def __new__(cls):

        if cls.tabla_unica is None:
           cls.tabla_unica = super(TablaSimbolos, cls).__new__(cls)
        return cls.tabla_unica

    # Cada diccionario almacena los identificadores de ese contexto
    contexto = [dict()]

    def agregar_contexto(self):  #cuando se entra a un bloque

        self.contexto.append(dict())

    def quitar_contexto(self):#cuando se sale de un bloque

        self.contexto.pop()

    def agregar_ID(self, ID): #agrega un ID al contexto actual
        
        self.contexto[-1][ID.nombre] = ID

    def buscar_ID(self, key_id): #busca un ID especifico los contexto
      
        for contexto in self.contexto:
            
            if key_id in contexto:
                
                return True         #si todo sale bien deveria delvoler true
            
        return False

    def devolver_ID(self, key_id): #
  
        for contexto in self.contexto:
            
            if key_id in contexto:
                
                return contexto[key_id]  
                  
        return False


class ID:
    
    def __init__(self, nombre, tipo):
        
        self.nombre = nombre        # Nombre del identificador
        self.tipo = tipo           # Tipo de dato
        self.initialized = False
        self.used = False
        self.varFunc = "variable" # Indica si es "variable" o "funcion"

    def toString(self): #ID a string 

        return f'(name->{self.nombre},tipo->{self.tipo},init->{self.initialized},used->{self.used},varFun->{self.varFunc})'


class VariableCompilador(ID): #repesenta una variable

    pass

class FuncionCompilador(ID): #representa una funcion

    def __init__(self, nombre, tipo, parameters): #constructor (de la funcion)

        super().__init__(nombre, tipo) 
        self.parameters = parameters    
        self.varFunc = "function"      
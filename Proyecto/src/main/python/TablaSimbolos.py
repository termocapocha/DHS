class TablaSimbolos:

    _tablaUnica = None

    def __new__(cls):

        if cls._tablaUnica is None:
           cls._tablaUnica = super(TablaSimbolos, cls).__new__(cls)
           cls._tablaUnica._inicializar()
        return cls._tablaUnica

    def _inicializar(self):
        # Cada diccionario almacena los identificadores de ese contexto
        self._contexto = [dict()]

    def agregarContexto(self):  #cuando se entra a un bloque

        self._contexto.append(dict())

    def quitarContexto(self):#cuando se sale de un bloque

        self._contexto.pop()

    def agregarId(self, ID): #agrega un ID al contexto actual
        
        self._contexto[-1][ID.getNombre()] = ID

    def buscarId(self, keyId): #busca un ID especifico los contexto
      
        # Busca de afuera hacia adentro (más global a más local)
        for contexto in self._contexto:
            
            if keyId in contexto:
                
                return True         #si todo sale bien deveria delvoler true
            
        return False

    def devolverID(self, keyId): #
  
        # Busca de afuera hacia adentro (más global a más local)
        for contexto in self._contexto:
            
            if keyId in contexto:
                
                return contexto[keyId]  
                  
        return False

    def getNumeroContextos(self):
        return len(self._contexto)
        
    def getContextoActual(self):
        """Retorna una copia del contexto actual para inspección"""
        return dict(self._contexto[-1])
        
    def iterarContextos(self):
        """Generador que permite iterar sobre los contextos de manera segura"""
        for contexto in self._contexto:
            yield dict(contexto)  # Retorna copias para evitar modificaciones externas


class ID:
    
    def __init__(self, nombre, tipo):
        
        self._nombre = nombre        # Nombre del identificador (privado)
        self._tipo = tipo           # Tipo de dato (privado)
        self._varFunc = "variable" # Indica si es "variable" o "funcion" (privado)

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getTipo(self):
        return self._tipo
        
    def setTipo(self, tipo):
        self._tipo = tipo
        
    def getVarFunc(self):
        return self._varFunc
        
    def setVarFunc(self, varFunc):
        self._varFunc = varFunc

    def toString(self): #ID a string 

        return f'(name->{self._nombre},tipo->{self._tipo},varFun->{self._varFunc})'


class VariableCompilador(ID): #repesenta una variable

    pass

class FuncionCompilador(ID): #representa una funcion

    def __init__(self, nombre, tipo, parametros): #constructor (de la funcion)

        super().__init__(nombre, tipo) 
        self.setVarFunc("funcion")      
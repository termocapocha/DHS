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
        
    def reiniciar(self):
        # Metodo para reiniciar la tabla de símbolos
        self._inicializar()

    def agregarContexto(self):  #cuando se entra a un bloque

        self._contexto.append(dict())

    def quitarContexto(self):#cuando se sale de un bloque

        self._contexto.pop()

    def agregarId(self, ID): #agrega un ID al contexto actual
        
        self._contexto[-1][ID.getNombre()] = ID

    def buscarId(self, keyId): #busca un ID especifico los contexto
      
        # Busca de afuera hacia adentro (mas global a mas local)
        for contexto in self._contexto:
            
            if keyId in contexto:
                
                return True         #si todo sale bien deberia delvoler true
            
        return False

    def devolverID(self, keyId): #
  
        # Busca de afuera hacia adentro (mas global a mas local)
        for contexto in self._contexto:
            
            if keyId in contexto:
                
                return contexto[keyId]  
                  
        return False

    def getNumeroContextos(self):
        return len(self._contexto)
        
    def getContextoActual(self):
        #Retorna una copia del contexto actual para inspeccion
        return dict(self._contexto[-1])
        
    def iterarContextos(self):
        #Generador que permite iterar sobre los contextos de manera segura
        for contexto in self._contexto:
            yield dict(contexto)  # Retorna copias para evitar modificaciones externas
            
    def marcarUtilizada(self, keyId):
        #Marca una variable/funcion como utilizada
        for contexto in self._contexto:
            
            if keyId in contexto:
                contexto[keyId].marcarUtilizada()
                return True
            
        return False
        
    def obtenerNoUtilizadas(self):
        #Retorna una lista de variables/funciones declaradas pero no utilizadas
        noUtilizadas = []
        for i, contexto in enumerate(self._contexto):
            
            for nombre, simbolo in contexto.items():
                
                if not simbolo.getUtilizada():
                    
                    noUtilizadas.append({
                        'nombre': nombre,
                        'tipo': simbolo.getTipo(),
                        'varFunc': simbolo.getVarFunc(),
                        'contexto': i
                    })
                    
        return noUtilizadas
        
    def exportarTabla(self, archivo):
        #Exporta la tabla de simbolos completa a un archivo
        archivo.write("CONTEXTOS DE LA TABLA DE SIMBOLOS:\n\n")
        
        for i, contexto in enumerate(self._contexto):
            archivo.write(f"CONTEXTO {i}:\n")
            if contexto:
                for nombre, item in contexto.items():
                    # Detectar si el ID representa una funcion o una variable
                    try:
                        if item.getVarFunc() == "funcion":
                            archivo.write(f"  - {nombre}: funcion {item.getTipo()}\n")
                        else:
                            archivo.write(f"  - {nombre}: variable {item.getTipo()}\n")
                    except Exception:
                        # Fallback por seguridad
                        archivo.write(f"  - {nombre}: {item.getTipo()}\n")
            else:
                archivo.write("  (vacío)\n")
            archivo.write("\n")


class ID:
    
    def __init__(self, nombre, tipo):
        
        self._nombre = nombre        # Nombre del identificador (privado)
        self._tipo = tipo           # Tipo de dato (privado)
        self._varFunc = "variable" # Indica si es "variable" o "funcion" (privado)
        self._utilizada = False    # Indica si ha sido utilizada (privado)

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
        
    def getUtilizada(self):
        return self._utilizada
        
    def setUtilizada(self, utilizada):
        self._utilizada = utilizada
        
    def marcarUtilizada(self):
        self._utilizada = True

    def toString(self): #ID a string 

        return f'(name->{self._nombre},tipo->{self._tipo},varFun->{self._varFunc},utilizada->{self._utilizada})'


class VariableCompilador(ID): #repesenta una variable

    pass

class FuncionCompilador(ID): #representa una funcion

    def __init__(self, nombre, tipo, parametros): #constructor (de la funcion)

        super().__init__(nombre, tipo) 
        self.setVarFunc("funcion")      
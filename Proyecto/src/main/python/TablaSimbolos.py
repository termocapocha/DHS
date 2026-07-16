class TablaSimbolos:
    tablaUnica = None

    def __new__(cls):
        if cls.tablaUnica is None:
            cls.tablaUnica = super(TablaSimbolos, cls).__new__(cls)
            cls.tablaUnica.inicializar()
        return cls.tablaUnica

    def inicializar(self):
        self.contexto = [dict()]
        self.historial = []
        self.contextoId = 1
        self.tiposContexto = {0: "global"}
        self.indiceAId = {0: 0}
        
    def reiniciar(self):
        self.inicializar()

    def agregarContexto(self, tipo="bloque"):
        nuevoId = self.contextoId
        self.contextoId += 1
        self.contexto.append(dict())
        self.tiposContexto[nuevoId] = tipo
        self.indiceAId[len(self.contexto) - 1] = nuevoId
        return nuevoId

    def quitarContexto(self):
        if len(self.contexto) > 0:
            indiceCerrar = len(self.contexto) - 1
            contextoId = self.indiceAId.get(indiceCerrar, indiceCerrar)
            tipo = self.tiposContexto.get(contextoId, "desconocido")
            contexto = self.contexto.pop()
            try:
                self.historial.append((contextoId, dict(contexto), tipo))
            except Exception:
                pass
            if indiceCerrar in self.indiceAId:
                del self.indiceAId[indiceCerrar]

    def agregarId(self, ID):
        self.contexto[-1][ID.getNombre()] = ID

    def buscarId(self, keyId):
        return self.devolverID(keyId)

    def devolverID(self, keyId):
        for i in range(len(self.contexto) - 1, -1, -1):
            if keyId in self.contexto[i]:
                return self.contexto[i][keyId]
        return None

    def getNumeroContextos(self):
        return len(self.contexto)
        
    def getContextoActual(self):
        return dict(self.contexto[-1])
    
    def getTipoContextoActual(self):
        indice = len(self.contexto) - 1
        contextoId = self.indiceAId.get(indice, indice)
        return self.tiposContexto.get(contextoId, "desconocido")

    def existeEnContextoActual(self, keyId):
        if not self.contexto:
            return False
        return keyId in self.contexto[-1]
            
    def marcarUtilizada(self, keyId):
        for i in range(len(self.contexto) - 1, -1, -1):
            if keyId in self.contexto[i]:
                self.contexto[i][keyId].marcarUtilizada()
                return True
        return False
        
    def obtenerNoUtilizadas(self):
        noUtilizadas = []
        for i, contexto in enumerate(self.contexto):
            contextoId = self.indiceAId.get(i, i)
            for nombre, simbolo in contexto.items():
                if not simbolo.getUtilizada():
                    noUtilizadas.append({
                        'nombre': nombre,
                        'tipo': simbolo.getTipo(),
                        'varFunc': simbolo.getVarFunc(),
                        'contexto': contextoId
                    })
        return noUtilizadas
        
    def exportarTabla(self, archivo):
        archivo.write("Tabla de Simbolos generada\n\n")
        todos = {}
        tipos = {}
        
        for i, c in enumerate(self.contexto):
            contextoId = self.indiceAId.get(i, i)
            todos[contextoId] = c
            tipos[contextoId] = self.tiposContexto.get(contextoId, "desconocido")
                
        for idx, c, tipo in self.historial:
            todos[idx] = c
            tipos[idx] = tipo

        for i in sorted(todos.keys()):
            contexto = todos[i]
            tipo = tipos.get(i, "desconocido")
            
            etiquetas = {0: "global", "funcion": "funcion", "if": "if", "else": "else", "while": "while"}
            if i == 0:
                archivo.write("CONTEXTO 0 (global):\n")
            elif tipo in etiquetas:
                archivo.write(f"CONTEXTO {i} ({etiquetas[tipo]}):\n")
            else:
                archivo.write(f"CONTEXTO {i} ({tipo}):\n")
            
            if contexto:
                for nombre, item in contexto.items():
                    try:
                        if item.getVarFunc() == "funcion":
                            params = ""
                            if hasattr(item, 'getParametros') and item.getParametros():
                                paramsList = list(reversed(item.getParametros()))
                                paramsStr = ", ".join([f"{p.getTipo()} {p.getNombre()}" for p in paramsList])
                                params = f"\n     parametros: {paramsStr}"
                            archivo.write(f"  - {nombre}: funcion {item.getTipo()}{params}\n")
                        else:
                            esParametro = getattr(item, '_esParametro', False)
                            tipoItem = "parametro" if esParametro else "variable"
                            archivo.write(f"  - {nombre}: {tipoItem} {item.getTipo()}\n")
                    except Exception:
                        archivo.write(f"  - {nombre}: {item.getTipo()}\n")
            else:
                archivo.write("  (vacio)\n")
            archivo.write("\n")

    def agregarIdGlobal(self, ID):
        if len(self.contexto) == 0:
            self.inicializar()
        self.contexto[0][ID.getNombre()] = ID


class ID:
    def __init__(self, nombre, tipo, varFunc="variable"):
        self.nombre = nombre
        self.tipo = tipo
        self.varFunc = varFunc
        self.utilizada = False
        self.esParametro = False

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def getTipo(self):
        return self.tipo
        
    def setTipo(self, tipo):
        self.tipo = tipo
        
    def getVarFunc(self):
        return self.varFunc
        
    def setVarFunc(self, varFunc):
        self.varFunc = varFunc
        
    def getUtilizada(self):
        return self.utilizada
        
    def setUtilizada(self, utilizada):
        self.utilizada = utilizada
        
    def marcarUtilizada(self):
        self.utilizada = True
        
    def esParametro(self):
        return self.esParametro
        
    def setEsParametro(self, esParametro):
        self.esParametro = esParametro

    def toString(self):
        return f'(name->{self.nombre},tipo->{self.tipo},varFun->{self.varFunc},utilizada->{self.utilizada})'


class FuncionCompilador(ID):
    def __init__(self, nombre, tipo, parametros):
        super().__init__(nombre, tipo, "funcion")
        self.parametros = parametros if parametros else []
        
    def getParametros(self):
        return self.parametros
    
    def setParametros(self, parametros):
        self.parametros = parametros if parametros else []


VariableCompilador = ID

import os

# === GENERADOR DE CODIGO DE TRES DIRECCIONES ===
class CodigoTresDirecciones:
    def __init__(self):
        self.output = []
        self.tempCount = 0
        self.labelCount = 0

    def nuevaTemporal(self):
        t = f"t{self.tempCount}"
        self.tempCount += 1
        return t

    def nuevoTemp(self):
        return self.nuevaTemporal()

    def nuevoLabel(self):
        l = f"L{self.labelCount}"
        self.labelCount += 1
        return l

    def nuevoLabelAlias(self):
        return self.nuevoLabel()

    def agregarInstruccion(self, line):
        if line is None:
            return
        if not isinstance(line, str):
            try:
                line = str(line)
            except Exception:
                return
        line = line.strip()
        if not line:
            return
        self.output.append(line)

    def asignacion(self, nombre, valor):
        if nombre is None:
            return
        if valor is None:
            valor = '0'
        self.agregarInstruccion(f"{nombre} = {valor}")

    def asignar(self, nombre, valor):
        return self.asignacion(nombre, valor)

    def operacion(self, destino, a, operador, b):
        if destino is None:
            return
        a = '0' if a is None else a
        b = '0' if b is None else b
        self.agregarInstruccion(f"{destino} = {a} {operador} {b}")

    def operar(self, destino, a, operador, b):
        return self.operacion(destino, a, operador, b)

    def llamadaFuncion(self, nombre, args=None):
        if nombre is None:
            return None
        if args is None:
            args = []
        for a in args:
            if a is None:
                a = '0'
            self.agregarInstruccion(f"param {a}")
        ret = self.nuevaTemporal()
        self.agregarInstruccion(f"{ret} = call {nombre}, {len(args)}")
        return ret

    def retorno(self, valor=None):
        if valor is not None:
            self.agregarInstruccion(f"return {valor}")
        else:
            self.agregarInstruccion("return")

    def retornar(self, valor=None):
        return self.retorno(valor)

    def escribirCodigo(self, filename=None):
        if filename is None:
            filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "output", "CodigoIntermedio.txt")
        folder = os.path.dirname(filename)
        if folder and not os.path.exists(folder):
            try:
                os.makedirs(folder, exist_ok=True)
            except Exception:
                pass
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for line in self.output:
                    f.write(line + "\n")
        except Exception:
            for line in self.output:
                print(line)

    def limpiar(self):
        self.output = []
        self.tempCount = 0
        self.labelCount = 0

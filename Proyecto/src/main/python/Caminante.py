from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser

class Caminante(compiladorVisitor):
    def __init__(self):
        self.contadorTemporales = 0
        self.output = []

    def nuevaTemporal(self): # t0,t1,t2,...
        temp = f"t{self.contadorTemporales}"
        self.contadorTemporales += 1
        return temp

    def emit(self, line):
        self.output.append(line)

    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        if ctx.instrucciones():
            return self.visitInstrucciones(ctx.instrucciones())
        # Al finalizar, volcar la salida acumulada
        for l in self.output:
            print(l)
        return None

    # Sobreescribe TODOS los metodos del visitor base para evitar visitChildren
    # estilo lista enlazada
    def visitInstrucciones(self, ctx):
        # Procesar recursivamente todas las instrucciones
        if hasattr(ctx, 'instruccion') and ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        if hasattr(ctx, 'instrucciones') and ctx.instrucciones():
            self.visitInstrucciones(ctx.instrucciones())
        return None

    def visitInstruccion(self, ctx):
        # Usar visitChildren pero controlado
        return self.visitChildren(ctx)

    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):  # ej: r=0, r=1, etc
        if ctx.ID() and ctx.opal():
            variable = ctx.ID().getText()
            temporal = self.visitOpal(ctx.opal())
            if temporal is not None:
                self.emit(f"{variable} = {temporal}")
        return None

    def visitOpal(self, ctx:compiladorParser.OpalContext):
        return self.visitExp(ctx.exp())

    def visitExp(self, ctx:compiladorParser.ExpContext): # suma/resta
        izq = self.visitTerm(ctx.term())
        if ctx.e() and ctx.e().getChildCount() > 0:
            return self.visitE(ctx.e(), izq)
        return izq

    def visitE(self, ctx, izq): # lo de arriba pero recursivo
        if ctx.getChildCount() == 0:
            return izq
        if ctx.getChildCount() >= 2:
            operador = ctx.getChild(0).getText()
            der = self.visit(ctx.getChild(1))
            # Constant folding si ambos operandos son literales numericos
            if isinstance(izq, str) and isinstance(der, str):
                def isLiteralNum(s):
                    if not s:
                        return False
                    if isinstance(s, str) and s[0].isalpha():
                        return False
                    try:
                        float(s)
                        return True
                    except Exception:
                        return False
                if isLiteralNum(izq) and isLiteralNum(der):
                    try:
                        a = float(izq)
                        b = float(der)
                        if operador == '+':
                            res = a + b
                        elif operador == '-':
                            res = a - b
                        elif operador == '*':
                            res = a * b
                        elif operador == '/':
                            res = a / b
                        else:
                            res = None
                        if res is not None:
                            # Formatear: si es entero exacto devolver sin .0
                            if float(res).is_integer():
                                return str(int(res))
                            else:
                                return str(res)
                    except Exception:
                        pass
            temporal = self.nuevaTemporal()
            self.emit(f"{temporal} = {izq} {operador} {der}")
            if ctx.getChildCount() > 2:
                return self.visitE(ctx.getChild(2), temporal)
            return temporal
        return izq

    def visitTerm(self, ctx:compiladorParser.TermContext): # * y /
        izq = self.visitFactor(ctx.factor())
        if ctx.t() and ctx.t().getChildCount() > 0:
            return self.visitT(ctx.t(), izq)
        return izq

    def visitT(self, ctx, izq): # lo de arriba pero recursivo
        if ctx.getChildCount() == 0:
            return izq
        if ctx.getChildCount() >= 2:
            operador = ctx.getChild(0).getText()
            der = self.visit(ctx.getChild(1))
            # Constant folding similar a visitE
            if isinstance(izq, str) and isinstance(der, str):
                def isLiteralNum(s):
                    if not s:
                        return False
                    if isinstance(s, str) and s[0].isalpha():
                        return False
                    try:
                        float(s)
                        return True
                    except Exception:
                        return False
                if isLiteralNum(izq) and isLiteralNum(der):
                    try:
                        a = float(izq)
                        b = float(der)
                        if operador == '+':
                            res = a + b
                        elif operador == '-':
                            res = a - b
                        elif operador == '*':
                            res = a * b
                        elif operador == '/':
                            res = a / b
                        else:
                            res = None
                        if res is not None:
                            if float(res).is_integer():
                                return str(int(res))
                            else:
                                return str(res)
                    except Exception:
                        pass
            temporal = self.nuevaTemporal()
            self.emit(f"{temporal} = {izq} {operador} {der}")
            if ctx.getChildCount() > 2:
                return self.visitT(ctx.getChild(2), temporal)
            return temporal
        return izq

    def visitFactor(self, ctx:compiladorParser.FactorContext): # numeros, ids, llamada, parentis
        if ctx.ID():
            return ctx.ID().getText()
        elif ctx.NUMERO():
            return ctx.NUMERO().getText()
        elif ctx.exp():
            return self.visitExp(ctx.exp())
        elif ctx.llamada():
            return self.visitLlamada(ctx.llamada())
        return None

    def visitIwhile(self, ctx:compiladorParser.IwhileContext):
        print("Entro a while")
        # Visitar la condicion si existe
        if hasattr(ctx, 'condicion') and ctx.condicion():
            self.visitCondicion(ctx.condicion())
        # Visitar la instruccion (cuerpo del while)
        if hasattr(ctx, 'instruccion') and ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        return None

    def visitCondicion(self, ctx):
        # Visitar la expresion de condicion
        if hasattr(ctx, 'orExp') and ctx.orExp():
            return self.visitOrExp(ctx.orExp())
        return None

    def visitOrExp(self, ctx):
        # andExp orExpRest
        if hasattr(ctx, 'andExp') and ctx.andExp():
            return self.visitAndExp(ctx.andExp())
        return None

    def visitOrExpRest(self, ctx):
        # OR andExp orExpRest | epsilon
        return None

    def visitAndExp(self, ctx):
        # comparacion andExpRest
        if hasattr(ctx, 'comparacion') and ctx.comparacion():
            return self.visitComparacion(ctx.comparacion())
        return None

    def visitAndExpRest(self, ctx):
        # AND comparacion andExpRest | epsilon
        return None

    def visitComparacion(self, ctx):
        # termino comparacionRest
        if hasattr(ctx, 'termino') and ctx.termino():
            return self.visitTermino(ctx.termino())
        return None

    def visitComparacionRest(self, ctx):
        # COMP termino | epsilon
        return None

    def visitTermino(self, ctx):
        # opal | LIT | PA condicion PC
        if hasattr(ctx, 'opal') and ctx.opal():
            return self.visitOpal(ctx.opal())
        elif hasattr(ctx, 'LIT') and ctx.LIT():
            return ctx.LIT().getText()
        elif hasattr(ctx, 'condicion') and ctx.condicion():
            return self.visitCondicion(ctx.condicion())
        return None

    def visitFuncion(self, ctx):
        # Generar marco de activacion para la funcion
        nombre = None
        if hasattr(ctx, 'ID') and ctx.ID():
            nombre = ctx.ID().getText()
        if nombre:
            self.emit(f"func {nombre} :")
            self.emit(f"push_frame {nombre}")
        # Procesar las instrucciones del bloque de la funcion
        if hasattr(ctx, 'bloque') and ctx.bloque():
            self.visitBloque(ctx.bloque())
        if nombre:
            self.emit(f"pop_frame {nombre}")
        return None

    def visitProto(self, ctx):
        # No generar codigo para prototipos
        return None

    def visitIif(self, ctx):
        # IF PA condicion PC instruccion ielse
        # Visitar la instruccion del if
        if hasattr(ctx, 'instruccion') and ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        # Visitar el else si existe
        if hasattr(ctx, 'ielse') and ctx.ielse():
            self.visitIelse(ctx.ielse())
        return None

    def visitIelse(self, ctx):
        # ELSE instruccion | epsilon
        if hasattr(ctx, 'instruccion') and ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        return None

    def visitLlamada(self, ctx):
        # ID PA argumentosLlamada PC
        # Generar codigo para la llamada
        if hasattr(ctx, 'ID'):
            funcName = ctx.ID().getText()
            args = []
            if hasattr(ctx, 'argumentosLlamada') and ctx.argumentosLlamada():
                args = self.visitArgumentosLlamada(ctx.argumentosLlamada()) or []
            # Push arguments
            for a in args:
                self.emit(f"push {a}")
            self.emit(f"call {funcName}")
            # Obtener retorno
            retTemp = self.nuevaTemporal()
            self.emit(f"{retTemp} = pop")
            # Limpieza de argumentos (si necesario)
            if args:
                self.emit(f"pop_args {len(args)}")
            return retTemp
        return None

    def visitArgumentosLlamada(self, ctx):
        # opal listaArgumentos | epsilon
        args = []
        if hasattr(ctx, 'opal') and ctx.opal():
            first = self.visitOpal(ctx.opal())
            if first is not None:
                args.append(first)
        if hasattr(ctx, 'listaArgumentos') and ctx.listaArgumentos():
            rest = self.visitListaArgumentos(ctx.listaArgumentos())
            if rest:
                args.extend(rest)
        return args

    def visitListaArgumentos(self, ctx):
        args = []
        if hasattr(ctx, 'opal') and ctx.opal():
            val = self.visitOpal(ctx.opal())
            if val is not None:
                args.append(val)
        if hasattr(ctx, 'listaArgumentos') and ctx.listaArgumentos():
            rest = self.visitListaArgumentos(ctx.listaArgumentos())
            if rest:
                args.extend(rest)
        return args

    def visitBloque(self, ctx):
        if ctx.children:
            for child in ctx.children:
                if hasattr(child, 'getRuleIndex'):
                    ruleIndex = child.getRuleIndex()
                    if ruleIndex == compiladorParser.RULE_instrucciones:
                        self.visitInstrucciones(child)
        return None

    def visitIreturn(self, ctx:compiladorParser.IreturnContext):
        if ctx.opal():
            temporal = self.visitOpal(ctx.opal())
            print(f"return {temporal}")
        return None

    def visitDeclaracion(self, ctx):
        # tipo ID inic listavar
        # Procesar la inicializacion si existe
        # Reservar espacio para la variable declarada
        if hasattr(ctx, 'ID') and ctx.ID():
            varName = ctx.ID().getText()
            print(f"alloc {varName}")
        if hasattr(ctx, 'inic') and ctx.inic():
            self.visitInic(ctx.inic())
        # Procesar la lista de variables si existe
        if hasattr(ctx, 'listavar') and ctx.listavar():
            self.visitListavar(ctx.listavar())
        return None

    def visitInic(self, ctx):
        # ASIG opal | epsilon
        # Obtener la variable del contexto padre (declaracion)
        if hasattr(ctx, 'opal') and ctx.opal():
            valor = self.visitOpal(ctx.opal())
            # Buscar el ID de la declaración padre
            parent = ctx.parentCtx
            if parent and hasattr(parent, 'ID'):
                varName = parent.ID().getText()
                if valor is not None:
                    print(f"{varName} = {valor}")
        return None

    def visitListavar(self, ctx):
        # COMA ID inic listavar | epsilon
        # Si hay mas variables en la lista
        if hasattr(ctx, 'ID') and ctx.ID():
            # Procesar inicialización si existe
            if hasattr(ctx, 'inic') and ctx.inic():
                valor = self.visitInic(ctx.inic())
                varName = ctx.ID().getText()
                if valor is not None:
                    print(f"{varName} = {valor}")
        # Procesar siguiente variable en la lista
        if hasattr(ctx, 'listavar') and ctx.listavar():
            self.visitListavar(ctx.listavar())
        return None

    def visitProto(self, ctx):
        return None

    def visitArgumento(self, ctx):
        return None

    def visitListaParametros(self, ctx):
        return None
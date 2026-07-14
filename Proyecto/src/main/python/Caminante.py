import re
from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser
from CodigoTresDirecciones import CodigoTresDirecciones

class Caminante(compiladorVisitor):
    
    def __init__(self):
        self.c3d = CodigoTresDirecciones()
        self._modo_expresion = False

    def nuevaTemporal(self):
        return self.c3d.nuevaTemporal()

    def nuevoLabel(self):
        return self.c3d.nuevoLabel()

    # PROGRAMA
    def visitPrograma(self, ctx):
        if ctx.instrucciones():
            self.visitInstrucciones(ctx.instrucciones())
        
        self.codigoOriginal = [line for line in self.c3d.output if isinstance(line, str) and line]
        optimizado = self.optimizarOutput(self.codigoOriginal[:]) or []
        self.codigoOptimizado = optimizado
        self.c3d.output = optimizado
        
        try:
            self.c3d.escribirCodigo()
        except Exception:
            for l in optimizado:
                print(l)
        return None

    # EXPRESIONES
    def visitFactor(self, ctx):
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        elif ctx.DECIMAL():
            return ctx.DECIMAL().getText()
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.exp():
            return self.visitExp(ctx.exp())
        elif ctx.llamada():
            return self.visitLlamada(ctx.llamada())
        return None

    def visitTerm(self, ctx):
        izq = self.visitFactor(ctx.factor()) if ctx.factor() else None
        if ctx.t() and ctx.t().getChildCount() > 0:
            return self._procesarTermRest(ctx.t(), izq)
        return izq

    def _procesarTermRest(self, ctx, izq):
        if ctx.getChildCount() == 0:
            return izq
        if ctx.getChildCount() >= 2:
            operador = ctx.getChild(0).getText()
            der = self.visitFactor(ctx.factor()) if ctx.factor() else None
            
            if isinstance(izq, str) and isinstance(der, str):
                res = self._evalExpresion(izq, operador, der)
                if res is not None:
                    if ctx.getChildCount() > 2:
                        return self._procesarTermRest(ctx.getChild(2), res)
                    return res
            
            return f"({izq} {operador} {der})"
        return izq

    def visitExp(self, ctx):
        izq = self.visitTerm(ctx.term()) if ctx.term() else None
        if ctx.e() and ctx.e().getChildCount() > 0:
            return self._procesarExpRest(ctx.e(), izq)
        return izq

    def _procesarExpRest(self, ctx, izq):
        if ctx.getChildCount() == 0:
            return izq
        if ctx.getChildCount() >= 2:
            operador = ctx.getChild(0).getText()
            der = self.visitTerm(ctx.term()) if ctx.term() else None
            
            if isinstance(izq, str) and isinstance(der, str):
                res = self._evalExpresion(izq, operador, der)
                if res is not None:
                    if ctx.getChildCount() > 2:
                        return self._procesarExpRest(ctx.getChild(2), res)
                    return res
            
            return f"({izq} {operador} {der})"
        return izq

    def visitOpal(self, ctx):
        return self.visitExp(ctx.exp()) if ctx.exp() else None

    def _evalExpresion(self, izq, op, der):
        try:
            def isNum(s):
                if not s:
                    return False
                try:
                    float(s.replace('(', '').replace(')', ''))
                    return True
                except:
                    return False
            
            izq_clean = izq.replace('(', '').replace(')', '')
            der_clean = der.replace('(', '').replace(')', '')
            
            if isNum(izq_clean) and isNum(der_clean):
                a = float(izq_clean)
                b = float(der_clean)
                if op == '+': res = a + b
                elif op == '-': res = a - b
                elif op == '*': res = a * b
                elif op == '/': 
                    if b == 0: return None
                    res = a / b
                elif op == '%': res = a % b
                else: return None
                
                if res is not None:
                    if float(res).is_integer():
                        return str(int(res))
                    return str(res)
        except:
            pass
        return None

    # COMPARACIONES
    def _evaluarComparacion(self, izq, op, der):
        try:
            def isNum(s):
                try:
                    float(s.replace('(', '').replace(')', ''))
                    return True
                except:
                    return False
            
            izq_clean = izq.replace('(', '').replace(')', '')
            der_clean = der.replace('(', '').replace(')', '')
            
            if isNum(izq_clean) and isNum(der_clean):
                a = float(izq_clean)
                b = float(der_clean)
                res = False
                if op == '==': res = (a == b)
                elif op == '!=': res = (a != b)
                elif op == '<': res = (a < b)
                elif op == '<=': res = (a <= b)
                elif op == '>': res = (a > b)
                elif op == '>=': res = (a >= b)
                return '1' if res else '0'
        except:
            pass
        return None

    # STATEMENTS
    def visitInstrucciones(self, ctx):
        return self.visitChildren(ctx)

    def visitInstruccion(self, ctx):
        return self.visitChildren(ctx)

    # ASIGNACION
    def visitAsignacion(self, ctx):
        if ctx.ID() and ctx.opal():
            variable = ctx.ID().getText()
            valor = self.visitOpal(ctx.opal())
            if valor is not None:
                self.c3d.asignacion(variable, valor)
        return None

    # INCDEC (++ / --)
    def visitIincdec(self, ctx):
        if ctx.INCDEC():
            op = ctx.INCDEC().getText()
            if ctx.ID():
                var = ctx.ID().getText()
                if op == '++':
                    temp = self.nuevaTemporal()
                    self.c3d.operacion(temp, var, '+', '1')
                    self.c3d.asignacion(var, temp)
                elif op == '--':
                    temp = self.nuevaTemporal()
                    self.c3d.operacion(temp, var, '-', '1')
                    self.c3d.asignacion(var, temp)
        return None

    # IF
    def visitIif(self, ctx):
        condicion_ctx = ctx.condicion()
        instruccion_if = ctx.instruccion()
        ielse_ctx = ctx.ielse()
        
        es_simple = self._esCondicionSimple(condicion_ctx)
        
        if es_simple:
            self._generarIfSimple(condicion_ctx, instruccion_if, ielse_ctx)
        else:
            self._generarIfCompleto(condicion_ctx, instruccion_if, ielse_ctx)
        
        return None

    def _esCondicionSimple(self, ctx):
        if not ctx or not ctx.orExp() or not ctx.orExp().andExp():
            return False
        andExp = ctx.orExp().andExp()
        if andExp.andExpRest() and andExp.andExpRest().getChildCount() > 0:
            return False
        if ctx.orExp().orExpRest() and ctx.orExp().orExpRest().getChildCount() > 0:
            return False
        return True

    def _generarIfSimple(self, ctx, instruccion_if, ielse_ctx):
        if not ctx.orExp() or not ctx.orExp().andExp():
            return
        
        andExp = ctx.orExp().andExp()
        if not andExp.comparacion():
            return
        
        comp = andExp.comparacion()
        izq = self._obtenerValorTermino(comp.termino()) if comp.termino() else None
        
        op = None
        der = None
        if comp.comparacionRest():
            rest = comp.comparacionRest()
            if rest.COMP():
                op = rest.COMP().getText()
            if rest.termino():
                der = self._obtenerValorTermino(rest.termino())
        
        if not izq or not op or not der:
            return
        
        tiene_else = ielse_ctx is not None and ielse_ctx.getChildCount() > 0
        
        if not tiene_else:
            LExit = self.nuevoLabel()
            self.c3d.agregarInstruccion(f"ifFalse {izq} {op} {der} goto {LExit}")
            if instruccion_if:
                self.visitInstruccion(instruccion_if)
            self.c3d.agregarInstruccion(f"{LExit}:")
        else:
            LElse = self.nuevoLabel()
            LExit = self.nuevoLabel()
            self.c3d.agregarInstruccion(f"ifFalse {izq} {op} {der} goto {LElse}")
            if instruccion_if:
                self.visitInstruccion(instruccion_if)
            self.c3d.agregarInstruccion(f"goto {LExit}")
            self.c3d.agregarInstruccion(f"{LElse}:")
            if ielse_ctx:
                self.visitIelse(ielse_ctx)
            self.c3d.agregarInstruccion(f"{LExit}:")

    def _generarIfCompleto(self, ctx, instruccion_if, ielse_ctx):
        expr_bool = self._evaluarCondicion(ctx)
        
        if not ielse_ctx:
            LExit = self.nuevoLabel()
            self.c3d.agregarInstruccion(f"ifFalse {expr_bool} goto {LExit}")
            if instruccion_if:
                self.visitInstruccion(instruccion_if)
            self.c3d.agregarInstruccion(f"{LExit}:")
        else:
            LElse = self.nuevoLabel()
            LExit = self.nuevoLabel()
            self.c3d.agregarInstruccion(f"ifFalse {expr_bool} goto {LElse}")
            if instruccion_if:
                self.visitInstruccion(instruccion_if)
            self.c3d.agregarInstruccion(f"goto {LExit}")
            self.c3d.agregarInstruccion(f"{LElse}:")
            if ielse_ctx:
                self.visitIelse(ielse_ctx)
            self.c3d.agregarInstruccion(f"{LExit}:")

    def _evaluarCondicion(self, ctx):
        if not ctx.orExp():
            return "0"
        
        orExp = ctx.orExp()
        
        noOr = not orExp.orExpRest() or orExp.orExpRest().getChildCount() == 0
        noAnd = not orExp.andExp() or not orExp.andExp().andExpRest() or orExp.andExp().andExpRest().getChildCount() == 0
        
        if noOr and noAnd:
            comp = orExp.andExp().comparacion() if orExp.andExp() else None
            if comp:
                return self._evaluarComparacionSimple(comp)
        
        return self._evaluarExpresionBooleana(orExp)

    def _evaluarComparacionSimple(self, comp):
        izq = self._obtenerValorTermino(comp.termino()) if comp.termino() else None
        if not izq:
            return "0"
        
        op = None
        der = None
        if comp.comparacionRest():
            rest = comp.comparacionRest()
            if rest.COMP():
                op = rest.COMP().getText()
            if rest.termino():
                der = self._obtenerValorTermino(rest.termino())
        
        if not op or not der:
            return "0"
        
        res = self._evaluarComparacion(izq, op, der)
        if res:
            return res
        
        t = self.nuevaTemporal()
        self.c3d.operacion(t, izq, op, der)
        return t

    def _evaluarExpresionBooleana(self, ctx):
        # ctx is orExp context
        andExp = ctx.andExp()
        if not andExp:
            return "0"
        
        result = self.nuevaTemporal()
        
        self._evaluarAndGroup(andExp, result)
        
        # Process OR chain with short-circuit
        if ctx.orExpRest() and ctx.orExpRest().getChildCount() > 0:
            LEnd = self.nuevoLabel()
            self._procesarOrChain(ctx.orExpRest(), result, LEnd)
            self.c3d.agregarInstruccion(f"{LEnd}:")
        
        return result

    def _evaluarAndGroup(self, andExpCtx, result):
        comp1 = andExpCtx.comparacion()
        if comp1:
            val1 = self._evaluarComparacionSimple(comp1)
            self.c3d.asignacion(result, val1)
            
            if andExpCtx.andExpRest() and andExpCtx.andExpRest().getChildCount() > 0:
                LFalse = self.nuevoLabel()
                self.c3d.agregarInstruccion(f"ifFalse {result} goto {LFalse}")
                self._procesarAndExpRest(andExpCtx.andExpRest(), result, LFalse)
                self.c3d.agregarInstruccion(f"{LFalse}:")
                self.c3d.asignacion(result, '0')

    def _procesarOrChain(self, ctx, result, LEnd):
        if ctx.getChildCount() == 0:
            return
        
        LNext = self.nuevoLabel()
        self.c3d.agregarInstruccion(f"ifTrue {result} goto {LNext}")
        
        if hasattr(ctx, 'andExp') and ctx.andExp():
            self._evaluarAndGroup(ctx.andExp(), result)
            self.c3d.agregarInstruccion(f"ifTrue {result} goto {LEnd}")
        
        self.c3d.agregarInstruccion(f"{LNext}:")
        
        if hasattr(ctx, 'orExpRest') and ctx.orExpRest() and ctx.orExpRest().getChildCount() > 0:
            self._procesarOrChain(ctx.orExpRest(), result, LEnd)

    def _procesarAndExpRest(self, ctx, resultTemp, LFalso):
        if ctx.comparacion():
            val = self._evaluarComparacionSimple(ctx.comparacion())
            temp = self.nuevaTemporal()
            self.c3d.operacion(temp, resultTemp, '&&', val)
            self.c3d.agregarInstruccion(f"ifFalse {temp} goto {LFalso}")
            self.c3d.asignacion(resultTemp, temp)
        
        if ctx.andExpRest() and ctx.andExpRest().getChildCount() > 0:
            self._procesarAndExpRest(ctx.andExpRest(), resultTemp, LFalso)

    def _obtenerValorTermino(self, ctx):
        if not ctx:
            return None
        if hasattr(ctx, 'opal') and ctx.opal():
            return self.visitOpal(ctx.opal())
        elif hasattr(ctx, 'LIT') and ctx.LIT():
            return ctx.LIT().getText()
        elif hasattr(ctx, 'condicion') and ctx.condicion():
            return self._evaluarCondicion(ctx.condicion())
        return None

    # WHILE
    def visitIwhile(self, ctx):
        LInicio = self.nuevoLabel()
        LFin = self.nuevoLabel()
        
        self.c3d.agregarInstruccion(f"{LInicio}:")
        
        if ctx.condicion():
            condicion = self._evaluarCondicion(ctx.condicion())
            self.c3d.agregarInstruccion(f"ifFalse {condicion} goto {LFin}")
        
        if ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        
        self.c3d.agregarInstruccion(f"goto {LInicio}")
        self.c3d.agregarInstruccion(f"{LFin}:")
        return None

    # FOR
    def visitIfor(self, ctx):
        LInicio = self.nuevoLabel()
        LFin = self.nuevoLabel()
        
        if ctx.asignacion():
            self.visitAsignacion(ctx.asignacion())
        elif ctx.declaracion():
            self.visitDeclaracion(ctx.declaracion())
        
        self.c3d.agregarInstruccion(f"{LInicio}:")
        
        if ctx.comparacion() and ctx.comparacion().getText():
            condicion = self._evaluarCondicion(ctx.comparacion())
            self.c3d.agregarInstruccion(f"ifFalse {condicion} goto {LFin}")
        
        if ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        
        if ctx.iincdec():
            self.visitIincdec(ctx.iincdec())
        
        self.c3d.agregarInstruccion(f"goto {LInicio}")
        self.c3d.agregarInstruccion(f"{LFin}:")
        return None

    # FUNCIONES
    def visitFuncion(self, ctx):
        nombre = None
        if hasattr(ctx, 'ID') and ctx.ID():
            nombre = ctx.ID().getText()
        
        if nombre:
            self.c3d.agregarInstruccion(f"{nombre}:")
        
        if hasattr(ctx, 'bloque') and ctx.bloque():
            self.visitBloque(ctx.bloque())
        
        return None

    def visitProto(self, ctx):
        return None

    def visitIelse(self, ctx):
        if hasattr(ctx, 'instruccion') and ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        return None

    def visitLlamada(self, ctx):
        if hasattr(ctx, 'ID'):
            funcName = ctx.ID().getText()
            args = []
            if hasattr(ctx, 'argumentosLlamada') and ctx.argumentosLlamada():
                args = self.visitArgumentosLlamada(ctx.argumentosLlamada()) or []
            return self.c3d.llamadaFuncion(funcName, args)
        return None

    def visitArgumentosLlamada(self, ctx):
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
        return self.visitChildren(ctx)

    def visitIreturn(self, ctx):
        if hasattr(ctx, 'opal') and ctx.opal():
            valor = self.visitOpal(ctx.opal())
            if valor:
                self.c3d.retorno(valor)
        elif hasattr(ctx, 'condicion') and ctx.condicion():
            valor = self._evaluarCondicion(ctx.condicion())
            if valor:
                self.c3d.retorno(valor)
        else:
            self.c3d.retorno()
        return None

    # DECLARACION
    def visitDeclaracion(self, ctx):
        tipo = None
        if hasattr(ctx, 'tipo') and ctx.tipo():
            tipo = ctx.tipo().getText()
        
        if hasattr(ctx, 'ID') and ctx.ID():
            varName = ctx.ID().getText()
            
            if hasattr(ctx, 'inic') and ctx.inic():
                valor = self.visitInic(ctx.inic())
                if valor is not None:
                    self.c3d.asignacion(varName, valor)
                else:
                    self.c3d.asignacion(varName, '0')
            else:
                if tipo == 'double':
                    self.c3d.asignacion(varName, '0.0')
                else:
                    self.c3d.asignacion(varName, '0')
        
        if hasattr(ctx, 'listavar') and ctx.listavar():
            self.visitListavar(ctx.listavar(), tipo)
        
        return None

    def visitInic(self, ctx):
        if hasattr(ctx, 'opal') and ctx.opal():
            return self.visitOpal(ctx.opal())
        return None

    def visitListavar(self, ctx, tipo=None):
        if hasattr(ctx, 'ID') and ctx.ID():
            varName = ctx.ID().getText()
            
            if hasattr(ctx, 'inic') and ctx.inic():
                valor = self.visitInic(ctx.inic())
                if valor is not None:
                    self.c3d.asignacion(varName, valor)
                else:
                    if tipo == 'double':
                        self.c3d.asignacion(varName, '0.0')
                    else:
                        self.c3d.asignacion(varName, '0')
            else:
                if tipo == 'double':
                    self.c3d.asignacion(varName, '0.0')
                else:
                    self.c3d.asignacion(varName, '0')
        
        if hasattr(ctx, 'listavar') and ctx.listavar():
            self.visitListavar(ctx.listavar(), tipo)
        return None

    def visitArgumento(self, ctx):
        return None

    def visitListaParametros(self, ctx):
        return None

    # OPTIMIZACIONES
    def optimizarOutput(self, lineas):
        if lineas is None:
            return []
        lineas = [l for l in lineas if isinstance(l, str) and l]
        
        for _ in range(25):
            originalLen = len(lineas)
            lineas = self.constantFolding(lineas)
            lineas = self.eliminarSaltosRedundantes(lineas)
            lineas = self.propagarYCadenas(lineas)
            lineas = self.eliminarTemporalesRedundantes(lineas)
            lineas = self.simplificarExpresiones(lineas)
            if len(lineas) == originalLen:
                break
        
        return lineas

    def endsWithLabel(self, s):
        s = s.strip()
        if ':' in s:
            return s.endswith(':')
        return False

    def startsWithGoto(self, s):
        s = s.strip()
        return s.startswith('goto ')

    def startsWithIfFalse(self, s):
        s = s.strip()
        return s.startswith('ifFalse ')

    def startsWithIfTrue(self, s):
        s = s.strip()
        return s.startswith('ifTrue ')

    def isTemp(self, var):
        return var.startswith('t') and var[1:].isdigit()

    def propagarYCadenas(self, lineas):
        resultado = []
        mapa = {}
        
        for i, linea in enumerate(lineas):
            if not isinstance(linea, str):
                resultado.append(linea)
                mapa = {}
                continue
            
            stripped = linea.strip()
            
            if self.endsWithLabel(stripped) or self.startsWithGoto(stripped) or self.startsWithIfFalse(stripped) or self.startsWithIfTrue(stripped):
                resultado.append(linea)
                mapa = {}
                continue
            
            if '=' in stripped:
                partes = stripped.split('=')
                if len(partes) == 2:
                    dest = partes[0].strip()
                    src = partes[1].strip()
                    
                    if src in mapa:
                        src = mapa[src]
                    
                    if self.isTemp(dest):
                        mapa[dest] = src
                    
                    resultado.append(f"{dest} = {src}")
                    continue
            
            lineaMod = linea
            for temp, val in mapa.items():
                lineaMod = re.sub(rf'\b{re.escape(temp)}\b', val, lineaMod)
            
            resultado.append(lineaMod)
        
        return resultado

    def eliminarTemporalesRedundantes(self, lineas):
        resultado = []
        usosTemporales = set()
        
        for linea in lineas:
            if not isinstance(linea, str):
                continue
            if '=' in linea:
                idx = linea.rfind('=')
                rhs = linea[idx+1:].strip()
                temps = self.findTemps(rhs)
                for t in temps:
                    usosTemporales.add(t)
            
            if linea.startswith('ifFalse '):
                resto = linea[8:]
                idx = resto.rfind(' goto')
                if idx > 0:
                    cond = resto[:idx].strip()
                    temps = self.findTemps(cond)
                    for t in temps:
                        usosTemporales.add(t)
        
        for linea in lineas:
            if not isinstance(linea, str):
                resultado.append(linea)
                continue
            
            if '=' in linea:
                partes = linea.split('=')
                if len(partes) == 2:
                    dest = partes[0].strip()
                    if self.isTemp(dest) and dest not in usosTemporales:
                        continue
            
            resultado.append(linea)
        
        return resultado

    def findTemps(self, s):
        temps = []
        palabra = ''
        for c in s:
            if c.isalnum():
                palabra += c
            else:
                if palabra.startswith('t') and len(palabra) > 1 and palabra[1:].isdigit():
                    temps.append(palabra)
                palabra = ''
        if palabra.startswith('t') and len(palabra) > 1 and palabra[1:].isdigit():
            temps.append(palabra)
        return temps

    def simplificarExpresiones(self, lineas):
        resultado = []
        
        for linea in lineas:
            if not isinstance(linea, str):
                resultado.append(linea)
                continue
            
            if '=' in linea:
                partes = linea.split('=')
                if len(partes) == 2:
                    dest = partes[0].strip()
                    expr = partes[1].strip()
                    
                    if ' == ' in expr:
                        ops = expr.split(' == ')
                        if len(ops) == 2 and ops[0] == ops[1]:
                            resultado.append(f"{dest} = 1")
                            continue
                    
                    if ' != ' in expr:
                        ops = expr.split(' != ')
                        if len(ops) == 2 and ops[0] == ops[1]:
                            resultado.append(f"{dest} = 0")
                            continue
                    
                    if ' > ' in expr:
                        ops = expr.split(' > ')
                        if len(ops) == 2 and ops[0] == ops[1]:
                            resultado.append(f"{dest} = 0")
                            continue
                    
                    if ' < ' in expr:
                        ops = expr.split(' < ')
                        if len(ops) == 2 and ops[0] == ops[1]:
                            resultado.append(f"{dest} = 0")
                            continue
            
            resultado.append(linea)
        
        return resultado

    def constantFolding(self, lineas):
        resultado = []
        
        for linea in lineas:
            if not isinstance(linea, str):
                resultado.append(linea)
                continue
            
            if '=' in linea:
                partes = linea.split('=')
                if len(partes) == 2:
                    destino = partes[0].strip()
                    expr = partes[1].strip()
                    
                    res = self.evalArit(expr)
                    if res:
                        resultado.append(f"{destino} = {res}")
                        continue
            
            resultado.append(linea)
        
        return resultado

    def evalArit(self, e):
        ops = [('+', lambda a,b: a+b), ('-', lambda a,b: a-b), 
               ('*', lambda a,b: a*b), ('/', lambda a,b: a/b if b != 0 else None)]
        
        for op, func in ops:
            if op in e:
                parts = e.split(op)
                if len(parts) == 2:
                    try:
                        a = float(parts[0].strip())
                        b = float(parts[1].strip())
                        res = func(a, b)
                        if res is not None:
                            if float(res).is_integer():
                                return str(int(res))
                            return str(res)
                    except:
                        pass
        return None

    def eliminarSaltosRedundantes(self, lineas):
        resultado = []
        i = 0
        
        while i < len(lineas):
            linea = lineas[i]
            if not isinstance(linea, str):
                resultado.append(linea)
                i += 1
                continue
            
            if linea.startswith('goto '):
                etiqueta = linea[5:].strip()
                if i + 1 < len(lineas):
                    sig = lineas[i + 1]
                    if isinstance(sig, str) and sig.strip() == f'{etiqueta}:':
                        i += 1
                        continue
            
            resultado.append(linea)
            i += 1
        
        return resultado

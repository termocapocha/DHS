# === IMPORTS ===
import re
from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser
from CodigoTresDirecciones import CodigoTresDirecciones

# === VISITOR: GENERACION DE CODIGO INTERMEDIO ===
class Caminante(compiladorVisitor):
    
    def __init__(self):
        self.c3d = CodigoTresDirecciones()
        self._modo_expresion = False
        self._breakLabels = []
        self._continueLabels = []
        self._funcionActual = None
        self._tipoRetornoActual = None

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
        
        return None

    # EXPRESIONES
    def visitFactor(self, ctx):
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        elif ctx.DECIMAL():
            return ctx.DECIMAL().getText()
        elif ctx.STRING():
            s = ctx.STRING().getText()
            return s
        elif ctx.ID():
            idName = ctx.ID().getText()
            if ctx.PA() and ctx.exp():
                index = self.visitExp(ctx.exp())
                t = self.nuevaTemporal()
                self.c3d.agregarInstruccion(f"{t} = {idName}[{index}]")
                return t
            return idName
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

    # INSTRUCCIONES
    def visitInstrucciones(self, ctx):
        return self.visitChildren(ctx)

    def visitInstruccion(self, ctx):
        if ctx.BREAK():
            return self.visitBreak(ctx)
        if ctx.CONTINUE():
            return self.visitContinue(ctx)
        return self.visitChildren(ctx)

    # ASIGNACION
    def visitAsignacion(self, ctx):
        if ctx.ID() and ctx.opal():
            variable = ctx.ID().getText()
            valor = self.visitOpal(ctx.opal())
            if valor is not None:
                if ctx.getChildCount() > 2 and ctx.getChild(1).getText() == '=' and ctx.getChild(2).getText() == '[':
                    pass
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
        ielse_ctx = ctx.ielse2()
        
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
        
        temp = self.nuevaTemporal()
        self.c3d.operacion(temp, izq, op, der)
        
        if not tiene_else:
            LExit = self.nuevoLabel()
            self.c3d.agregarInstruccion(f"ifFalse {temp} goto {LExit}")
            if instruccion_if:
                self.visitInstruccion(instruccion_if)
            self.c3d.agregarInstruccion(f"{LExit}:")
        else:
            LElse = self.nuevoLabel()
            LExit = self.nuevoLabel()
            self.c3d.agregarInstruccion(f"ifFalse {temp} goto {LElse}")
            if instruccion_if:
                self.visitInstruccion(instruccion_if)
            self.c3d.agregarInstruccion(f"goto {LExit}")
            self.c3d.agregarInstruccion(f"{LElse}:")
            if ielse_ctx:
                self.visitIelse2(ielse_ctx)
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
                self.visitIelse2(ielse_ctx)
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
            return izq
        
        res = self._evaluarComparacion(izq, op, der)
        if res:
            return res
        
        t = self.nuevaTemporal()
        self.c3d.operacion(t, izq, op, der)
        return t

    def _evaluarExpresionBooleana(self, ctx):
        andExp = ctx.andExp()
        if not andExp:
            return "0"
        
        result = self.nuevaTemporal()
        
        self._evaluarAndGroup(andExp, result)
        
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

    # BREAK / CONTINUE
    def visitBreak(self, ctx):
        if self._breakLabels:
            self.c3d.agregarInstruccion(f"goto {self._breakLabels[-1]}")
        return None

    def visitContinue(self, ctx):
        if self._continueLabels:
            self.c3d.agregarInstruccion(f"goto {self._continueLabels[-1]}")
        return None

    # DO-WHILE
    def visitIdowhile(self, ctx):
        LInicio = self.nuevoLabel()
        LContinue = self.nuevoLabel()
        LFin = self.nuevoLabel()
        
        self._breakLabels.append(LFin)
        self._continueLabels.append(LContinue)
        
        self.c3d.agregarInstruccion(f"{LInicio}:")
        
        if ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        
        self.c3d.agregarInstruccion(f"{LContinue}:")
        
        if ctx.condicion():
            condicion = self._evaluarCondicion(ctx.condicion())
            self.c3d.agregarInstruccion(f"ifTrue {condicion} goto {LInicio}")
        
        self.c3d.agregarInstruccion(f"{LFin}:")
        
        self._breakLabels.pop()
        self._continueLabels.pop()
        return None

    # SWITCH
    def visitIswitch(self, ctx):
        LFin = self.nuevoLabel()
        self._breakLabels.append(LFin)
        
        valorSwitch = self._evaluarCondicion(ctx.condicion()) if ctx.condicion() else '0'
        
        casos = []
        tieneDefault = False
        if ctx.casosSwitch():
            self._recogerCasos(ctx.casosSwitch(), casos)
        
        labelsCasos = []
        for i, c in enumerate(casos):
            lbl = self.nuevoLabel()
            labelsCasos.append(lbl)
        
        for i, caso in enumerate(casos):
            if caso is None:
                continue
            t = self.nuevaTemporal()
            self.c3d.agregarInstruccion(f"{t} = {valorSwitch} == {caso}")
            self.c3d.agregarInstruccion(f"ifTrue {t} goto {labelsCasos[i]}")
        
        if not tieneDefault:
            self.c3d.agregarInstruccion(f"goto {LFin}")
        
        idx = 0
        if ctx.casosSwitch():
            self._visitarCasos(ctx.casosSwitch(), labelsCasos, idx, LFin)
        
        self.c3d.agregarInstruccion(f"{LFin}:")
        self._breakLabels.pop()
        return None

    def _recogerCasos(self, ctx, casos):
        if ctx.CASE() and ctx.opal():
            val = self.visitOpal(ctx.opal())
            casos.append(val)
            if ctx.casosSwitch():
                self._recogerCasos(ctx.casosSwitch(), casos)
        elif ctx.DEFAULT():
            casos.append(None)

    def _visitarCasos(self, ctx, labelsCasos, idx, LFin):
        if ctx.CASE():
            if idx < len(labelsCasos):
                self.c3d.agregarInstruccion(f"{labelsCasos[idx]}:")
            if ctx.instrucciones():
                self.visitInstrucciones(ctx.instrucciones())
            self.c3d.agregarInstruccion(f"goto {LFin}")
            if ctx.casosSwitch():
                self._visitarCasos(ctx.casosSwitch(), labelsCasos, idx + 1, LFin)
        elif ctx.DEFAULT():
            lblDefault = self.nuevoLabel()
            self.c3d.agregarInstruccion(f"{lblDefault}:")
            if ctx.instrucciones():
                self.visitInstrucciones(ctx.instrucciones())

    # WHILE
    def visitIwhile(self, ctx):
        LInicio = self.nuevoLabel()
        LContinue = self.nuevoLabel()
        LFin = self.nuevoLabel()
        
        self._breakLabels.append(LFin)
        self._continueLabels.append(LContinue)
        
        self.c3d.agregarInstruccion(f"{LInicio}:")
        
        if ctx.condicion():
            condicion = self._evaluarCondicion(ctx.condicion())
            self.c3d.agregarInstruccion(f"ifFalse {condicion} goto {LFin}")
        
        if ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        
        self.c3d.agregarInstruccion(f"{LContinue}:")
        self.c3d.agregarInstruccion(f"goto {LInicio}")
        self.c3d.agregarInstruccion(f"{LFin}:")
        
        self._breakLabels.pop()
        self._continueLabels.pop()
        return None

    # FOR
    def visitIfor(self, ctx):
        LInicio = self.nuevoLabel()
        LContinue = self.nuevoLabel()
        LFin = self.nuevoLabel()
        
        self._breakLabels.append(LFin)
        self._continueLabels.append(LContinue)
        
        if ctx.asignacion():
            self.visitAsignacion(ctx.asignacion())
        elif ctx.declaracion():
            self.visitDeclaracion(ctx.declaracion())
        elif ctx.opal():
            self.visitOpal(ctx.opal())
        
        self.c3d.agregarInstruccion(f"{LInicio}:")
        
        if ctx.comparacion():
            comp = ctx.comparacion()
            izq = self._obtenerValorTermino(comp.termino()) if comp.termino() else None
            op = None
            der = None
            if comp.comparacionRest():
                rest = comp.comparacionRest()
                if rest.COMP():
                    op = rest.COMP().getText()
                if rest.termino():
                    der = self._obtenerValorTermino(rest.termino())
            if izq and op and der:
                t = self.nuevaTemporal()
                self.c3d.operacion(t, izq, op, der)
                self.c3d.agregarInstruccion(f"ifFalse {t} goto {LFin}")
            elif izq:
                self.c3d.agregarInstruccion(f"ifFalse {izq} goto {LFin}")
        
        if ctx.instruccion():
            self.visitInstruccion(ctx.instruccion())
        
        self.c3d.agregarInstruccion(f"{LContinue}:")
        if ctx.iincdec():
            self.visitIincdec(ctx.iincdec())
        
        self.c3d.agregarInstruccion(f"goto {LInicio}")
        self.c3d.agregarInstruccion(f"{LFin}:")
        
        self._breakLabels.pop()
        self._continueLabels.pop()
        return None

    # FUNCIONES
    def visitFuncion(self, ctx):
        if hasattr(ctx, 'ID') and ctx.ID():
            self._funcionActual = ctx.ID().getText()
            if hasattr(ctx, 'tipo') and ctx.tipo():
                self._tipoRetornoActual = ctx.tipo().getText()
        
        if self._funcionActual:
            self.c3d.agregarInstruccion(f"{self._funcionActual}:")
        
        if hasattr(ctx, 'bloque') and ctx.bloque():
            self.visitBloque(ctx.bloque())
        
        self._funcionActual = None
        self._tipoRetornoActual = None
        return None

    def visitProto(self, ctx):
        return None

    def visitIelse2(self, ctx):
        if hasattr(ctx, 'iif') and ctx.iif():
            self.visitIif(ctx.iif())
        elif hasattr(ctx, 'instruccion') and ctx.instruccion():
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
        if ctx.opal():
            valor = self.visitOpal(ctx.opal())
            if valor is not None:
                self.c3d.retorno(valor)
                return None
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

    # === OPTIMIZACIONES ===
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
            lineas = self.eliminarAsignacionesTriviales(lineas)
            lineas = self.eliminarAsignacionesSobrescritas(lineas)
            lineas = self.simplificarEstructurasControl(lineas)
            lineas = self.eliminarCodigoMuerto(lineas)
            lineas = self.eliminarEtiquetasVacias(lineas)
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
                lineaMod = re.sub(rf'(?<!\w){re.escape(temp)}(?!\w)', val, lineaMod)
            
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
            
            if linea.startswith('ifFalse ') or linea.startswith('ifTrue '):
                prefix = 'ifFalse ' if linea.startswith('ifFalse ') else 'ifTrue '
                resto = linea[len(prefix):]
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
        e = e.strip()
        if not e:
            return None
        # Intentar evaluar directamente si es un numero
        try:
            val = float(e)
            if val.is_integer():
                return str(int(val))
            return str(val)
        except:
            pass
        # Si hay parentesis, intentar evaluar el interior
        if e.startswith('(') and e.endswith(')'):
            inner = self.evalArit(e[1:-1])
            if inner is not None:
                return inner
            return None
        # Buscar operador de menor precedencia primero (+ / - fuera de parentesis)
        ops = [('+', lambda a,b: a+b), ('-', lambda a,b: a-b)]
        for op, func in ops:
            idx = self._findOpOutsideParens(e, op)
            if idx > 0:
                izq = self.evalArit(e[:idx])
                der = self.evalArit(e[idx+1:])
                if izq is not None and der is not None:
                    res = func(float(izq), float(der))
                    if float(res).is_integer():
                        return str(int(res))
                    return str(res)
                return None
        
        ops2 = [('*', lambda a,b: a*b), ('/', lambda a,b: a/b if b != 0 else None),
                ('%', lambda a,b: a % b)]
        for op, func in ops2:
            idx = self._findOpOutsideParens(e, op)
            if idx > 0:
                izq = self.evalArit(e[:idx])
                der = self.evalArit(e[idx+1:])
                if izq is not None and der is not None:
                    res = func(float(izq), float(der))
                    if float(res).is_integer():
                        return str(int(res))
                    return str(res)
                return None
        return None

    def _findOpOutsideParens(self, s, op):
        parens = 0
        for i, ch in enumerate(s):
            if ch == '(':
                parens += 1
            elif ch == ')':
                parens -= 1
            elif ch == op and parens == 0:
                return i
        return -1

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

    def eliminarAsignacionesTriviales(self, lineas):
        resultado = []
        for linea in lineas:
            if not isinstance(linea, str):
                resultado.append(linea)
                continue
            if '=' in linea and not linea.startswith('if'):
                partes = linea.split('=', 1)
                var = partes[0].strip()
                expr = partes[1].strip()
                if var == expr:
                    continue
            resultado.append(linea)
        return resultado

    def eliminarAsignacionesSobrescritas(self, lineas):
        resultado = []
        ultima_def = {}
        for linea in lineas:
            if not isinstance(linea, str):
                resultado.append(linea)
                continue
            stripped = linea.strip()
            if self.endsWithLabel(stripped) or self.startsWithGoto(stripped) or self.startsWithIfFalse(stripped) or self.startsWithIfTrue(stripped):
                ultima_def.clear()
                resultado.append(linea)
                continue
            if '=' in stripped and not stripped.startswith('if'):
                partes = stripped.split('=', 1)
                var = partes[0].strip()
                if var in ultima_def:
                    idx = ultima_def[var]
                    resultado[idx] = None
                ultima_def[var] = len(resultado)
                resultado.append(linea)
            else:
                resultado.append(linea)
        return [l for l in resultado if l is not None]

    def simplificarEstructurasControl(self, lineas):
        cambio = True
        while cambio:
            cambio = False
            resultado = []
            i = 0
            while i < len(lineas):
                linea = lineas[i]
                if not isinstance(linea, str):
                    resultado.append(linea)
                    i += 1
                    continue
                found = False
                stripped = linea.strip()
                if stripped.startswith('ifFalse') and i + 5 < len(lineas):
                    resto = stripped[len('ifFalse '):]
                    goto_idx = resto.rfind(' goto ')
                    if goto_idx > 0:
                        temp = resto[:goto_idx].strip()
                        label_else = resto[goto_idx + 6:].strip()
                        idx_goto_fin = None
                        idx_label_else = None
                        idx_label_fin = None
                        for j in range(i + 1, min(i + 8, len(lineas))):
                            s = lineas[j].strip() if isinstance(lineas[j], str) else ''
                            if s.startswith('goto ') and idx_goto_fin is None:
                                idx_goto_fin = j
                            if s.endswith(':') and s[:-1].strip() == label_else and idx_label_else is None:
                                idx_label_else = j
                            if s.endswith(':') and idx_goto_fin is not None and idx_label_else is not None and j > idx_label_else and idx_label_fin is None:
                                idx_label_fin = j
                                break
                        if idx_goto_fin and idx_label_else and idx_label_fin:
                            then_body = [lineas[j] for j in range(i + 1, idx_goto_fin)]
                            else_body = [lineas[j] for j in range(idx_label_else + 1, idx_label_fin)]
                            if len(then_body) == len(else_body) and all(
                                (isinstance(a, str) and isinstance(b, str) and a.strip() == b.strip())
                                for a, b in zip(then_body, else_body)
                            ):
                                for line in then_body:
                                    resultado.append(line)
                                i = idx_label_fin + 1
                                cambio = True
                                found = True
                if found:
                    continue
                resultado.append(linea)
                i += 1
            lineas = resultado
        return lineas

    def eliminarCodigoMuerto(self, lineas):
        resultado = []
        muerto = False
        for linea in lineas:
            if not isinstance(linea, str):
                resultado.append(linea)
                continue
            stripped = linea.strip()
            if self.endsWithLabel(stripped):
                muerto = False
                resultado.append(linea)
                continue
            if muerto:
                continue
            resultado.append(linea)
            if stripped.startswith('return') or stripped.startswith('goto '):
                muerto = True
        return resultado

    def eliminarEtiquetasVacias(self, lineas):
        resultado = []
        for linea in lineas:
            if not isinstance(linea, str):
                resultado.append(linea)
                continue
            stripped = linea.strip()
            if stripped.endswith(':') and len(resultado) > 0:
                prev = resultado[-1].strip() if isinstance(resultado[-1], str) else ''
                if prev.endswith(':'):
                    continue
            resultado.append(linea)
        return resultado

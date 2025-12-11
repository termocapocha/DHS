from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser

class Caminante (compiladorVisitor):
    def __init__(self):
        self.contadorTemporales = 0
        
    def nuevaTemporal(self):
        temp = f"t{self.contadorTemporales}"
        self.contadorTemporales += 1
        return temp

    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        if ctx.instrucciones():
            return self.visit(ctx.instrucciones())
        return None

    # Sobreescribe TODOS los metodos del visitor base para evitar visitChildren
    def visitInstrucciones(self, ctx): 
        
        # Procesar recursivamente todas las instrucciones 
        if hasattr(ctx, 'instruccion') and ctx.instruccion():
            self.visit(ctx.instruccion())
        if hasattr(ctx, 'instrucciones') and ctx.instrucciones():
            self.visit(ctx.instrucciones())
        return None
        
    def visitInstruccion(self, ctx):
        # Usar visitChildren pero controlado
        return self.visitChildren(ctx)

    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        if ctx.ID() and ctx.opal():
            variable = ctx.ID().getText()
            temporal = self.visit(ctx.opal())
            print(f"{variable} = {temporal}")
        return None
        
    def visitOpal(self, ctx:compiladorParser.OpalContext):
        return self.visit(ctx.exp())
        
    def visitExp(self, ctx:compiladorParser.ExpContext):
        izq = self.visit(ctx.term())
        if ctx.e() and ctx.e().getChildCount() > 0:
            return self.visitE(ctx.e(), izq)
        return izq
        
    def visitE(self, ctx, izq):
        if ctx.getChildCount() == 0:
            return izq
        if ctx.getChildCount() >= 2:
            operador = ctx.getChild(0).getText()
            der = self.visit(ctx.getChild(1))
            temporal = self.nuevaTemporal()
            print(f"{temporal} = {izq} {operador} {der}")
            if ctx.getChildCount() > 2:
                return self.visitE(ctx.getChild(2), temporal)
            return temporal
        return izq
        
    def visitTerm(self, ctx:compiladorParser.TermContext):
        izq = self.visit(ctx.factor())
        if ctx.t() and ctx.t().getChildCount() > 0:
            return self.visitT(ctx.t(), izq)
        return izq
        
    def visitT(self, ctx, izq):
        if ctx.getChildCount() == 0:
            return izq
        if ctx.getChildCount() >= 2:
            operador = ctx.getChild(0).getText()
            der = self.visit(ctx.getChild(1))
            temporal = self.nuevaTemporal()
            print(f"{temporal} = {izq} {operador} {der}")
            if ctx.getChildCount() > 2:
                return self.visitT(ctx.getChild(2), temporal)
            return temporal
        return izq
        
    def visitFactor(self, ctx:compiladorParser.FactorContext):
        if ctx.ID():
            return ctx.ID().getText()
        elif ctx.NUMERO():
            return ctx.NUMERO().getText()
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.llamada():
            return self.visit(ctx.llamada())
        return None

    def visitIwhile(self, ctx:compiladorParser.IwhileContext):
        print("Entro a while")
        return None
        
    def visitFuncion(self, ctx):
        # Solo procesa returns en funciones
        if ctx.children:
            for child in ctx.children:
                if hasattr(child, 'getRuleIndex'):
                    ruleIndex = child.getRuleIndex()
                    if ruleIndex == compiladorParser.RULE_bloque:
                        self.visit(child)
        return None
        
    def visitBloque(self, ctx):
        if ctx.children:
            for child in ctx.children:
                if hasattr(child, 'getRuleIndex'):
                    ruleIndex = child.getRuleIndex()
                    if ruleIndex == compiladorParser.RULE_instrucciones:
                        self.visit(child)
        return None
        
    def visitIreturn(self, ctx:compiladorParser.IreturnContext):
        if ctx.opal():
            temporal = self.visit(ctx.opal())
            print(f"return {temporal}")
        return None
        
    def visitDeclaracion(self, ctx):
        return None
        
    def visitProto(self, ctx):
        return None
        
    def visitListavar(self, ctx):
        return None
        
    def visitArgumento(self, ctx):
        return None
        
    def visitListaParametros(self, ctx):
        return None
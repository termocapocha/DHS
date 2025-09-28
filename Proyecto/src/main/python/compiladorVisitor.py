# Generated from c:/Users/Usuario/Desktop/DHS/Proyecto/src/main/python/compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete generic visitor for a parse tree produced by compiladorParser.

class compiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladorParser#programa.
    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instruccion.
    def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#bloque.
    def visitBloque(self, ctx:compiladorParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iwhile.
    def visitIwhile(self, ctx:compiladorParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iif.
    def visitIif(self, ctx:compiladorParser.IifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ielse.
    def visitIelse(self, ctx:compiladorParser.IelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ifor.
    def visitIfor(self, ctx:compiladorParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracion.
    def visitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listavar.
    def visitListavar(self, ctx:compiladorParser.ListavarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#inic.
    def visitInic(self, ctx:compiladorParser.InicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#tipo.
    def visitTipo(self, ctx:compiladorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#inicializacion.
    def visitInicializacion(self, ctx:compiladorParser.InicializacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iincdec.
    def visitIincdec(self, ctx:compiladorParser.IincdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#comparator.
    def visitComparator(self, ctx:compiladorParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacion.
    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#funcion.
    def visitFuncion(self, ctx:compiladorParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#proto.
    def visitProto(self, ctx:compiladorParser.ProtoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ireturn.
    def visitIreturn(self, ctx:compiladorParser.IreturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#opal.
    def visitOpal(self, ctx:compiladorParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp.
    def visitExp(self, ctx:compiladorParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#e.
    def visitE(self, ctx:compiladorParser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#term.
    def visitTerm(self, ctx:compiladorParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#t.
    def visitT(self, ctx:compiladorParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#factor.
    def visitFactor(self, ctx:compiladorParser.FactorContext):
        return self.visitChildren(ctx)



del compiladorParser
# Generated from compilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete listener for a parse tree produced by compiladorParser.
class compiladorListener(ParseTreeListener):

    # Enter a parse tree produced by compiladorParser#programa.
    def enterPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladorParser#programa.
    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladorParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladorParser#instruccion.
    def enterInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladorParser#instruccion.
    def exitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladorParser#bloque.
    def enterBloque(self, ctx:compiladorParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladorParser#bloque.
    def exitBloque(self, ctx:compiladorParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladorParser#iwhile.
    def enterIwhile(self, ctx:compiladorParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladorParser#iwhile.
    def exitIwhile(self, ctx:compiladorParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladorParser#iif.
    def enterIif(self, ctx:compiladorParser.IifContext):
        pass

    # Exit a parse tree produced by compiladorParser#iif.
    def exitIif(self, ctx:compiladorParser.IifContext):
        pass


    # Enter a parse tree produced by compiladorParser#condicion.
    def enterCondicion(self, ctx:compiladorParser.CondicionContext):
        pass

    # Exit a parse tree produced by compiladorParser#condicion.
    def exitCondicion(self, ctx:compiladorParser.CondicionContext):
        pass


    # Enter a parse tree produced by compiladorParser#orExp.
    def enterOrExp(self, ctx:compiladorParser.OrExpContext):
        pass

    # Exit a parse tree produced by compiladorParser#orExp.
    def exitOrExp(self, ctx:compiladorParser.OrExpContext):
        pass


    # Enter a parse tree produced by compiladorParser#orExpRest.
    def enterOrExpRest(self, ctx:compiladorParser.OrExpRestContext):
        pass

    # Exit a parse tree produced by compiladorParser#orExpRest.
    def exitOrExpRest(self, ctx:compiladorParser.OrExpRestContext):
        pass


    # Enter a parse tree produced by compiladorParser#andExp.
    def enterAndExp(self, ctx:compiladorParser.AndExpContext):
        pass

    # Exit a parse tree produced by compiladorParser#andExp.
    def exitAndExp(self, ctx:compiladorParser.AndExpContext):
        pass


    # Enter a parse tree produced by compiladorParser#andExpRest.
    def enterAndExpRest(self, ctx:compiladorParser.AndExpRestContext):
        pass

    # Exit a parse tree produced by compiladorParser#andExpRest.
    def exitAndExpRest(self, ctx:compiladorParser.AndExpRestContext):
        pass


    # Enter a parse tree produced by compiladorParser#comparacion.
    def enterComparacion(self, ctx:compiladorParser.ComparacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#comparacion.
    def exitComparacion(self, ctx:compiladorParser.ComparacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#comparacionRest.
    def enterComparacionRest(self, ctx:compiladorParser.ComparacionRestContext):
        pass

    # Exit a parse tree produced by compiladorParser#comparacionRest.
    def exitComparacionRest(self, ctx:compiladorParser.ComparacionRestContext):
        pass


    # Enter a parse tree produced by compiladorParser#termino.
    def enterTermino(self, ctx:compiladorParser.TerminoContext):
        pass

    # Exit a parse tree produced by compiladorParser#termino.
    def exitTermino(self, ctx:compiladorParser.TerminoContext):
        pass


    # Enter a parse tree produced by compiladorParser#ielse.
    def enterIelse(self, ctx:compiladorParser.IelseContext):
        pass

    # Exit a parse tree produced by compiladorParser#ielse.
    def exitIelse(self, ctx:compiladorParser.IelseContext):
        pass


    # Enter a parse tree produced by compiladorParser#ifor.
    def enterIfor(self, ctx:compiladorParser.IforContext):
        pass

    # Exit a parse tree produced by compiladorParser#ifor.
    def exitIfor(self, ctx:compiladorParser.IforContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion.
    def enterDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion.
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladorParser#listavar.
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        pass

    # Exit a parse tree produced by compiladorParser#listavar.
    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        pass


    # Enter a parse tree produced by compiladorParser#inic.
    def enterInic(self, ctx:compiladorParser.InicContext):
        pass

    # Exit a parse tree produced by compiladorParser#inic.
    def exitInic(self, ctx:compiladorParser.InicContext):
        pass


    # Enter a parse tree produced by compiladorParser#tipo.
    def enterTipo(self, ctx:compiladorParser.TipoContext):
        pass

    # Exit a parse tree produced by compiladorParser#tipo.
    def exitTipo(self, ctx:compiladorParser.TipoContext):
        pass


    # Enter a parse tree produced by compiladorParser#iincdec.
    def enterIincdec(self, ctx:compiladorParser.IincdecContext):
        pass

    # Exit a parse tree produced by compiladorParser#iincdec.
    def exitIincdec(self, ctx:compiladorParser.IincdecContext):
        pass


    # Enter a parse tree produced by compiladorParser#asignacion.
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignacion.
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#funcion.
    def enterFuncion(self, ctx:compiladorParser.FuncionContext):
        pass

    # Exit a parse tree produced by compiladorParser#funcion.
    def exitFuncion(self, ctx:compiladorParser.FuncionContext):
        pass


    # Enter a parse tree produced by compiladorParser#proto.
    def enterProto(self, ctx:compiladorParser.ProtoContext):
        pass

    # Exit a parse tree produced by compiladorParser#proto.
    def exitProto(self, ctx:compiladorParser.ProtoContext):
        pass


    # Enter a parse tree produced by compiladorParser#llamada.
    def enterLlamada(self, ctx:compiladorParser.LlamadaContext):
        pass

    # Exit a parse tree produced by compiladorParser#llamada.
    def exitLlamada(self, ctx:compiladorParser.LlamadaContext):
        pass


    # Enter a parse tree produced by compiladorParser#argumento.
    def enterArgumento(self, ctx:compiladorParser.ArgumentoContext):
        pass

    # Exit a parse tree produced by compiladorParser#argumento.
    def exitArgumento(self, ctx:compiladorParser.ArgumentoContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaParametros.
    def enterListaParametros(self, ctx:compiladorParser.ListaParametrosContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaParametros.
    def exitListaParametros(self, ctx:compiladorParser.ListaParametrosContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaArgumentos.
    def enterListaArgumentos(self, ctx:compiladorParser.ListaArgumentosContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaArgumentos.
    def exitListaArgumentos(self, ctx:compiladorParser.ListaArgumentosContext):
        pass


    # Enter a parse tree produced by compiladorParser#argumentosLlamada.
    def enterArgumentosLlamada(self, ctx:compiladorParser.ArgumentosLlamadaContext):
        pass

    # Exit a parse tree produced by compiladorParser#argumentosLlamada.
    def exitArgumentosLlamada(self, ctx:compiladorParser.ArgumentosLlamadaContext):
        pass


    # Enter a parse tree produced by compiladorParser#ireturn.
    def enterIreturn(self, ctx:compiladorParser.IreturnContext):
        pass

    # Exit a parse tree produced by compiladorParser#ireturn.
    def exitIreturn(self, ctx:compiladorParser.IreturnContext):
        pass


    # Enter a parse tree produced by compiladorParser#opal.
    def enterOpal(self, ctx:compiladorParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladorParser#opal.
    def exitOpal(self, ctx:compiladorParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp.
    def enterExp(self, ctx:compiladorParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp.
    def exitExp(self, ctx:compiladorParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladorParser#e.
    def enterE(self, ctx:compiladorParser.EContext):
        pass

    # Exit a parse tree produced by compiladorParser#e.
    def exitE(self, ctx:compiladorParser.EContext):
        pass


    # Enter a parse tree produced by compiladorParser#term.
    def enterTerm(self, ctx:compiladorParser.TermContext):
        pass

    # Exit a parse tree produced by compiladorParser#term.
    def exitTerm(self, ctx:compiladorParser.TermContext):
        pass


    # Enter a parse tree produced by compiladorParser#t.
    def enterT(self, ctx:compiladorParser.TContext):
        pass

    # Exit a parse tree produced by compiladorParser#t.
    def exitT(self, ctx:compiladorParser.TContext):
        pass


    # Enter a parse tree produced by compiladorParser#factor.
    def enterFactor(self, ctx:compiladorParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladorParser#factor.
    def exitFactor(self, ctx:compiladorParser.FactorContext):
        pass



del compiladorParser
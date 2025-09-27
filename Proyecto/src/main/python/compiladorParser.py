# Generated from c:/Users/Usuario/Desktop/DHS/Proyecto/src/main/python/compilador.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,221,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,67,8,2,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,3,4,78,8,4,1,4,1,4,1,4,3,4,83,8,4,1,5,1,
        5,1,5,1,5,1,5,3,5,90,8,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,99,8,6,
        1,7,1,7,1,7,1,7,3,7,105,8,7,1,7,1,7,1,7,3,7,110,8,7,1,7,1,7,1,7,
        3,7,115,8,7,1,7,1,7,1,7,3,7,120,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,133,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,141,8,9,
        1,10,1,10,1,10,3,10,146,8,10,1,11,1,11,1,12,1,12,1,12,3,12,153,8,
        12,1,13,1,13,1,13,1,13,3,13,159,8,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,173,8,14,1,15,1,15,1,15,1,
        15,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,3,18,193,8,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,211,8,20,1,21,1,21,1,
        21,1,21,1,21,1,21,3,21,219,8,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,0,1,1,0,17,18,231,0,44,1,
        0,0,0,2,51,1,0,0,0,4,66,1,0,0,0,6,68,1,0,0,0,8,72,1,0,0,0,10,84,
        1,0,0,0,12,98,1,0,0,0,14,100,1,0,0,0,16,132,1,0,0,0,18,140,1,0,0,
        0,20,145,1,0,0,0,22,147,1,0,0,0,24,152,1,0,0,0,26,158,1,0,0,0,28,
        172,1,0,0,0,30,174,1,0,0,0,32,178,1,0,0,0,34,180,1,0,0,0,36,192,
        1,0,0,0,38,194,1,0,0,0,40,210,1,0,0,0,42,218,1,0,0,0,44,45,3,2,1,
        0,45,46,5,0,0,1,46,1,1,0,0,0,47,48,3,4,2,0,48,49,3,2,1,0,49,52,1,
        0,0,0,50,52,1,0,0,0,51,47,1,0,0,0,51,50,1,0,0,0,52,3,1,0,0,0,53,
        54,3,30,15,0,54,55,5,5,0,0,55,67,1,0,0,0,56,57,3,16,8,0,57,58,5,
        5,0,0,58,67,1,0,0,0,59,60,3,26,13,0,60,61,5,5,0,0,61,67,1,0,0,0,
        62,67,3,14,7,0,63,67,3,10,5,0,64,67,3,8,4,0,65,67,3,6,3,0,66,53,
        1,0,0,0,66,56,1,0,0,0,66,59,1,0,0,0,66,62,1,0,0,0,66,63,1,0,0,0,
        66,64,1,0,0,0,66,65,1,0,0,0,67,5,1,0,0,0,68,69,5,3,0,0,69,70,3,2,
        1,0,70,71,5,4,0,0,71,7,1,0,0,0,72,73,5,22,0,0,73,77,5,1,0,0,74,78,
        3,32,16,0,75,78,3,28,14,0,76,78,5,15,0,0,77,74,1,0,0,0,77,75,1,0,
        0,0,77,76,1,0,0,0,78,79,1,0,0,0,79,82,5,2,0,0,80,83,3,4,2,0,81,83,
        3,6,3,0,82,80,1,0,0,0,82,81,1,0,0,0,83,9,1,0,0,0,84,85,5,19,0,0,
        85,89,5,1,0,0,86,90,3,32,16,0,87,90,3,28,14,0,88,90,5,15,0,0,89,
        86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,92,5,2,0,
        0,92,93,3,4,2,0,93,94,3,12,6,0,94,11,1,0,0,0,95,96,5,20,0,0,96,99,
        3,4,2,0,97,99,1,0,0,0,98,95,1,0,0,0,98,97,1,0,0,0,99,13,1,0,0,0,
        100,101,5,21,0,0,101,104,5,1,0,0,102,105,3,24,12,0,103,105,1,0,0,
        0,104,102,1,0,0,0,104,103,1,0,0,0,105,106,1,0,0,0,106,109,5,5,0,
        0,107,110,3,28,14,0,108,110,1,0,0,0,109,107,1,0,0,0,109,108,1,0,
        0,0,110,111,1,0,0,0,111,114,5,5,0,0,112,115,3,26,13,0,113,115,1,
        0,0,0,114,112,1,0,0,0,114,113,1,0,0,0,115,116,1,0,0,0,116,119,5,
        2,0,0,117,120,3,6,3,0,118,120,3,4,2,0,119,117,1,0,0,0,119,118,1,
        0,0,0,120,15,1,0,0,0,121,122,3,22,11,0,122,123,5,23,0,0,123,124,
        3,20,10,0,124,125,3,18,9,0,125,133,1,0,0,0,126,127,3,22,11,0,127,
        128,5,23,0,0,128,129,3,20,10,0,129,130,3,18,9,0,130,131,5,5,0,0,
        131,133,1,0,0,0,132,121,1,0,0,0,132,126,1,0,0,0,133,17,1,0,0,0,134,
        135,5,7,0,0,135,136,5,23,0,0,136,137,3,20,10,0,137,138,3,18,9,0,
        138,141,1,0,0,0,139,141,1,0,0,0,140,134,1,0,0,0,140,139,1,0,0,0,
        141,19,1,0,0,0,142,143,5,6,0,0,143,146,3,32,16,0,144,146,1,0,0,0,
        145,142,1,0,0,0,145,144,1,0,0,0,146,21,1,0,0,0,147,148,7,0,0,0,148,
        23,1,0,0,0,149,153,5,23,0,0,150,153,3,30,15,0,151,153,3,16,8,0,152,
        149,1,0,0,0,152,150,1,0,0,0,152,151,1,0,0,0,153,25,1,0,0,0,154,155,
        5,23,0,0,155,159,5,13,0,0,156,157,5,13,0,0,157,159,5,23,0,0,158,
        154,1,0,0,0,158,156,1,0,0,0,159,27,1,0,0,0,160,161,5,23,0,0,161,
        162,5,14,0,0,162,173,5,23,0,0,163,164,5,23,0,0,164,165,5,14,0,0,
        165,173,5,16,0,0,166,167,5,16,0,0,167,168,5,14,0,0,168,173,5,23,
        0,0,169,170,5,16,0,0,170,171,5,14,0,0,171,173,5,16,0,0,172,160,1,
        0,0,0,172,163,1,0,0,0,172,166,1,0,0,0,172,169,1,0,0,0,173,29,1,0,
        0,0,174,175,5,23,0,0,175,176,5,6,0,0,176,177,3,32,16,0,177,31,1,
        0,0,0,178,179,3,34,17,0,179,33,1,0,0,0,180,181,3,38,19,0,181,182,
        3,36,18,0,182,35,1,0,0,0,183,184,5,8,0,0,184,185,3,38,19,0,185,186,
        3,36,18,0,186,193,1,0,0,0,187,188,5,9,0,0,188,189,3,38,19,0,189,
        190,3,36,18,0,190,193,1,0,0,0,191,193,1,0,0,0,192,183,1,0,0,0,192,
        187,1,0,0,0,192,191,1,0,0,0,193,37,1,0,0,0,194,195,3,42,21,0,195,
        196,3,40,20,0,196,39,1,0,0,0,197,198,5,10,0,0,198,199,3,42,21,0,
        199,200,3,40,20,0,200,211,1,0,0,0,201,202,5,11,0,0,202,203,3,42,
        21,0,203,204,3,40,20,0,204,211,1,0,0,0,205,206,5,12,0,0,206,207,
        3,42,21,0,207,208,3,40,20,0,208,211,1,0,0,0,209,211,1,0,0,0,210,
        197,1,0,0,0,210,201,1,0,0,0,210,205,1,0,0,0,210,209,1,0,0,0,211,
        41,1,0,0,0,212,219,5,16,0,0,213,219,5,23,0,0,214,215,5,1,0,0,215,
        216,3,34,17,0,216,217,5,2,0,0,217,219,1,0,0,0,218,212,1,0,0,0,218,
        213,1,0,0,0,218,214,1,0,0,0,219,43,1,0,0,0,19,51,66,77,82,89,98,
        104,109,114,119,132,140,145,152,158,172,192,210,218
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "','", "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'double'", 
                     "'if'", "'else'", "'for'", "'while'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "ASIG", 
                      "COMA", "SUMA", "RESTA", "MULT", "DIV", "MOD", "INCDEC", 
                      "COMP", "LIT", "NUMERO", "INT", "DOUBLE", "IF", "ELSE", 
                      "FOR", "WHILE", "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_bloque = 3
    RULE_iwhile = 4
    RULE_iif = 5
    RULE_ielse = 6
    RULE_ifor = 7
    RULE_declaracion = 8
    RULE_listavar = 9
    RULE_inic = 10
    RULE_tipo = 11
    RULE_inicializacion = 12
    RULE_iincdec = 13
    RULE_comparator = 14
    RULE_asignacion = 15
    RULE_opal = 16
    RULE_exp = 17
    RULE_e = 18
    RULE_term = 19
    RULE_t = 20
    RULE_factor = 21

    ruleNames =  [ "programa", "instrucciones", "instruccion", "bloque", 
                   "iwhile", "iif", "ielse", "ifor", "declaracion", "listavar", 
                   "inic", "tipo", "inicializacion", "iincdec", "comparator", 
                   "asignacion", "opal", "exp", "e", "term", "t", "factor" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    ASIG=6
    COMA=7
    SUMA=8
    RESTA=9
    MULT=10
    DIV=11
    MOD=12
    INCDEC=13
    COMP=14
    LIT=15
    NUMERO=16
    INT=17
    DOUBLE=18
    IF=19
    ELSE=20
    FOR=21
    WHILE=22
    ID=23
    WS=24
    OTRO=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladorParser.EOF, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.instrucciones()
            self.state = 45
            self.match(compiladorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladorParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 13, 17, 18, 19, 21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.instruccion()
                self.state = 48
                self.instrucciones()
                pass
            elif token in [-1, 4]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def declaracion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionContext,0)


        def iincdec(self):
            return self.getTypedRuleContext(compiladorParser.IincdecContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladorParser.IforContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladorParser.IifContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladorParser.IwhileContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladorParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.asignacion()
                self.state = 54
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.declaracion()
                self.state = 57
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.iincdec()
                self.state = 60
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.ifor()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.iif()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                self.iwhile()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 65
                self.bloque()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladorParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladorParser.LLC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladorParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(compiladorParser.LLA)
            self.state = 69
            self.instrucciones()
            self.state = 70
            self.match(compiladorParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladorParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def comparator(self):
            return self.getTypedRuleContext(compiladorParser.ComparatorContext,0)


        def LIT(self):
            return self.getToken(compiladorParser.LIT, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compiladorParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(compiladorParser.WHILE)
            self.state = 73
            self.match(compiladorParser.PA)
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 74
                self.opal()
                pass

            elif la_ == 2:
                self.state = 75
                self.comparator()
                pass

            elif la_ == 3:
                self.state = 76
                self.match(compiladorParser.LIT)
                pass


            self.state = 79
            self.match(compiladorParser.PC)
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 80
                self.instruccion()
                pass

            elif la_ == 2:
                self.state = 81
                self.bloque()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladorParser.IF, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def ielse(self):
            return self.getTypedRuleContext(compiladorParser.IelseContext,0)


        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def comparator(self):
            return self.getTypedRuleContext(compiladorParser.ComparatorContext,0)


        def LIT(self):
            return self.getToken(compiladorParser.LIT, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compiladorParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(compiladorParser.IF)
            self.state = 85
            self.match(compiladorParser.PA)
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 86
                self.opal()
                pass

            elif la_ == 2:
                self.state = 87
                self.comparator()
                pass

            elif la_ == 3:
                self.state = 88
                self.match(compiladorParser.LIT)
                pass


            self.state = 91
            self.match(compiladorParser.PC)
            self.state = 92
            self.instruccion()
            self.state = 93
            self.ielse()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladorParser.ELSE, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_ielse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIelse" ):
                listener.enterIelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIelse" ):
                listener.exitIelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIelse" ):
                return visitor.visitIelse(self)
            else:
                return visitor.visitChildren(self)




    def ielse(self):

        localctx = compiladorParser.IelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ielse)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(compiladorParser.ELSE)
                self.state = 96
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladorParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.PYC)
            else:
                return self.getToken(compiladorParser.PYC, i)

        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def inicializacion(self):
            return self.getTypedRuleContext(compiladorParser.InicializacionContext,0)


        def comparator(self):
            return self.getTypedRuleContext(compiladorParser.ComparatorContext,0)


        def iincdec(self):
            return self.getTypedRuleContext(compiladorParser.IincdecContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compiladorParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(compiladorParser.FOR)
            self.state = 101
            self.match(compiladorParser.PA)
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 23]:
                self.state = 102
                self.inicializacion()
                pass
            elif token in [5]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 106
            self.match(compiladorParser.PYC)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 23]:
                self.state = 107
                self.comparator()
                pass
            elif token in [5]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 111
            self.match(compiladorParser.PYC)
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 23]:
                self.state = 112
                self.iincdec()
                pass
            elif token in [2]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 116
            self.match(compiladorParser.PC)
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 117
                self.bloque()
                pass

            elif la_ == 2:
                self.state = 118
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladorParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaracion)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.tipo()
                self.state = 122
                self.match(compiladorParser.ID)
                self.state = 123
                self.inic()
                self.state = 124
                self.listavar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.tipo()
                self.state = 127
                self.match(compiladorParser.ID)
                self.state = 128
                self.inic()
                self.state = 129
                self.listavar()
                self.state = 130
                self.match(compiladorParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListavarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listavar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListavar" ):
                listener.enterListavar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListavar" ):
                listener.exitListavar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListavar" ):
                return visitor.visitListavar(self)
            else:
                return visitor.visitChildren(self)




    def listavar(self):

        localctx = compiladorParser.ListavarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listavar)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(compiladorParser.COMA)
                self.state = 135
                self.match(compiladorParser.ID)
                self.state = 136
                self.inic()
                self.state = 137
                self.listavar()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_inic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInic" ):
                listener.enterInic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInic" ):
                listener.exitInic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInic" ):
                return visitor.visitInic(self)
            else:
                return visitor.visitChildren(self)




    def inic(self):

        localctx = compiladorParser.InicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_inic)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(compiladorParser.ASIG)
                self.state = 143
                self.opal()
                pass
            elif token in [5, 7]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladorParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladorParser.DOUBLE, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = compiladorParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_inicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializacion" ):
                listener.enterInicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializacion" ):
                listener.exitInicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacion" ):
                return visitor.visitInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def inicializacion(self):

        localctx = compiladorParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inicializacion)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(compiladorParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.declaracion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IincdecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def INCDEC(self):
            return self.getToken(compiladorParser.INCDEC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_iincdec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIincdec" ):
                listener.enterIincdec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIincdec" ):
                listener.exitIincdec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIincdec" ):
                return visitor.visitIincdec(self)
            else:
                return visitor.visitChildren(self)




    def iincdec(self):

        localctx = compiladorParser.IincdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iincdec)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(compiladorParser.ID)
                self.state = 155
                self.match(compiladorParser.INCDEC)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(compiladorParser.INCDEC)
                self.state = 157
                self.match(compiladorParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.ID)
            else:
                return self.getToken(compiladorParser.ID, i)

        def COMP(self):
            return self.getToken(compiladorParser.COMP, 0)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.NUMERO)
            else:
                return self.getToken(compiladorParser.NUMERO, i)

        def getRuleIndex(self):
            return compiladorParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = compiladorParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comparator)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(compiladorParser.ID)
                self.state = 161
                self.match(compiladorParser.COMP)
                self.state = 162
                self.match(compiladorParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(compiladorParser.ID)
                self.state = 164
                self.match(compiladorParser.COMP)
                self.state = 165
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.match(compiladorParser.NUMERO)
                self.state = 167
                self.match(compiladorParser.COMP)
                self.state = 168
                self.match(compiladorParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                self.match(compiladorParser.NUMERO)
                self.state = 170
                self.match(compiladorParser.COMP)
                self.state = 171
                self.match(compiladorParser.NUMERO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladorParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(compiladorParser.ID)
            self.state = 175
            self.match(compiladorParser.ASIG)
            self.state = 176
            self.opal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladorParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladorParser.EContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladorParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.term()
            self.state = 181
            self.e()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladorParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladorParser.EContext,0)


        def RESTA(self):
            return self.getToken(compiladorParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = compiladorParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_e)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(compiladorParser.SUMA)
                self.state = 184
                self.term()
                self.state = 185
                self.e()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(compiladorParser.RESTA)
                self.state = 188
                self.term()
                self.state = 189
                self.e()
                pass
            elif token in [2, 5, 7]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladorParser.TContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.factor()
            self.state = 195
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladorParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladorParser.TContext,0)


        def DIV(self):
            return self.getToken(compiladorParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladorParser.MOD, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladorParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_t)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(compiladorParser.MULT)
                self.state = 198
                self.factor()
                self.state = 199
                self.t()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(compiladorParser.DIV)
                self.state = 202
                self.factor()
                self.state = 203
                self.t()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.match(compiladorParser.MOD)
                self.state = 206
                self.factor()
                self.state = 207
                self.t()
                pass
            elif token in [2, 5, 7, 8, 9]:
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladorParser.NUMERO, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factor)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(compiladorParser.NUMERO)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(compiladorParser.ID)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.match(compiladorParser.PA)
                self.state = 215
                self.exp()
                self.state = 216
                self.match(compiladorParser.PC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






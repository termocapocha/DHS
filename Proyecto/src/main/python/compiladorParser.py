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
        4,1,24,243,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,64,8,2,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,86,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,142,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,3,8,155,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,163,8,
        9,1,10,1,10,1,10,3,10,168,8,10,1,11,1,11,1,12,1,12,1,12,1,12,3,12,
        176,8,12,1,13,1,13,1,13,1,13,1,13,3,13,183,8,13,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,195,8,14,1,15,1,15,1,15,1,
        15,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,3,18,215,8,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,233,8,20,1,21,1,21,1,
        21,1,21,1,21,1,21,3,21,241,8,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,0,1,1,0,16,17,251,0,44,1,
        0,0,0,2,51,1,0,0,0,4,63,1,0,0,0,6,65,1,0,0,0,8,69,1,0,0,0,10,75,
        1,0,0,0,12,85,1,0,0,0,14,141,1,0,0,0,16,154,1,0,0,0,18,162,1,0,0,
        0,20,167,1,0,0,0,22,169,1,0,0,0,24,175,1,0,0,0,26,182,1,0,0,0,28,
        194,1,0,0,0,30,196,1,0,0,0,32,200,1,0,0,0,34,202,1,0,0,0,36,214,
        1,0,0,0,38,216,1,0,0,0,40,232,1,0,0,0,42,240,1,0,0,0,44,45,3,2,1,
        0,45,46,5,0,0,1,46,1,1,0,0,0,47,48,3,4,2,0,48,49,3,2,1,0,49,52,1,
        0,0,0,50,52,1,0,0,0,51,47,1,0,0,0,51,50,1,0,0,0,52,3,1,0,0,0,53,
        54,3,30,15,0,54,55,5,5,0,0,55,64,1,0,0,0,56,57,3,16,8,0,57,58,5,
        5,0,0,58,64,1,0,0,0,59,64,3,14,7,0,60,64,3,10,5,0,61,64,3,8,4,0,
        62,64,3,6,3,0,63,53,1,0,0,0,63,56,1,0,0,0,63,59,1,0,0,0,63,60,1,
        0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,64,5,1,0,0,0,65,66,5,3,0,0,66,
        67,3,2,1,0,67,68,5,4,0,0,68,7,1,0,0,0,69,70,5,21,0,0,70,71,5,1,0,
        0,71,72,3,32,16,0,72,73,5,2,0,0,73,74,3,4,2,0,74,9,1,0,0,0,75,76,
        5,18,0,0,76,77,5,1,0,0,77,78,3,32,16,0,78,79,5,2,0,0,79,80,3,4,2,
        0,80,81,3,12,6,0,81,11,1,0,0,0,82,83,5,19,0,0,83,86,3,4,2,0,84,86,
        1,0,0,0,85,82,1,0,0,0,85,84,1,0,0,0,86,13,1,0,0,0,87,88,5,20,0,0,
        88,89,5,1,0,0,89,90,5,5,0,0,90,91,5,5,0,0,91,92,5,2,0,0,92,142,3,
        6,3,0,93,94,5,20,0,0,94,95,5,1,0,0,95,96,5,22,0,0,96,97,5,5,0,0,
        97,98,5,5,0,0,98,99,5,2,0,0,99,142,3,6,3,0,100,101,5,20,0,0,101,
        102,5,1,0,0,102,103,3,30,15,0,103,104,5,5,0,0,104,105,5,5,0,0,105,
        106,5,2,0,0,106,107,3,6,3,0,107,142,1,0,0,0,108,109,5,20,0,0,109,
        110,5,1,0,0,110,111,3,16,8,0,111,112,5,5,0,0,112,113,5,5,0,0,113,
        114,5,2,0,0,114,115,3,6,3,0,115,142,1,0,0,0,116,117,5,20,0,0,117,
        118,5,1,0,0,118,119,5,5,0,0,119,120,3,28,14,0,120,121,5,5,0,0,121,
        122,5,2,0,0,122,123,3,6,3,0,123,142,1,0,0,0,124,125,5,20,0,0,125,
        126,5,1,0,0,126,127,5,5,0,0,127,128,5,5,0,0,128,129,3,26,13,0,129,
        130,5,2,0,0,130,131,3,6,3,0,131,142,1,0,0,0,132,133,5,20,0,0,133,
        134,5,1,0,0,134,135,5,5,0,0,135,136,3,28,14,0,136,137,5,5,0,0,137,
        138,3,26,13,0,138,139,5,2,0,0,139,140,3,6,3,0,140,142,1,0,0,0,141,
        87,1,0,0,0,141,93,1,0,0,0,141,100,1,0,0,0,141,108,1,0,0,0,141,116,
        1,0,0,0,141,124,1,0,0,0,141,132,1,0,0,0,142,15,1,0,0,0,143,144,3,
        22,11,0,144,145,5,22,0,0,145,146,3,20,10,0,146,147,3,18,9,0,147,
        155,1,0,0,0,148,149,3,22,11,0,149,150,5,22,0,0,150,151,3,20,10,0,
        151,152,3,18,9,0,152,153,5,5,0,0,153,155,1,0,0,0,154,143,1,0,0,0,
        154,148,1,0,0,0,155,17,1,0,0,0,156,157,5,7,0,0,157,158,5,22,0,0,
        158,159,3,20,10,0,159,160,3,18,9,0,160,163,1,0,0,0,161,163,1,0,0,
        0,162,156,1,0,0,0,162,161,1,0,0,0,163,19,1,0,0,0,164,165,5,6,0,0,
        165,168,3,32,16,0,166,168,1,0,0,0,167,164,1,0,0,0,167,166,1,0,0,
        0,168,21,1,0,0,0,169,170,7,0,0,0,170,23,1,0,0,0,171,176,5,22,0,0,
        172,176,3,30,15,0,173,176,3,16,8,0,174,176,1,0,0,0,175,171,1,0,0,
        0,175,172,1,0,0,0,175,173,1,0,0,0,175,174,1,0,0,0,176,25,1,0,0,0,
        177,178,5,22,0,0,178,183,5,13,0,0,179,180,5,13,0,0,180,183,5,22,
        0,0,181,183,1,0,0,0,182,177,1,0,0,0,182,179,1,0,0,0,182,181,1,0,
        0,0,183,27,1,0,0,0,184,185,5,22,0,0,185,186,5,14,0,0,186,195,5,22,
        0,0,187,188,5,22,0,0,188,189,5,14,0,0,189,195,5,15,0,0,190,191,5,
        15,0,0,191,192,5,14,0,0,192,195,5,22,0,0,193,195,1,0,0,0,194,184,
        1,0,0,0,194,187,1,0,0,0,194,190,1,0,0,0,194,193,1,0,0,0,195,29,1,
        0,0,0,196,197,5,22,0,0,197,198,5,6,0,0,198,199,3,32,16,0,199,31,
        1,0,0,0,200,201,3,34,17,0,201,33,1,0,0,0,202,203,3,38,19,0,203,204,
        3,36,18,0,204,35,1,0,0,0,205,206,5,8,0,0,206,207,3,38,19,0,207,208,
        3,36,18,0,208,215,1,0,0,0,209,210,5,9,0,0,210,211,3,38,19,0,211,
        212,3,36,18,0,212,215,1,0,0,0,213,215,1,0,0,0,214,205,1,0,0,0,214,
        209,1,0,0,0,214,213,1,0,0,0,215,37,1,0,0,0,216,217,3,42,21,0,217,
        218,3,40,20,0,218,39,1,0,0,0,219,220,5,10,0,0,220,221,3,42,21,0,
        221,222,3,40,20,0,222,233,1,0,0,0,223,224,5,11,0,0,224,225,3,42,
        21,0,225,226,3,40,20,0,226,233,1,0,0,0,227,228,5,12,0,0,228,229,
        3,42,21,0,229,230,3,40,20,0,230,233,1,0,0,0,231,233,1,0,0,0,232,
        219,1,0,0,0,232,223,1,0,0,0,232,227,1,0,0,0,232,231,1,0,0,0,233,
        41,1,0,0,0,234,241,5,15,0,0,235,241,5,22,0,0,236,237,5,1,0,0,237,
        238,3,34,17,0,238,239,5,2,0,0,239,241,1,0,0,0,240,234,1,0,0,0,240,
        235,1,0,0,0,240,236,1,0,0,0,241,43,1,0,0,0,13,51,63,85,141,154,162,
        167,175,182,194,214,232,240
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "','", "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'int'", "'double'", "'if'", 
                     "'else'", "'for'", "'while'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "ASIG", 
                      "COMA", "SUMA", "RESTA", "MULT", "DIV", "MOD", "INCDEC", 
                      "COMP", "NUMERO", "INT", "DOUBLE", "IF", "ELSE", "FOR", 
                      "WHILE", "ID", "WS", "OTRO" ]

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
    RULE_icomparator = 14
    RULE_asignacion = 15
    RULE_opal = 16
    RULE_exp = 17
    RULE_e = 18
    RULE_term = 19
    RULE_t = 20
    RULE_factor = 21

    ruleNames =  [ "programa", "instrucciones", "instruccion", "bloque", 
                   "iwhile", "iif", "ielse", "ifor", "declaracion", "listavar", 
                   "inic", "tipo", "inicializacion", "iincdec", "icomparator", 
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
    NUMERO=15
    INT=16
    DOUBLE=17
    IF=18
    ELSE=19
    FOR=20
    WHILE=21
    ID=22
    WS=23
    OTRO=24

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
            if token in [3, 16, 17, 18, 20, 21, 22]:
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.asignacion()
                self.state = 54
                self.match(compiladorParser.PYC)
                pass
            elif token in [16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.declaracion()
                self.state = 57
                self.match(compiladorParser.PYC)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.ifor()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.iif()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.iwhile()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 6)
                self.state = 62
                self.bloque()
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
            self.state = 65
            self.match(compiladorParser.LLA)
            self.state = 66
            self.instrucciones()
            self.state = 67
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

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


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
            self.state = 69
            self.match(compiladorParser.WHILE)
            self.state = 70
            self.match(compiladorParser.PA)
            self.state = 71
            self.opal()
            self.state = 72
            self.match(compiladorParser.PC)
            self.state = 73
            self.instruccion()
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

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def ielse(self):
            return self.getTypedRuleContext(compiladorParser.IelseContext,0)


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
            self.state = 75
            self.match(compiladorParser.IF)
            self.state = 76
            self.match(compiladorParser.PA)
            self.state = 77
            self.opal()
            self.state = 78
            self.match(compiladorParser.PC)
            self.state = 79
            self.instruccion()
            self.state = 80
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
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(compiladorParser.ELSE)
                self.state = 83
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

        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionContext,0)


        def icomparator(self):
            return self.getTypedRuleContext(compiladorParser.IcomparatorContext,0)


        def iincdec(self):
            return self.getTypedRuleContext(compiladorParser.IincdecContext,0)


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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(compiladorParser.FOR)
                self.state = 88
                self.match(compiladorParser.PA)
                self.state = 89
                self.match(compiladorParser.PYC)
                self.state = 90
                self.match(compiladorParser.PYC)
                self.state = 91
                self.match(compiladorParser.PC)
                self.state = 92
                self.bloque()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(compiladorParser.FOR)
                self.state = 94
                self.match(compiladorParser.PA)
                self.state = 95
                self.match(compiladorParser.ID)
                self.state = 96
                self.match(compiladorParser.PYC)
                self.state = 97
                self.match(compiladorParser.PYC)
                self.state = 98
                self.match(compiladorParser.PC)
                self.state = 99
                self.bloque()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.match(compiladorParser.FOR)
                self.state = 101
                self.match(compiladorParser.PA)
                self.state = 102
                self.asignacion()
                self.state = 103
                self.match(compiladorParser.PYC)
                self.state = 104
                self.match(compiladorParser.PYC)
                self.state = 105
                self.match(compiladorParser.PC)
                self.state = 106
                self.bloque()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.match(compiladorParser.FOR)
                self.state = 109
                self.match(compiladorParser.PA)
                self.state = 110
                self.declaracion()
                self.state = 111
                self.match(compiladorParser.PYC)
                self.state = 112
                self.match(compiladorParser.PYC)
                self.state = 113
                self.match(compiladorParser.PC)
                self.state = 114
                self.bloque()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 116
                self.match(compiladorParser.FOR)
                self.state = 117
                self.match(compiladorParser.PA)
                self.state = 118
                self.match(compiladorParser.PYC)
                self.state = 119
                self.icomparator()
                self.state = 120
                self.match(compiladorParser.PYC)
                self.state = 121
                self.match(compiladorParser.PC)
                self.state = 122
                self.bloque()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 124
                self.match(compiladorParser.FOR)
                self.state = 125
                self.match(compiladorParser.PA)
                self.state = 126
                self.match(compiladorParser.PYC)
                self.state = 127
                self.match(compiladorParser.PYC)
                self.state = 128
                self.iincdec()
                self.state = 129
                self.match(compiladorParser.PC)
                self.state = 130
                self.bloque()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 132
                self.match(compiladorParser.FOR)
                self.state = 133
                self.match(compiladorParser.PA)
                self.state = 134
                self.match(compiladorParser.PYC)
                self.state = 135
                self.icomparator()
                self.state = 136
                self.match(compiladorParser.PYC)
                self.state = 137
                self.iincdec()
                self.state = 138
                self.match(compiladorParser.PC)
                self.state = 139
                self.bloque()
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
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.tipo()
                self.state = 144
                self.match(compiladorParser.ID)
                self.state = 145
                self.inic()
                self.state = 146
                self.listavar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.tipo()
                self.state = 149
                self.match(compiladorParser.ID)
                self.state = 150
                self.inic()
                self.state = 151
                self.listavar()
                self.state = 152
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
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(compiladorParser.COMA)
                self.state = 157
                self.match(compiladorParser.ID)
                self.state = 158
                self.inic()
                self.state = 159
                self.listavar()
                pass
            elif token in [-1, 5]:
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
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(compiladorParser.ASIG)
                self.state = 165
                self.opal()
                pass
            elif token in [-1, 5, 7]:
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
            self.state = 169
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
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
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(compiladorParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.declaracion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

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
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(compiladorParser.ID)
                self.state = 178
                self.match(compiladorParser.INCDEC)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(compiladorParser.INCDEC)
                self.state = 180
                self.match(compiladorParser.ID)
                pass
            elif token in [2]:
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


    class IcomparatorContext(ParserRuleContext):
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

        def NUMERO(self):
            return self.getToken(compiladorParser.NUMERO, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_icomparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIcomparator" ):
                listener.enterIcomparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIcomparator" ):
                listener.exitIcomparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIcomparator" ):
                return visitor.visitIcomparator(self)
            else:
                return visitor.visitChildren(self)




    def icomparator(self):

        localctx = compiladorParser.IcomparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_icomparator)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(compiladorParser.ID)
                self.state = 185
                self.match(compiladorParser.COMP)
                self.state = 186
                self.match(compiladorParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(compiladorParser.ID)
                self.state = 188
                self.match(compiladorParser.COMP)
                self.state = 189
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(compiladorParser.NUMERO)
                self.state = 191
                self.match(compiladorParser.COMP)
                self.state = 192
                self.match(compiladorParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

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
            self.state = 196
            self.match(compiladorParser.ID)
            self.state = 197
            self.match(compiladorParser.ASIG)
            self.state = 198
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
            self.state = 200
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
            self.state = 202
            self.term()
            self.state = 203
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
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(compiladorParser.SUMA)
                self.state = 206
                self.term()
                self.state = 207
                self.e()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.match(compiladorParser.RESTA)
                self.state = 210
                self.term()
                self.state = 211
                self.e()
                pass
            elif token in [-1, 2, 5, 7]:
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
            self.state = 216
            self.factor()
            self.state = 217
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
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(compiladorParser.MULT)
                self.state = 220
                self.factor()
                self.state = 221
                self.t()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(compiladorParser.DIV)
                self.state = 224
                self.factor()
                self.state = 225
                self.t()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(compiladorParser.MOD)
                self.state = 228
                self.factor()
                self.state = 229
                self.t()
                pass
            elif token in [-1, 2, 5, 7, 8, 9]:
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
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(compiladorParser.NUMERO)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(compiladorParser.ID)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.match(compiladorParser.PA)
                self.state = 237
                self.exp()
                self.state = 238
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






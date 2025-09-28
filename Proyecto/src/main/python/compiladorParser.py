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
        4,1,26,292,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,68,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,91,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,3,4,102,8,4,1,4,1,4,1,4,3,4,107,8,4,1,5,1,5,1,5,1,5,1,5,3,
        5,114,8,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,123,8,6,1,7,1,7,1,7,1,
        7,3,7,129,8,7,1,7,1,7,1,7,3,7,134,8,7,1,7,1,7,1,7,3,7,139,8,7,1,
        7,1,7,1,7,3,7,144,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,157,8,9,1,10,1,10,1,10,3,10,162,8,10,1,11,1,11,1,12,1,12,1,
        12,3,12,169,8,12,1,13,1,13,1,13,1,13,3,13,175,8,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,189,8,14,1,15,
        1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,3,19,219,8,19,1,20,1,20,1,20,1,20,1,20,1,20,3,20,227,8,20,1,
        21,1,21,1,21,1,21,3,21,233,8,21,1,22,1,22,1,22,1,22,1,22,3,22,240,
        8,22,1,23,1,23,1,23,1,23,1,23,3,23,247,8,23,1,24,1,24,1,25,1,25,
        1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,263,8,26,
        1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,3,28,281,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        3,29,290,8,29,1,29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,1,1,0,17,18,305,0,
        60,1,0,0,0,2,67,1,0,0,0,4,90,1,0,0,0,6,92,1,0,0,0,8,96,1,0,0,0,10,
        108,1,0,0,0,12,122,1,0,0,0,14,124,1,0,0,0,16,145,1,0,0,0,18,156,
        1,0,0,0,20,161,1,0,0,0,22,163,1,0,0,0,24,168,1,0,0,0,26,174,1,0,
        0,0,28,188,1,0,0,0,30,190,1,0,0,0,32,194,1,0,0,0,34,201,1,0,0,0,
        36,208,1,0,0,0,38,218,1,0,0,0,40,226,1,0,0,0,42,232,1,0,0,0,44,239,
        1,0,0,0,46,241,1,0,0,0,48,248,1,0,0,0,50,250,1,0,0,0,52,262,1,0,
        0,0,54,264,1,0,0,0,56,280,1,0,0,0,58,289,1,0,0,0,60,61,3,2,1,0,61,
        62,5,0,0,1,62,1,1,0,0,0,63,64,3,4,2,0,64,65,3,2,1,0,65,68,1,0,0,
        0,66,68,1,0,0,0,67,63,1,0,0,0,67,66,1,0,0,0,68,3,1,0,0,0,69,70,3,
        30,15,0,70,71,5,5,0,0,71,91,1,0,0,0,72,73,3,16,8,0,73,74,5,5,0,0,
        74,91,1,0,0,0,75,76,3,26,13,0,76,77,5,5,0,0,77,91,1,0,0,0,78,79,
        3,46,23,0,79,80,5,5,0,0,80,91,1,0,0,0,81,91,3,14,7,0,82,91,3,10,
        5,0,83,91,3,8,4,0,84,91,3,32,16,0,85,91,3,34,17,0,86,87,3,36,18,
        0,87,88,5,5,0,0,88,91,1,0,0,0,89,91,3,6,3,0,90,69,1,0,0,0,90,72,
        1,0,0,0,90,75,1,0,0,0,90,78,1,0,0,0,90,81,1,0,0,0,90,82,1,0,0,0,
        90,83,1,0,0,0,90,84,1,0,0,0,90,85,1,0,0,0,90,86,1,0,0,0,90,89,1,
        0,0,0,91,5,1,0,0,0,92,93,5,3,0,0,93,94,3,2,1,0,94,95,5,4,0,0,95,
        7,1,0,0,0,96,97,5,22,0,0,97,101,5,1,0,0,98,102,3,48,24,0,99,102,
        3,28,14,0,100,102,5,15,0,0,101,98,1,0,0,0,101,99,1,0,0,0,101,100,
        1,0,0,0,102,103,1,0,0,0,103,106,5,2,0,0,104,107,3,4,2,0,105,107,
        3,6,3,0,106,104,1,0,0,0,106,105,1,0,0,0,107,9,1,0,0,0,108,109,5,
        19,0,0,109,113,5,1,0,0,110,114,3,48,24,0,111,114,3,28,14,0,112,114,
        5,15,0,0,113,110,1,0,0,0,113,111,1,0,0,0,113,112,1,0,0,0,114,115,
        1,0,0,0,115,116,5,2,0,0,116,117,3,4,2,0,117,118,3,12,6,0,118,11,
        1,0,0,0,119,120,5,20,0,0,120,123,3,4,2,0,121,123,1,0,0,0,122,119,
        1,0,0,0,122,121,1,0,0,0,123,13,1,0,0,0,124,125,5,21,0,0,125,128,
        5,1,0,0,126,129,3,24,12,0,127,129,1,0,0,0,128,126,1,0,0,0,128,127,
        1,0,0,0,129,130,1,0,0,0,130,133,5,5,0,0,131,134,3,28,14,0,132,134,
        1,0,0,0,133,131,1,0,0,0,133,132,1,0,0,0,134,135,1,0,0,0,135,138,
        5,5,0,0,136,139,3,26,13,0,137,139,1,0,0,0,138,136,1,0,0,0,138,137,
        1,0,0,0,139,140,1,0,0,0,140,143,5,2,0,0,141,144,3,6,3,0,142,144,
        3,4,2,0,143,141,1,0,0,0,143,142,1,0,0,0,144,15,1,0,0,0,145,146,3,
        22,11,0,146,147,5,24,0,0,147,148,3,20,10,0,148,149,3,18,9,0,149,
        17,1,0,0,0,150,151,5,7,0,0,151,152,5,24,0,0,152,153,3,20,10,0,153,
        154,3,18,9,0,154,157,1,0,0,0,155,157,1,0,0,0,156,150,1,0,0,0,156,
        155,1,0,0,0,157,19,1,0,0,0,158,159,5,6,0,0,159,162,3,48,24,0,160,
        162,1,0,0,0,161,158,1,0,0,0,161,160,1,0,0,0,162,21,1,0,0,0,163,164,
        7,0,0,0,164,23,1,0,0,0,165,169,5,24,0,0,166,169,3,30,15,0,167,169,
        3,16,8,0,168,165,1,0,0,0,168,166,1,0,0,0,168,167,1,0,0,0,169,25,
        1,0,0,0,170,171,5,24,0,0,171,175,5,13,0,0,172,173,5,13,0,0,173,175,
        5,24,0,0,174,170,1,0,0,0,174,172,1,0,0,0,175,27,1,0,0,0,176,177,
        5,24,0,0,177,178,5,14,0,0,178,189,5,24,0,0,179,180,5,24,0,0,180,
        181,5,14,0,0,181,189,5,16,0,0,182,183,5,16,0,0,183,184,5,14,0,0,
        184,189,5,24,0,0,185,186,5,16,0,0,186,187,5,14,0,0,187,189,5,16,
        0,0,188,176,1,0,0,0,188,179,1,0,0,0,188,182,1,0,0,0,188,185,1,0,
        0,0,189,29,1,0,0,0,190,191,5,24,0,0,191,192,5,6,0,0,192,193,3,48,
        24,0,193,31,1,0,0,0,194,195,3,22,11,0,195,196,5,24,0,0,196,197,5,
        1,0,0,197,198,3,38,19,0,198,199,5,2,0,0,199,200,3,6,3,0,200,33,1,
        0,0,0,201,202,3,22,11,0,202,203,5,24,0,0,203,204,5,1,0,0,204,205,
        3,38,19,0,205,206,5,2,0,0,206,207,5,5,0,0,207,35,1,0,0,0,208,209,
        5,24,0,0,209,210,5,1,0,0,210,211,3,42,21,0,211,212,5,2,0,0,212,37,
        1,0,0,0,213,214,3,22,11,0,214,215,5,24,0,0,215,216,3,40,20,0,216,
        219,1,0,0,0,217,219,1,0,0,0,218,213,1,0,0,0,218,217,1,0,0,0,219,
        39,1,0,0,0,220,221,5,7,0,0,221,222,3,22,11,0,222,223,5,24,0,0,223,
        224,3,40,20,0,224,227,1,0,0,0,225,227,1,0,0,0,226,220,1,0,0,0,226,
        225,1,0,0,0,227,41,1,0,0,0,228,229,3,48,24,0,229,230,3,44,22,0,230,
        233,1,0,0,0,231,233,1,0,0,0,232,228,1,0,0,0,232,231,1,0,0,0,233,
        43,1,0,0,0,234,235,5,7,0,0,235,236,3,48,24,0,236,237,3,44,22,0,237,
        240,1,0,0,0,238,240,1,0,0,0,239,234,1,0,0,0,239,238,1,0,0,0,240,
        45,1,0,0,0,241,246,5,23,0,0,242,247,3,48,24,0,243,247,5,15,0,0,244,
        247,3,28,14,0,245,247,1,0,0,0,246,242,1,0,0,0,246,243,1,0,0,0,246,
        244,1,0,0,0,246,245,1,0,0,0,247,47,1,0,0,0,248,249,3,50,25,0,249,
        49,1,0,0,0,250,251,3,54,27,0,251,252,3,52,26,0,252,51,1,0,0,0,253,
        254,5,8,0,0,254,255,3,54,27,0,255,256,3,52,26,0,256,263,1,0,0,0,
        257,258,5,9,0,0,258,259,3,54,27,0,259,260,3,52,26,0,260,263,1,0,
        0,0,261,263,1,0,0,0,262,253,1,0,0,0,262,257,1,0,0,0,262,261,1,0,
        0,0,263,53,1,0,0,0,264,265,3,58,29,0,265,266,3,56,28,0,266,55,1,
        0,0,0,267,268,5,10,0,0,268,269,3,58,29,0,269,270,3,56,28,0,270,281,
        1,0,0,0,271,272,5,11,0,0,272,273,3,58,29,0,273,274,3,56,28,0,274,
        281,1,0,0,0,275,276,5,12,0,0,276,277,3,58,29,0,277,278,3,56,28,0,
        278,281,1,0,0,0,279,281,1,0,0,0,280,267,1,0,0,0,280,271,1,0,0,0,
        280,275,1,0,0,0,280,279,1,0,0,0,281,57,1,0,0,0,282,290,5,16,0,0,
        283,290,5,24,0,0,284,285,5,1,0,0,285,286,3,50,25,0,286,287,5,2,0,
        0,287,290,1,0,0,0,288,290,3,36,18,0,289,282,1,0,0,0,289,283,1,0,
        0,0,289,284,1,0,0,0,289,288,1,0,0,0,290,59,1,0,0,0,23,67,90,101,
        106,113,122,128,133,138,143,156,161,168,174,188,218,226,232,239,
        246,262,280,289
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "','", "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'double'", 
                     "'if'", "'else'", "'for'", "'while'", "'return'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "ASIG", 
                      "COMA", "SUMA", "RESTA", "MULT", "DIV", "MOD", "INCDEC", 
                      "COMP", "LIT", "NUMERO", "INT", "DOUBLE", "IF", "ELSE", 
                      "FOR", "WHILE", "RETURN", "ID", "WS", "OTRO" ]

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
    RULE_funcion = 16
    RULE_proto = 17
    RULE_llamada = 18
    RULE_argumento = 19
    RULE_masArgumento = 20
    RULE_largumento = 21
    RULE_masLargumento = 22
    RULE_ireturn = 23
    RULE_opal = 24
    RULE_exp = 25
    RULE_e = 26
    RULE_term = 27
    RULE_t = 28
    RULE_factor = 29

    ruleNames =  [ "programa", "instrucciones", "instruccion", "bloque", 
                   "iwhile", "iif", "ielse", "ifor", "declaracion", "listavar", 
                   "inic", "tipo", "inicializacion", "iincdec", "comparator", 
                   "asignacion", "funcion", "proto", "llamada", "argumento", 
                   "masArgumento", "largumento", "masLargumento", "ireturn", 
                   "opal", "exp", "e", "term", "t", "factor" ]

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
    RETURN=23
    ID=24
    WS=25
    OTRO=26

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
            self.state = 60
            self.instrucciones()
            self.state = 61
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
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 13, 17, 18, 19, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.instruccion()
                self.state = 64
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


        def ireturn(self):
            return self.getTypedRuleContext(compiladorParser.IreturnContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladorParser.IforContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladorParser.IifContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladorParser.IwhileContext,0)


        def funcion(self):
            return self.getTypedRuleContext(compiladorParser.FuncionContext,0)


        def proto(self):
            return self.getTypedRuleContext(compiladorParser.ProtoContext,0)


        def llamada(self):
            return self.getTypedRuleContext(compiladorParser.LlamadaContext,0)


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
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.asignacion()
                self.state = 70
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.declaracion()
                self.state = 73
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.iincdec()
                self.state = 76
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.ireturn()
                self.state = 79
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
                self.ifor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.iif()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 83
                self.iwhile()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 84
                self.funcion()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 85
                self.proto()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 86
                self.llamada()
                self.state = 87
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 89
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
            self.state = 92
            self.match(compiladorParser.LLA)
            self.state = 93
            self.instrucciones()
            self.state = 94
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
            self.state = 96
            self.match(compiladorParser.WHILE)
            self.state = 97
            self.match(compiladorParser.PA)
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 98
                self.opal()
                pass

            elif la_ == 2:
                self.state = 99
                self.comparator()
                pass

            elif la_ == 3:
                self.state = 100
                self.match(compiladorParser.LIT)
                pass


            self.state = 103
            self.match(compiladorParser.PC)
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 104
                self.instruccion()
                pass

            elif la_ == 2:
                self.state = 105
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
            self.state = 108
            self.match(compiladorParser.IF)
            self.state = 109
            self.match(compiladorParser.PA)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 110
                self.opal()
                pass

            elif la_ == 2:
                self.state = 111
                self.comparator()
                pass

            elif la_ == 3:
                self.state = 112
                self.match(compiladorParser.LIT)
                pass


            self.state = 115
            self.match(compiladorParser.PC)
            self.state = 116
            self.instruccion()
            self.state = 117
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
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(compiladorParser.ELSE)
                self.state = 120
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
            self.state = 124
            self.match(compiladorParser.FOR)
            self.state = 125
            self.match(compiladorParser.PA)
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 24]:
                self.state = 126
                self.inicializacion()
                pass
            elif token in [5]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 130
            self.match(compiladorParser.PYC)
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 24]:
                self.state = 131
                self.comparator()
                pass
            elif token in [5]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 135
            self.match(compiladorParser.PYC)
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 24]:
                self.state = 136
                self.iincdec()
                pass
            elif token in [2]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 140
            self.match(compiladorParser.PC)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 141
                self.bloque()
                pass

            elif la_ == 2:
                self.state = 142
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
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.tipo()
            self.state = 146
            self.match(compiladorParser.ID)
            self.state = 147
            self.inic()
            self.state = 148
            self.listavar()
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
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(compiladorParser.COMA)
                self.state = 151
                self.match(compiladorParser.ID)
                self.state = 152
                self.inic()
                self.state = 153
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
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(compiladorParser.ASIG)
                self.state = 159
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
            self.state = 163
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
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(compiladorParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
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
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(compiladorParser.ID)
                self.state = 171
                self.match(compiladorParser.INCDEC)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(compiladorParser.INCDEC)
                self.state = 173
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
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(compiladorParser.ID)
                self.state = 177
                self.match(compiladorParser.COMP)
                self.state = 178
                self.match(compiladorParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(compiladorParser.ID)
                self.state = 180
                self.match(compiladorParser.COMP)
                self.state = 181
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(compiladorParser.NUMERO)
                self.state = 183
                self.match(compiladorParser.COMP)
                self.state = 184
                self.match(compiladorParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.match(compiladorParser.NUMERO)
                self.state = 186
                self.match(compiladorParser.COMP)
                self.state = 187
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
            self.state = 190
            self.match(compiladorParser.ID)
            self.state = 191
            self.match(compiladorParser.ASIG)
            self.state = 192
            self.opal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def argumento(self):
            return self.getTypedRuleContext(compiladorParser.ArgumentoContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = compiladorParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.tipo()
            self.state = 195
            self.match(compiladorParser.ID)
            self.state = 196
            self.match(compiladorParser.PA)
            self.state = 197
            self.argumento()
            self.state = 198
            self.match(compiladorParser.PC)
            self.state = 199
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProtoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def argumento(self):
            return self.getTypedRuleContext(compiladorParser.ArgumentoContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_proto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProto" ):
                listener.enterProto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProto" ):
                listener.exitProto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProto" ):
                return visitor.visitProto(self)
            else:
                return visitor.visitChildren(self)




    def proto(self):

        localctx = compiladorParser.ProtoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_proto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.tipo()
            self.state = 202
            self.match(compiladorParser.ID)
            self.state = 203
            self.match(compiladorParser.PA)
            self.state = 204
            self.argumento()
            self.state = 205
            self.match(compiladorParser.PC)
            self.state = 206
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def largumento(self):
            return self.getTypedRuleContext(compiladorParser.LargumentoContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)




    def llamada(self):

        localctx = compiladorParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_llamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(compiladorParser.ID)
            self.state = 209
            self.match(compiladorParser.PA)
            self.state = 210
            self.largumento()
            self.state = 211
            self.match(compiladorParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def masArgumento(self):
            return self.getTypedRuleContext(compiladorParser.MasArgumentoContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_argumento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumento" ):
                listener.enterArgumento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumento" ):
                listener.exitArgumento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumento" ):
                return visitor.visitArgumento(self)
            else:
                return visitor.visitChildren(self)




    def argumento(self):

        localctx = compiladorParser.ArgumentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_argumento)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.tipo()
                self.state = 214
                self.match(compiladorParser.ID)
                self.state = 215
                self.masArgumento()
                pass
            elif token in [2]:
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


    class MasArgumentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def masArgumento(self):
            return self.getTypedRuleContext(compiladorParser.MasArgumentoContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_masArgumento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMasArgumento" ):
                listener.enterMasArgumento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMasArgumento" ):
                listener.exitMasArgumento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMasArgumento" ):
                return visitor.visitMasArgumento(self)
            else:
                return visitor.visitChildren(self)




    def masArgumento(self):

        localctx = compiladorParser.MasArgumentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_masArgumento)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(compiladorParser.COMA)
                self.state = 221
                self.tipo()
                self.state = 222
                self.match(compiladorParser.ID)
                self.state = 223
                self.masArgumento()
                pass
            elif token in [2]:
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


    class LargumentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def masLargumento(self):
            return self.getTypedRuleContext(compiladorParser.MasLargumentoContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_largumento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLargumento" ):
                listener.enterLargumento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLargumento" ):
                listener.exitLargumento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLargumento" ):
                return visitor.visitLargumento(self)
            else:
                return visitor.visitChildren(self)




    def largumento(self):

        localctx = compiladorParser.LargumentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_largumento)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 16, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.opal()
                self.state = 229
                self.masLargumento()
                pass
            elif token in [2]:
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


    class MasLargumentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def masLargumento(self):
            return self.getTypedRuleContext(compiladorParser.MasLargumentoContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_masLargumento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMasLargumento" ):
                listener.enterMasLargumento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMasLargumento" ):
                listener.exitMasLargumento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMasLargumento" ):
                return visitor.visitMasLargumento(self)
            else:
                return visitor.visitChildren(self)




    def masLargumento(self):

        localctx = compiladorParser.MasLargumentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_masLargumento)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(compiladorParser.COMA)
                self.state = 235
                self.opal()
                self.state = 236
                self.masLargumento()
                pass
            elif token in [2]:
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


    class IreturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladorParser.RETURN, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def LIT(self):
            return self.getToken(compiladorParser.LIT, 0)

        def comparator(self):
            return self.getTypedRuleContext(compiladorParser.ComparatorContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_ireturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIreturn" ):
                listener.enterIreturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIreturn" ):
                listener.exitIreturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIreturn" ):
                return visitor.visitIreturn(self)
            else:
                return visitor.visitChildren(self)




    def ireturn(self):

        localctx = compiladorParser.IreturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ireturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(compiladorParser.RETURN)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 242
                self.opal()
                pass

            elif la_ == 2:
                self.state = 243
                self.match(compiladorParser.LIT)
                pass

            elif la_ == 3:
                self.state = 244
                self.comparator()
                pass

            elif la_ == 4:
                pass


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
        self.enterRule(localctx, 48, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
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
        self.enterRule(localctx, 50, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.term()
            self.state = 251
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
        self.enterRule(localctx, 52, self.RULE_e)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(compiladorParser.SUMA)
                self.state = 254
                self.term()
                self.state = 255
                self.e()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(compiladorParser.RESTA)
                self.state = 258
                self.term()
                self.state = 259
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
        self.enterRule(localctx, 54, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.factor()
            self.state = 265
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
        self.enterRule(localctx, 56, self.RULE_t)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(compiladorParser.MULT)
                self.state = 268
                self.factor()
                self.state = 269
                self.t()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(compiladorParser.DIV)
                self.state = 272
                self.factor()
                self.state = 273
                self.t()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.match(compiladorParser.MOD)
                self.state = 276
                self.factor()
                self.state = 277
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

        def llamada(self):
            return self.getTypedRuleContext(compiladorParser.LlamadaContext,0)


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
        self.enterRule(localctx, 58, self.RULE_factor)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.match(compiladorParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.match(compiladorParser.PA)
                self.state = 285
                self.exp()
                self.state = 286
                self.match(compiladorParser.PC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 288
                self.llamada()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






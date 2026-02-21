# Generated from compilador.g4 by ANTLR 4.13.2
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
        4,1,29,313,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,80,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,103,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,3,8,132,8,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,
        142,8,10,1,11,1,11,1,11,1,12,1,12,1,12,3,12,150,8,12,1,13,1,13,1,
        13,1,13,1,13,1,13,3,13,158,8,13,1,14,1,14,1,14,3,14,163,8,14,1,15,
        1,15,1,15,1,15,1,15,3,15,170,8,15,1,15,1,15,1,15,3,15,175,8,15,1,
        15,1,15,1,15,3,15,180,8,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,
        16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,196,8,17,1,18,1,18,1,18,3,
        18,201,8,18,1,19,1,19,1,20,1,20,1,20,1,20,3,20,209,8,20,1,21,1,21,
        1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,
        3,25,239,8,25,1,26,1,26,1,26,1,26,1,26,1,26,3,26,247,8,26,1,27,1,
        27,1,27,1,27,1,27,3,27,254,8,27,1,28,1,28,1,28,1,28,3,28,260,8,28,
        1,29,1,29,1,29,1,29,1,29,3,29,267,8,29,1,30,1,30,1,31,1,31,1,31,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,283,8,32,1,33,
        1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,1,34,3,34,301,8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        3,35,311,8,35,1,35,0,0,36,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,0,
        1,1,0,20,21,316,0,72,1,0,0,0,2,79,1,0,0,0,4,102,1,0,0,0,6,104,1,
        0,0,0,8,108,1,0,0,0,10,114,1,0,0,0,12,121,1,0,0,0,14,123,1,0,0,0,
        16,131,1,0,0,0,18,133,1,0,0,0,20,141,1,0,0,0,22,143,1,0,0,0,24,149,
        1,0,0,0,26,157,1,0,0,0,28,162,1,0,0,0,30,164,1,0,0,0,32,184,1,0,
        0,0,34,195,1,0,0,0,36,200,1,0,0,0,38,202,1,0,0,0,40,208,1,0,0,0,
        42,210,1,0,0,0,44,214,1,0,0,0,46,221,1,0,0,0,48,228,1,0,0,0,50,238,
        1,0,0,0,52,246,1,0,0,0,54,253,1,0,0,0,56,259,1,0,0,0,58,261,1,0,
        0,0,60,268,1,0,0,0,62,270,1,0,0,0,64,282,1,0,0,0,66,284,1,0,0,0,
        68,300,1,0,0,0,70,310,1,0,0,0,72,73,3,2,1,0,73,74,5,0,0,1,74,1,1,
        0,0,0,75,76,3,4,2,0,76,77,3,2,1,0,77,80,1,0,0,0,78,80,1,0,0,0,79,
        75,1,0,0,0,79,78,1,0,0,0,80,3,1,0,0,0,81,82,3,42,21,0,82,83,5,5,
        0,0,83,103,1,0,0,0,84,85,3,32,16,0,85,86,5,5,0,0,86,103,1,0,0,0,
        87,88,3,40,20,0,88,89,5,5,0,0,89,103,1,0,0,0,90,91,3,58,29,0,91,
        92,5,5,0,0,92,103,1,0,0,0,93,103,3,30,15,0,94,103,3,10,5,0,95,103,
        3,8,4,0,96,103,3,44,22,0,97,103,3,46,23,0,98,99,3,48,24,0,99,100,
        5,5,0,0,100,103,1,0,0,0,101,103,3,6,3,0,102,81,1,0,0,0,102,84,1,
        0,0,0,102,87,1,0,0,0,102,90,1,0,0,0,102,93,1,0,0,0,102,94,1,0,0,
        0,102,95,1,0,0,0,102,96,1,0,0,0,102,97,1,0,0,0,102,98,1,0,0,0,102,
        101,1,0,0,0,103,5,1,0,0,0,104,105,5,3,0,0,105,106,3,2,1,0,106,107,
        5,4,0,0,107,7,1,0,0,0,108,109,5,25,0,0,109,110,5,1,0,0,110,111,3,
        12,6,0,111,112,5,2,0,0,112,113,3,4,2,0,113,9,1,0,0,0,114,115,5,22,
        0,0,115,116,5,1,0,0,116,117,3,12,6,0,117,118,5,2,0,0,118,119,3,4,
        2,0,119,120,3,28,14,0,120,11,1,0,0,0,121,122,3,14,7,0,122,13,1,0,
        0,0,123,124,3,18,9,0,124,125,3,16,8,0,125,15,1,0,0,0,126,127,5,15,
        0,0,127,128,3,18,9,0,128,129,3,16,8,0,129,132,1,0,0,0,130,132,1,
        0,0,0,131,126,1,0,0,0,131,130,1,0,0,0,132,17,1,0,0,0,133,134,3,22,
        11,0,134,135,3,20,10,0,135,19,1,0,0,0,136,137,5,14,0,0,137,138,3,
        22,11,0,138,139,3,20,10,0,139,142,1,0,0,0,140,142,1,0,0,0,141,136,
        1,0,0,0,141,140,1,0,0,0,142,21,1,0,0,0,143,144,3,26,13,0,144,145,
        3,24,12,0,145,23,1,0,0,0,146,147,5,16,0,0,147,150,3,26,13,0,148,
        150,1,0,0,0,149,146,1,0,0,0,149,148,1,0,0,0,150,25,1,0,0,0,151,158,
        3,60,30,0,152,158,5,17,0,0,153,154,5,1,0,0,154,155,3,12,6,0,155,
        156,5,2,0,0,156,158,1,0,0,0,157,151,1,0,0,0,157,152,1,0,0,0,157,
        153,1,0,0,0,158,27,1,0,0,0,159,160,5,23,0,0,160,163,3,4,2,0,161,
        163,1,0,0,0,162,159,1,0,0,0,162,161,1,0,0,0,163,29,1,0,0,0,164,165,
        5,24,0,0,165,169,5,1,0,0,166,170,3,42,21,0,167,170,3,32,16,0,168,
        170,1,0,0,0,169,166,1,0,0,0,169,167,1,0,0,0,169,168,1,0,0,0,170,
        171,1,0,0,0,171,174,5,5,0,0,172,175,3,22,11,0,173,175,1,0,0,0,174,
        172,1,0,0,0,174,173,1,0,0,0,175,176,1,0,0,0,176,179,5,5,0,0,177,
        180,3,40,20,0,178,180,1,0,0,0,179,177,1,0,0,0,179,178,1,0,0,0,180,
        181,1,0,0,0,181,182,5,2,0,0,182,183,3,4,2,0,183,31,1,0,0,0,184,185,
        3,38,19,0,185,186,5,27,0,0,186,187,3,36,18,0,187,188,3,34,17,0,188,
        33,1,0,0,0,189,190,5,7,0,0,190,191,5,27,0,0,191,192,3,36,18,0,192,
        193,3,34,17,0,193,196,1,0,0,0,194,196,1,0,0,0,195,189,1,0,0,0,195,
        194,1,0,0,0,196,35,1,0,0,0,197,198,5,6,0,0,198,201,3,60,30,0,199,
        201,1,0,0,0,200,197,1,0,0,0,200,199,1,0,0,0,201,37,1,0,0,0,202,203,
        7,0,0,0,203,39,1,0,0,0,204,205,5,27,0,0,205,209,5,13,0,0,206,207,
        5,13,0,0,207,209,5,27,0,0,208,204,1,0,0,0,208,206,1,0,0,0,209,41,
        1,0,0,0,210,211,5,27,0,0,211,212,5,6,0,0,212,213,3,60,30,0,213,43,
        1,0,0,0,214,215,3,38,19,0,215,216,5,27,0,0,216,217,5,1,0,0,217,218,
        3,50,25,0,218,219,5,2,0,0,219,220,3,6,3,0,220,45,1,0,0,0,221,222,
        3,38,19,0,222,223,5,27,0,0,223,224,5,1,0,0,224,225,3,50,25,0,225,
        226,5,2,0,0,226,227,5,5,0,0,227,47,1,0,0,0,228,229,5,27,0,0,229,
        230,5,1,0,0,230,231,3,56,28,0,231,232,5,2,0,0,232,49,1,0,0,0,233,
        234,3,38,19,0,234,235,5,27,0,0,235,236,3,52,26,0,236,239,1,0,0,0,
        237,239,1,0,0,0,238,233,1,0,0,0,238,237,1,0,0,0,239,51,1,0,0,0,240,
        241,5,7,0,0,241,242,3,38,19,0,242,243,5,27,0,0,243,244,3,52,26,0,
        244,247,1,0,0,0,245,247,1,0,0,0,246,240,1,0,0,0,246,245,1,0,0,0,
        247,53,1,0,0,0,248,249,5,7,0,0,249,250,3,60,30,0,250,251,3,54,27,
        0,251,254,1,0,0,0,252,254,1,0,0,0,253,248,1,0,0,0,253,252,1,0,0,
        0,254,55,1,0,0,0,255,256,3,60,30,0,256,257,3,54,27,0,257,260,1,0,
        0,0,258,260,1,0,0,0,259,255,1,0,0,0,259,258,1,0,0,0,260,57,1,0,0,
        0,261,266,5,26,0,0,262,267,3,60,30,0,263,267,5,17,0,0,264,267,3,
        12,6,0,265,267,1,0,0,0,266,262,1,0,0,0,266,263,1,0,0,0,266,264,1,
        0,0,0,266,265,1,0,0,0,267,59,1,0,0,0,268,269,3,62,31,0,269,61,1,
        0,0,0,270,271,3,66,33,0,271,272,3,64,32,0,272,63,1,0,0,0,273,274,
        5,8,0,0,274,275,3,66,33,0,275,276,3,64,32,0,276,283,1,0,0,0,277,
        278,5,9,0,0,278,279,3,66,33,0,279,280,3,64,32,0,280,283,1,0,0,0,
        281,283,1,0,0,0,282,273,1,0,0,0,282,277,1,0,0,0,282,281,1,0,0,0,
        283,65,1,0,0,0,284,285,3,70,35,0,285,286,3,68,34,0,286,67,1,0,0,
        0,287,288,5,10,0,0,288,289,3,70,35,0,289,290,3,68,34,0,290,301,1,
        0,0,0,291,292,5,11,0,0,292,293,3,70,35,0,293,294,3,68,34,0,294,301,
        1,0,0,0,295,296,5,12,0,0,296,297,3,70,35,0,297,298,3,68,34,0,298,
        301,1,0,0,0,299,301,1,0,0,0,300,287,1,0,0,0,300,291,1,0,0,0,300,
        295,1,0,0,0,300,299,1,0,0,0,301,69,1,0,0,0,302,311,5,18,0,0,303,
        311,5,19,0,0,304,311,5,27,0,0,305,306,5,1,0,0,306,307,3,62,31,0,
        307,308,5,2,0,0,308,311,1,0,0,0,309,311,3,48,24,0,310,302,1,0,0,
        0,310,303,1,0,0,0,310,304,1,0,0,0,310,305,1,0,0,0,310,309,1,0,0,
        0,311,71,1,0,0,0,21,79,102,131,141,149,157,162,169,174,179,195,200,
        208,238,246,253,259,266,282,300,310
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "','", "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", 
                     "'&&'", "'||'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'int'", "'double'", "'if'", "'else'", 
                     "'for'", "'while'", "'return'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "ASIG", 
                      "COMA", "SUMA", "RESTA", "MULT", "DIV", "MOD", "INCDEC", 
                      "AND", "OR", "COMP", "LIT", "NUMERO", "DECIMAL", "INT", 
                      "DOUBLE", "IF", "ELSE", "FOR", "WHILE", "RETURN", 
                      "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_bloque = 3
    RULE_iwhile = 4
    RULE_iif = 5
    RULE_condicion = 6
    RULE_orExp = 7
    RULE_orExpRest = 8
    RULE_andExp = 9
    RULE_andExpRest = 10
    RULE_comparacion = 11
    RULE_comparacionRest = 12
    RULE_termino = 13
    RULE_ielse = 14
    RULE_ifor = 15
    RULE_declaracion = 16
    RULE_listavar = 17
    RULE_inic = 18
    RULE_tipo = 19
    RULE_iincdec = 20
    RULE_asignacion = 21
    RULE_funcion = 22
    RULE_proto = 23
    RULE_llamada = 24
    RULE_argumento = 25
    RULE_listaParametros = 26
    RULE_listaArgumentos = 27
    RULE_argumentosLlamada = 28
    RULE_ireturn = 29
    RULE_opal = 30
    RULE_exp = 31
    RULE_e = 32
    RULE_term = 33
    RULE_t = 34
    RULE_factor = 35

    ruleNames =  [ "programa", "instrucciones", "instruccion", "bloque", 
                   "iwhile", "iif", "condicion", "orExp", "orExpRest", "andExp", 
                   "andExpRest", "comparacion", "comparacionRest", "termino", 
                   "ielse", "ifor", "declaracion", "listavar", "inic", "tipo", 
                   "iincdec", "asignacion", "funcion", "proto", "llamada", 
                   "argumento", "listaParametros", "listaArgumentos", "argumentosLlamada", 
                   "ireturn", "opal", "exp", "e", "term", "t", "factor" ]

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
    AND=14
    OR=15
    COMP=16
    LIT=17
    NUMERO=18
    DECIMAL=19
    INT=20
    DOUBLE=21
    IF=22
    ELSE=23
    FOR=24
    WHILE=25
    RETURN=26
    ID=27
    WS=28
    OTRO=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
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
            self.state = 72
            self.instrucciones()
            self.state = 73
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
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 13, 20, 21, 22, 24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.instruccion()
                self.state = 76
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
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.asignacion()
                self.state = 82
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.declaracion()
                self.state = 85
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.iincdec()
                self.state = 88
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.ireturn()
                self.state = 91
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.ifor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.iif()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 95
                self.iwhile()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 96
                self.funcion()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 97
                self.proto()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 98
                self.llamada()
                self.state = 99
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 101
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
            self.state = 104
            self.match(compiladorParser.LLA)
            self.state = 105
            self.instrucciones()
            self.state = 106
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

        def condicion(self):
            return self.getTypedRuleContext(compiladorParser.CondicionContext,0)


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
            self.state = 108
            self.match(compiladorParser.WHILE)
            self.state = 109
            self.match(compiladorParser.PA)
            self.state = 110
            self.condicion()
            self.state = 111
            self.match(compiladorParser.PC)
            self.state = 112
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

        def condicion(self):
            return self.getTypedRuleContext(compiladorParser.CondicionContext,0)


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
            self.state = 114
            self.match(compiladorParser.IF)
            self.state = 115
            self.match(compiladorParser.PA)
            self.state = 116
            self.condicion()
            self.state = 117
            self.match(compiladorParser.PC)
            self.state = 118
            self.instruccion()
            self.state = 119
            self.ielse()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExp(self):
            return self.getTypedRuleContext(compiladorParser.OrExpContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = compiladorParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.orExp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExp(self):
            return self.getTypedRuleContext(compiladorParser.AndExpContext,0)


        def orExpRest(self):
            return self.getTypedRuleContext(compiladorParser.OrExpRestContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_orExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExp" ):
                listener.enterOrExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExp" ):
                listener.exitOrExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExp" ):
                return visitor.visitOrExp(self)
            else:
                return visitor.visitChildren(self)




    def orExp(self):

        localctx = compiladorParser.OrExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_orExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.andExp()
            self.state = 124
            self.orExpRest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExpRestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladorParser.OR, 0)

        def andExp(self):
            return self.getTypedRuleContext(compiladorParser.AndExpContext,0)


        def orExpRest(self):
            return self.getTypedRuleContext(compiladorParser.OrExpRestContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_orExpRest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpRest" ):
                listener.enterOrExpRest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpRest" ):
                listener.exitOrExpRest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpRest" ):
                return visitor.visitOrExpRest(self)
            else:
                return visitor.visitChildren(self)




    def orExpRest(self):

        localctx = compiladorParser.OrExpRestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_orExpRest)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(compiladorParser.OR)
                self.state = 127
                self.andExp()
                self.state = 128
                self.orExpRest()
                pass
            elif token in [2, 5]:
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


    class AndExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacion(self):
            return self.getTypedRuleContext(compiladorParser.ComparacionContext,0)


        def andExpRest(self):
            return self.getTypedRuleContext(compiladorParser.AndExpRestContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_andExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExp" ):
                listener.enterAndExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExp" ):
                listener.exitAndExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExp" ):
                return visitor.visitAndExp(self)
            else:
                return visitor.visitChildren(self)




    def andExp(self):

        localctx = compiladorParser.AndExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_andExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.comparacion()
            self.state = 134
            self.andExpRest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExpRestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladorParser.AND, 0)

        def comparacion(self):
            return self.getTypedRuleContext(compiladorParser.ComparacionContext,0)


        def andExpRest(self):
            return self.getTypedRuleContext(compiladorParser.AndExpRestContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_andExpRest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpRest" ):
                listener.enterAndExpRest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpRest" ):
                listener.exitAndExpRest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpRest" ):
                return visitor.visitAndExpRest(self)
            else:
                return visitor.visitChildren(self)




    def andExpRest(self):

        localctx = compiladorParser.AndExpRestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_andExpRest)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(compiladorParser.AND)
                self.state = 137
                self.comparacion()
                self.state = 138
                self.andExpRest()
                pass
            elif token in [2, 5, 15]:
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


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(compiladorParser.TerminoContext,0)


        def comparacionRest(self):
            return self.getTypedRuleContext(compiladorParser.ComparacionRestContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = compiladorParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comparacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.termino()
            self.state = 144
            self.comparacionRest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionRestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMP(self):
            return self.getToken(compiladorParser.COMP, 0)

        def termino(self):
            return self.getTypedRuleContext(compiladorParser.TerminoContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_comparacionRest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacionRest" ):
                listener.enterComparacionRest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacionRest" ):
                listener.exitComparacionRest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacionRest" ):
                return visitor.visitComparacionRest(self)
            else:
                return visitor.visitChildren(self)




    def comparacionRest(self):

        localctx = compiladorParser.ComparacionRestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparacionRest)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(compiladorParser.COMP)
                self.state = 147
                self.termino()
                pass
            elif token in [2, 5, 14, 15]:
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


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def LIT(self):
            return self.getToken(compiladorParser.LIT, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def condicion(self):
            return self.getTypedRuleContext(compiladorParser.CondicionContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = compiladorParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_termino)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(compiladorParser.LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.match(compiladorParser.PA)
                self.state = 154
                self.condicion()
                self.state = 155
                self.match(compiladorParser.PC)
                pass


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
        self.enterRule(localctx, 28, self.RULE_ielse)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(compiladorParser.ELSE)
                self.state = 160
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

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionContext,0)


        def comparacion(self):
            return self.getTypedRuleContext(compiladorParser.ComparacionContext,0)


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
        self.enterRule(localctx, 30, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(compiladorParser.FOR)
            self.state = 165
            self.match(compiladorParser.PA)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 166
                self.asignacion()
                pass
            elif token in [20, 21]:
                self.state = 167
                self.declaracion()
                pass
            elif token in [5]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 171
            self.match(compiladorParser.PYC)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 17, 18, 19, 27]:
                self.state = 172
                self.comparacion()
                pass
            elif token in [5]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 176
            self.match(compiladorParser.PYC)
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 27]:
                self.state = 177
                self.iincdec()
                pass
            elif token in [2]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 181
            self.match(compiladorParser.PC)
            self.state = 182
            self.instruccion()
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
        self.enterRule(localctx, 32, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.tipo()
            self.state = 185
            self.match(compiladorParser.ID)
            self.state = 186
            self.inic()
            self.state = 187
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
        self.enterRule(localctx, 34, self.RULE_listavar)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(compiladorParser.COMA)
                self.state = 190
                self.match(compiladorParser.ID)
                self.state = 191
                self.inic()
                self.state = 192
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
        self.enterRule(localctx, 36, self.RULE_inic)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(compiladorParser.ASIG)
                self.state = 198
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
        self.enterRule(localctx, 38, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
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
        self.enterRule(localctx, 40, self.RULE_iincdec)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(compiladorParser.ID)
                self.state = 205
                self.match(compiladorParser.INCDEC)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(compiladorParser.INCDEC)
                self.state = 207
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
        self.enterRule(localctx, 42, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(compiladorParser.ID)
            self.state = 211
            self.match(compiladorParser.ASIG)
            self.state = 212
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
        self.enterRule(localctx, 44, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.tipo()
            self.state = 215
            self.match(compiladorParser.ID)
            self.state = 216
            self.match(compiladorParser.PA)
            self.state = 217
            self.argumento()
            self.state = 218
            self.match(compiladorParser.PC)
            self.state = 219
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
        self.enterRule(localctx, 46, self.RULE_proto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.tipo()
            self.state = 222
            self.match(compiladorParser.ID)
            self.state = 223
            self.match(compiladorParser.PA)
            self.state = 224
            self.argumento()
            self.state = 225
            self.match(compiladorParser.PC)
            self.state = 226
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

        def argumentosLlamada(self):
            return self.getTypedRuleContext(compiladorParser.ArgumentosLlamadaContext,0)


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
        self.enterRule(localctx, 48, self.RULE_llamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(compiladorParser.ID)
            self.state = 229
            self.match(compiladorParser.PA)
            self.state = 230
            self.argumentosLlamada()
            self.state = 231
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

        def listaParametros(self):
            return self.getTypedRuleContext(compiladorParser.ListaParametrosContext,0)


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
        self.enterRule(localctx, 50, self.RULE_argumento)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.tipo()
                self.state = 234
                self.match(compiladorParser.ID)
                self.state = 235
                self.listaParametros()
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


    class ListaParametrosContext(ParserRuleContext):
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

        def listaParametros(self):
            return self.getTypedRuleContext(compiladorParser.ListaParametrosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listaParametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaParametros" ):
                listener.enterListaParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaParametros" ):
                listener.exitListaParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParametros" ):
                return visitor.visitListaParametros(self)
            else:
                return visitor.visitChildren(self)




    def listaParametros(self):

        localctx = compiladorParser.ListaParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_listaParametros)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(compiladorParser.COMA)
                self.state = 241
                self.tipo()
                self.state = 242
                self.match(compiladorParser.ID)
                self.state = 243
                self.listaParametros()
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


    class ListaArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def listaArgumentos(self):
            return self.getTypedRuleContext(compiladorParser.ListaArgumentosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listaArgumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaArgumentos" ):
                listener.enterListaArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaArgumentos" ):
                listener.exitListaArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaArgumentos" ):
                return visitor.visitListaArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def listaArgumentos(self):

        localctx = compiladorParser.ListaArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_listaArgumentos)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(compiladorParser.COMA)
                self.state = 249
                self.opal()
                self.state = 250
                self.listaArgumentos()
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


    class ArgumentosLlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def listaArgumentos(self):
            return self.getTypedRuleContext(compiladorParser.ListaArgumentosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_argumentosLlamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentosLlamada" ):
                listener.enterArgumentosLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentosLlamada" ):
                listener.exitArgumentosLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentosLlamada" ):
                return visitor.visitArgumentosLlamada(self)
            else:
                return visitor.visitChildren(self)




    def argumentosLlamada(self):

        localctx = compiladorParser.ArgumentosLlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_argumentosLlamada)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 18, 19, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.opal()
                self.state = 256
                self.listaArgumentos()
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

        def condicion(self):
            return self.getTypedRuleContext(compiladorParser.CondicionContext,0)


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
        self.enterRule(localctx, 58, self.RULE_ireturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(compiladorParser.RETURN)
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 262
                self.opal()
                pass

            elif la_ == 2:
                self.state = 263
                self.match(compiladorParser.LIT)
                pass

            elif la_ == 3:
                self.state = 264
                self.condicion()
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
        self.enterRule(localctx, 60, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
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
        self.enterRule(localctx, 62, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.term()
            self.state = 271
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
        self.enterRule(localctx, 64, self.RULE_e)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(compiladorParser.SUMA)
                self.state = 274
                self.term()
                self.state = 275
                self.e()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(compiladorParser.RESTA)
                self.state = 278
                self.term()
                self.state = 279
                self.e()
                pass
            elif token in [2, 5, 7, 14, 15, 16]:
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
        self.enterRule(localctx, 66, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.factor()
            self.state = 285
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
        self.enterRule(localctx, 68, self.RULE_t)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(compiladorParser.MULT)
                self.state = 288
                self.factor()
                self.state = 289
                self.t()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.match(compiladorParser.DIV)
                self.state = 292
                self.factor()
                self.state = 293
                self.t()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.match(compiladorParser.MOD)
                self.state = 296
                self.factor()
                self.state = 297
                self.t()
                pass
            elif token in [2, 5, 7, 8, 9, 14, 15, 16]:
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

        def DECIMAL(self):
            return self.getToken(compiladorParser.DECIMAL, 0)

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
        self.enterRule(localctx, 70, self.RULE_factor)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(compiladorParser.DECIMAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.match(compiladorParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 305
                self.match(compiladorParser.PA)
                self.state = 306
                self.exp()
                self.state = 307
                self.match(compiladorParser.PC)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 309
                self.llamada()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






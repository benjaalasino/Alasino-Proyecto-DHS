# Generated from c:/Users/Usuario/OneDrive/Documents/DHS2025/src/main/python/compilador.g4 by ANTLR 4.13.1
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
        4,1,33,313,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,0,3,0,79,8,0,1,
        1,1,1,1,1,1,1,3,1,85,8,1,1,2,1,2,1,2,1,2,3,2,91,8,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,103,8,3,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,125,
        8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,139,8,9,
        1,10,1,10,1,10,1,10,3,10,145,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,153,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,3,13,
        164,8,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,172,8,14,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,
        17,3,17,190,8,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,
        19,3,19,202,8,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,3,21,211,8,21,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,3,23,221,8,23,1,24,1,24,
        1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,3,27,242,8,27,1,28,1,28,1,28,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,260,8,29,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,273,
        8,30,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,3,32,283,8,32,1,33,
        1,33,1,33,1,34,1,34,1,34,1,34,1,34,3,34,293,8,34,1,35,1,35,1,35,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        3,36,311,8,36,1,36,0,0,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        0,1,1,0,23,25,316,0,78,1,0,0,0,2,84,1,0,0,0,4,90,1,0,0,0,6,102,1,
        0,0,0,8,104,1,0,0,0,10,108,1,0,0,0,12,114,1,0,0,0,14,124,1,0,0,0,
        16,126,1,0,0,0,18,138,1,0,0,0,20,144,1,0,0,0,22,152,1,0,0,0,24,154,
        1,0,0,0,26,163,1,0,0,0,28,171,1,0,0,0,30,173,1,0,0,0,32,180,1,0,
        0,0,34,189,1,0,0,0,36,191,1,0,0,0,38,201,1,0,0,0,40,203,1,0,0,0,
        42,210,1,0,0,0,44,212,1,0,0,0,46,220,1,0,0,0,48,222,1,0,0,0,50,224,
        1,0,0,0,52,229,1,0,0,0,54,241,1,0,0,0,56,243,1,0,0,0,58,259,1,0,
        0,0,60,272,1,0,0,0,62,274,1,0,0,0,64,282,1,0,0,0,66,284,1,0,0,0,
        68,292,1,0,0,0,70,294,1,0,0,0,72,310,1,0,0,0,74,75,3,2,1,0,75,76,
        3,0,0,0,76,79,1,0,0,0,77,79,5,0,0,1,78,74,1,0,0,0,78,77,1,0,0,0,
        79,1,1,0,0,0,80,85,3,24,12,0,81,85,3,32,16,0,82,85,3,30,15,0,83,
        85,3,6,3,0,84,80,1,0,0,0,84,81,1,0,0,0,84,82,1,0,0,0,84,83,1,0,0,
        0,85,3,1,0,0,0,86,87,3,6,3,0,87,88,3,4,2,0,88,91,1,0,0,0,89,91,1,
        0,0,0,90,86,1,0,0,0,90,89,1,0,0,0,91,5,1,0,0,0,92,103,3,50,25,0,
        93,103,3,24,12,0,94,103,3,12,6,0,95,103,3,10,5,0,96,103,3,16,8,0,
        97,103,3,22,11,0,98,99,3,40,20,0,99,100,5,5,0,0,100,103,1,0,0,0,
        101,103,3,8,4,0,102,92,1,0,0,0,102,93,1,0,0,0,102,94,1,0,0,0,102,
        95,1,0,0,0,102,96,1,0,0,0,102,97,1,0,0,0,102,98,1,0,0,0,102,101,
        1,0,0,0,103,7,1,0,0,0,104,105,5,3,0,0,105,106,3,4,2,0,106,107,5,
        4,0,0,107,9,1,0,0,0,108,109,5,29,0,0,109,110,5,1,0,0,110,111,3,62,
        31,0,111,112,5,2,0,0,112,113,3,6,3,0,113,11,1,0,0,0,114,115,5,26,
        0,0,115,116,5,1,0,0,116,117,3,62,31,0,117,118,5,2,0,0,118,119,3,
        6,3,0,119,120,3,14,7,0,120,13,1,0,0,0,121,122,5,27,0,0,122,125,3,
        6,3,0,123,125,1,0,0,0,124,121,1,0,0,0,124,123,1,0,0,0,125,15,1,0,
        0,0,126,127,5,28,0,0,127,128,5,1,0,0,128,129,3,18,9,0,129,130,3,
        62,31,0,130,131,5,5,0,0,131,132,3,20,10,0,132,133,5,2,0,0,133,134,
        3,6,3,0,134,17,1,0,0,0,135,139,3,24,12,0,136,139,3,50,25,0,137,139,
        1,0,0,0,138,135,1,0,0,0,138,136,1,0,0,0,138,137,1,0,0,0,139,19,1,
        0,0,0,140,141,5,31,0,0,141,142,5,6,0,0,142,145,3,52,26,0,143,145,
        1,0,0,0,144,140,1,0,0,0,144,143,1,0,0,0,145,21,1,0,0,0,146,147,5,
        30,0,0,147,148,3,52,26,0,148,149,5,5,0,0,149,153,1,0,0,0,150,151,
        5,30,0,0,151,153,5,5,0,0,152,146,1,0,0,0,152,150,1,0,0,0,153,23,
        1,0,0,0,154,155,3,48,24,0,155,156,5,31,0,0,156,157,3,26,13,0,157,
        158,3,28,14,0,158,159,5,5,0,0,159,25,1,0,0,0,160,161,5,6,0,0,161,
        164,3,52,26,0,162,164,1,0,0,0,163,160,1,0,0,0,163,162,1,0,0,0,164,
        27,1,0,0,0,165,166,5,7,0,0,166,167,5,31,0,0,167,168,3,26,13,0,168,
        169,3,28,14,0,169,172,1,0,0,0,170,172,1,0,0,0,171,165,1,0,0,0,171,
        170,1,0,0,0,172,29,1,0,0,0,173,174,3,48,24,0,174,175,5,31,0,0,175,
        176,5,1,0,0,176,177,3,34,17,0,177,178,5,2,0,0,178,179,5,5,0,0,179,
        31,1,0,0,0,180,181,3,48,24,0,181,182,5,31,0,0,182,183,5,1,0,0,183,
        184,3,34,17,0,184,185,5,2,0,0,185,186,3,8,4,0,186,33,1,0,0,0,187,
        190,3,36,18,0,188,190,1,0,0,0,189,187,1,0,0,0,189,188,1,0,0,0,190,
        35,1,0,0,0,191,192,3,48,24,0,192,193,5,31,0,0,193,194,3,38,19,0,
        194,37,1,0,0,0,195,196,5,7,0,0,196,197,3,48,24,0,197,198,5,31,0,
        0,198,199,3,38,19,0,199,202,1,0,0,0,200,202,1,0,0,0,201,195,1,0,
        0,0,201,200,1,0,0,0,202,39,1,0,0,0,203,204,5,31,0,0,204,205,5,1,
        0,0,205,206,3,42,21,0,206,207,5,2,0,0,207,41,1,0,0,0,208,211,3,44,
        22,0,209,211,1,0,0,0,210,208,1,0,0,0,210,209,1,0,0,0,211,43,1,0,
        0,0,212,213,3,52,26,0,213,214,3,46,23,0,214,45,1,0,0,0,215,216,5,
        7,0,0,216,217,3,52,26,0,217,218,3,46,23,0,218,221,1,0,0,0,219,221,
        1,0,0,0,220,215,1,0,0,0,220,219,1,0,0,0,221,47,1,0,0,0,222,223,7,
        0,0,0,223,49,1,0,0,0,224,225,5,31,0,0,225,226,5,6,0,0,226,227,3,
        52,26,0,227,228,5,5,0,0,228,51,1,0,0,0,229,230,3,56,28,0,230,231,
        3,54,27,0,231,53,1,0,0,0,232,233,5,8,0,0,233,234,3,56,28,0,234,235,
        3,54,27,0,235,242,1,0,0,0,236,237,5,9,0,0,237,238,3,56,28,0,238,
        239,3,54,27,0,239,242,1,0,0,0,240,242,1,0,0,0,241,232,1,0,0,0,241,
        236,1,0,0,0,241,240,1,0,0,0,242,55,1,0,0,0,243,244,3,60,30,0,244,
        245,3,58,29,0,245,57,1,0,0,0,246,247,5,10,0,0,247,248,3,60,30,0,
        248,249,3,58,29,0,249,260,1,0,0,0,250,251,5,11,0,0,251,252,3,60,
        30,0,252,253,3,58,29,0,253,260,1,0,0,0,254,255,5,12,0,0,255,256,
        3,60,30,0,256,257,3,58,29,0,257,260,1,0,0,0,258,260,1,0,0,0,259,
        246,1,0,0,0,259,250,1,0,0,0,259,254,1,0,0,0,259,258,1,0,0,0,260,
        59,1,0,0,0,261,273,5,31,0,0,262,273,5,22,0,0,263,273,3,40,20,0,264,
        265,5,1,0,0,265,266,3,52,26,0,266,267,5,2,0,0,267,273,1,0,0,0,268,
        269,5,9,0,0,269,273,3,60,30,0,270,271,5,8,0,0,271,273,3,60,30,0,
        272,261,1,0,0,0,272,262,1,0,0,0,272,263,1,0,0,0,272,264,1,0,0,0,
        272,268,1,0,0,0,272,270,1,0,0,0,273,61,1,0,0,0,274,275,3,66,33,0,
        275,276,3,64,32,0,276,63,1,0,0,0,277,278,5,20,0,0,278,279,3,66,33,
        0,279,280,3,64,32,0,280,283,1,0,0,0,281,283,1,0,0,0,282,277,1,0,
        0,0,282,281,1,0,0,0,283,65,1,0,0,0,284,285,3,70,35,0,285,286,3,68,
        34,0,286,67,1,0,0,0,287,288,5,19,0,0,288,289,3,70,35,0,289,290,3,
        68,34,0,290,293,1,0,0,0,291,293,1,0,0,0,292,287,1,0,0,0,292,291,
        1,0,0,0,293,69,1,0,0,0,294,295,3,52,26,0,295,296,3,72,36,0,296,71,
        1,0,0,0,297,298,5,13,0,0,298,311,3,52,26,0,299,300,5,14,0,0,300,
        311,3,52,26,0,301,302,5,15,0,0,302,311,3,52,26,0,303,304,5,16,0,
        0,304,311,3,52,26,0,305,306,5,17,0,0,306,311,3,52,26,0,307,308,5,
        18,0,0,308,311,3,52,26,0,309,311,1,0,0,0,310,297,1,0,0,0,310,299,
        1,0,0,0,310,301,1,0,0,0,310,303,1,0,0,0,310,305,1,0,0,0,310,307,
        1,0,0,0,310,309,1,0,0,0,311,73,1,0,0,0,20,78,84,90,102,124,138,144,
        152,163,171,189,201,210,220,241,259,272,282,292,310
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "','", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "'!'", 
                     "<INVALID>", "'int'", "'double'", "'void'", "'if'", 
                     "'else'", "'for'", "'while'", "'return'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "ASIG", 
                      "COMA", "SUMA", "RESTA", "MULT", "DIV", "MOD", "EQ", 
                      "NEQ", "MEN", "MAY", "MENIG", "MAYIG", "AND", "OR", 
                      "NOT", "NUMERO", "INT", "DOUBLE", "VOID", "IF", "ELSE", 
                      "FOR", "WHILE", "RETURN", "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_elemento_programa = 1
    RULE_instrucciones = 2
    RULE_instruccion = 3
    RULE_bloque = 4
    RULE_iwhile = 5
    RULE_iif = 6
    RULE_ielse = 7
    RULE_ifor = 8
    RULE_declaracion_for = 9
    RULE_asignacion_for = 10
    RULE_ireturn = 11
    RULE_declaracion_variable = 12
    RULE_inic = 13
    RULE_listavar = 14
    RULE_prototipo_funcion = 15
    RULE_declaracion_funcion = 16
    RULE_parametros_formales = 17
    RULE_lista_parametros = 18
    RULE_resto_parametros = 19
    RULE_llamada_funcion = 20
    RULE_parametros_reales = 21
    RULE_lista_expresiones = 22
    RULE_resto_expresiones = 23
    RULE_tipo = 24
    RULE_asignacion = 25
    RULE_expr = 26
    RULE_expr_rest = 27
    RULE_term = 28
    RULE_term_rest = 29
    RULE_factor = 30
    RULE_expr_logica = 31
    RULE_expr_logica_rest = 32
    RULE_expr_and = 33
    RULE_expr_and_rest = 34
    RULE_expr_comp = 35
    RULE_expr_comp_rest = 36

    ruleNames =  [ "programa", "elemento_programa", "instrucciones", "instruccion", 
                   "bloque", "iwhile", "iif", "ielse", "ifor", "declaracion_for", 
                   "asignacion_for", "ireturn", "declaracion_variable", 
                   "inic", "listavar", "prototipo_funcion", "declaracion_funcion", 
                   "parametros_formales", "lista_parametros", "resto_parametros", 
                   "llamada_funcion", "parametros_reales", "lista_expresiones", 
                   "resto_expresiones", "tipo", "asignacion", "expr", "expr_rest", 
                   "term", "term_rest", "factor", "expr_logica", "expr_logica_rest", 
                   "expr_and", "expr_and_rest", "expr_comp", "expr_comp_rest" ]

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
    EQ=13
    NEQ=14
    MEN=15
    MAY=16
    MENIG=17
    MAYIG=18
    AND=19
    OR=20
    NOT=21
    NUMERO=22
    INT=23
    DOUBLE=24
    VOID=25
    IF=26
    ELSE=27
    FOR=28
    WHILE=29
    RETURN=30
    ID=31
    WS=32
    OTRO=33

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

        def elemento_programa(self):
            return self.getTypedRuleContext(compiladorParser.Elemento_programaContext,0)


        def programa(self):
            return self.getTypedRuleContext(compiladorParser.ProgramaContext,0)


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
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 23, 24, 25, 26, 28, 29, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.elemento_programa()
                self.state = 75
                self.programa()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(compiladorParser.EOF)
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


    class Elemento_programaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_variable(self):
            return self.getTypedRuleContext(compiladorParser.Declaracion_variableContext,0)


        def declaracion_funcion(self):
            return self.getTypedRuleContext(compiladorParser.Declaracion_funcionContext,0)


        def prototipo_funcion(self):
            return self.getTypedRuleContext(compiladorParser.Prototipo_funcionContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_elemento_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemento_programa" ):
                listener.enterElemento_programa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemento_programa" ):
                listener.exitElemento_programa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemento_programa" ):
                return visitor.visitElemento_programa(self)
            else:
                return visitor.visitChildren(self)




    def elemento_programa(self):

        localctx = compiladorParser.Elemento_programaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_elemento_programa)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.declaracion_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.declaracion_funcion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.prototipo_funcion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.instruccion()
                pass


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
        self.enterRule(localctx, 4, self.RULE_instrucciones)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 23, 24, 25, 26, 28, 29, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.instruccion()
                self.state = 87
                self.instrucciones()
                pass
            elif token in [4]:
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


        def declaracion_variable(self):
            return self.getTypedRuleContext(compiladorParser.Declaracion_variableContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladorParser.IifContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladorParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladorParser.IforContext,0)


        def ireturn(self):
            return self.getTypedRuleContext(compiladorParser.IreturnContext,0)


        def llamada_funcion(self):
            return self.getTypedRuleContext(compiladorParser.Llamada_funcionContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

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
        self.enterRule(localctx, 6, self.RULE_instruccion)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.declaracion_variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.iif()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.iwhile()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.ifor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 97
                self.ireturn()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.llamada_funcion()
                self.state = 99
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
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
        self.enterRule(localctx, 8, self.RULE_bloque)
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

        def expr_logica(self):
            return self.getTypedRuleContext(compiladorParser.Expr_logicaContext,0)


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
        self.enterRule(localctx, 10, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(compiladorParser.WHILE)
            self.state = 109
            self.match(compiladorParser.PA)
            self.state = 110
            self.expr_logica()
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

        def expr_logica(self):
            return self.getTypedRuleContext(compiladorParser.Expr_logicaContext,0)


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
        self.enterRule(localctx, 12, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(compiladorParser.IF)
            self.state = 115
            self.match(compiladorParser.PA)
            self.state = 116
            self.expr_logica()
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
        self.enterRule(localctx, 14, self.RULE_ielse)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(compiladorParser.ELSE)
                self.state = 122
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

        def declaracion_for(self):
            return self.getTypedRuleContext(compiladorParser.Declaracion_forContext,0)


        def expr_logica(self):
            return self.getTypedRuleContext(compiladorParser.Expr_logicaContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def asignacion_for(self):
            return self.getTypedRuleContext(compiladorParser.Asignacion_forContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

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
        self.enterRule(localctx, 16, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(compiladorParser.FOR)
            self.state = 127
            self.match(compiladorParser.PA)
            self.state = 128
            self.declaracion_for()
            self.state = 129
            self.expr_logica()
            self.state = 130
            self.match(compiladorParser.PYC)
            self.state = 131
            self.asignacion_for()
            self.state = 132
            self.match(compiladorParser.PC)
            self.state = 133
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_variable(self):
            return self.getTypedRuleContext(compiladorParser.Declaracion_variableContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_declaracion_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_for" ):
                listener.enterDeclaracion_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_for" ):
                listener.exitDeclaracion_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_for" ):
                return visitor.visitDeclaracion_for(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_for(self):

        localctx = compiladorParser.Declaracion_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declaracion_for)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.declaracion_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asignacion_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_asignacion_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion_for" ):
                listener.enterAsignacion_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion_for" ):
                listener.exitAsignacion_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion_for" ):
                return visitor.visitAsignacion_for(self)
            else:
                return visitor.visitChildren(self)




    def asignacion_for(self):

        localctx = compiladorParser.Asignacion_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_asignacion_for)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(compiladorParser.ID)
                self.state = 141
                self.match(compiladorParser.ASIG)
                self.state = 142
                self.expr()
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

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

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
        self.enterRule(localctx, 22, self.RULE_ireturn)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(compiladorParser.RETURN)
                self.state = 147
                self.expr()
                self.state = 148
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(compiladorParser.RETURN)
                self.state = 151
                self.match(compiladorParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_variableContext(ParserRuleContext):
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
            return compiladorParser.RULE_declaracion_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_variable" ):
                listener.enterDeclaracion_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_variable" ):
                listener.exitDeclaracion_variable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_variable" ):
                return visitor.visitDeclaracion_variable(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_variable(self):

        localctx = compiladorParser.Declaracion_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaracion_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.tipo()
            self.state = 155
            self.match(compiladorParser.ID)
            self.state = 156
            self.inic()
            self.state = 157
            self.listavar()
            self.state = 158
            self.match(compiladorParser.PYC)
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

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


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
        self.enterRule(localctx, 26, self.RULE_inic)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(compiladorParser.ASIG)
                self.state = 161
                self.expr()
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
        self.enterRule(localctx, 28, self.RULE_listavar)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(compiladorParser.COMA)
                self.state = 166
                self.match(compiladorParser.ID)
                self.state = 167
                self.inic()
                self.state = 168
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


    class Prototipo_funcionContext(ParserRuleContext):
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

        def parametros_formales(self):
            return self.getTypedRuleContext(compiladorParser.Parametros_formalesContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_prototipo_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrototipo_funcion" ):
                listener.enterPrototipo_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrototipo_funcion" ):
                listener.exitPrototipo_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototipo_funcion" ):
                return visitor.visitPrototipo_funcion(self)
            else:
                return visitor.visitChildren(self)




    def prototipo_funcion(self):

        localctx = compiladorParser.Prototipo_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_prototipo_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.tipo()
            self.state = 174
            self.match(compiladorParser.ID)
            self.state = 175
            self.match(compiladorParser.PA)
            self.state = 176
            self.parametros_formales()
            self.state = 177
            self.match(compiladorParser.PC)
            self.state = 178
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_funcionContext(ParserRuleContext):
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

        def parametros_formales(self):
            return self.getTypedRuleContext(compiladorParser.Parametros_formalesContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_declaracion_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_funcion" ):
                listener.enterDeclaracion_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_funcion" ):
                listener.exitDeclaracion_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_funcion" ):
                return visitor.visitDeclaracion_funcion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_funcion(self):

        localctx = compiladorParser.Declaracion_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declaracion_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.tipo()
            self.state = 181
            self.match(compiladorParser.ID)
            self.state = 182
            self.match(compiladorParser.PA)
            self.state = 183
            self.parametros_formales()
            self.state = 184
            self.match(compiladorParser.PC)
            self.state = 185
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parametros_formalesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_parametros(self):
            return self.getTypedRuleContext(compiladorParser.Lista_parametrosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_parametros_formales

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros_formales" ):
                listener.enterParametros_formales(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros_formales" ):
                listener.exitParametros_formales(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros_formales" ):
                return visitor.visitParametros_formales(self)
            else:
                return visitor.visitChildren(self)




    def parametros_formales(self):

        localctx = compiladorParser.Parametros_formalesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parametros_formales)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.lista_parametros()
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


    class Lista_parametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def resto_parametros(self):
            return self.getTypedRuleContext(compiladorParser.Resto_parametrosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_lista_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_parametros" ):
                listener.enterLista_parametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_parametros" ):
                listener.exitLista_parametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_parametros" ):
                return visitor.visitLista_parametros(self)
            else:
                return visitor.visitChildren(self)




    def lista_parametros(self):

        localctx = compiladorParser.Lista_parametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lista_parametros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.tipo()
            self.state = 192
            self.match(compiladorParser.ID)
            self.state = 193
            self.resto_parametros()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Resto_parametrosContext(ParserRuleContext):
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

        def resto_parametros(self):
            return self.getTypedRuleContext(compiladorParser.Resto_parametrosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_resto_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResto_parametros" ):
                listener.enterResto_parametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResto_parametros" ):
                listener.exitResto_parametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResto_parametros" ):
                return visitor.visitResto_parametros(self)
            else:
                return visitor.visitChildren(self)




    def resto_parametros(self):

        localctx = compiladorParser.Resto_parametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_resto_parametros)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(compiladorParser.COMA)
                self.state = 196
                self.tipo()
                self.state = 197
                self.match(compiladorParser.ID)
                self.state = 198
                self.resto_parametros()
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


    class Llamada_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def parametros_reales(self):
            return self.getTypedRuleContext(compiladorParser.Parametros_realesContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_llamada_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_funcion" ):
                listener.enterLlamada_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_funcion" ):
                listener.exitLlamada_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada_funcion" ):
                return visitor.visitLlamada_funcion(self)
            else:
                return visitor.visitChildren(self)




    def llamada_funcion(self):

        localctx = compiladorParser.Llamada_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_llamada_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(compiladorParser.ID)
            self.state = 204
            self.match(compiladorParser.PA)
            self.state = 205
            self.parametros_reales()
            self.state = 206
            self.match(compiladorParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parametros_realesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_expresiones(self):
            return self.getTypedRuleContext(compiladorParser.Lista_expresionesContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_parametros_reales

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros_reales" ):
                listener.enterParametros_reales(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros_reales" ):
                listener.exitParametros_reales(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros_reales" ):
                return visitor.visitParametros_reales(self)
            else:
                return visitor.visitChildren(self)




    def parametros_reales(self):

        localctx = compiladorParser.Parametros_realesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parametros_reales)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 8, 9, 22, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.lista_expresiones()
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


    class Lista_expresionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


        def resto_expresiones(self):
            return self.getTypedRuleContext(compiladorParser.Resto_expresionesContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_lista_expresiones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_expresiones" ):
                listener.enterLista_expresiones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_expresiones" ):
                listener.exitLista_expresiones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_expresiones" ):
                return visitor.visitLista_expresiones(self)
            else:
                return visitor.visitChildren(self)




    def lista_expresiones(self):

        localctx = compiladorParser.Lista_expresionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lista_expresiones)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.expr()
            self.state = 213
            self.resto_expresiones()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Resto_expresionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


        def resto_expresiones(self):
            return self.getTypedRuleContext(compiladorParser.Resto_expresionesContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_resto_expresiones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResto_expresiones" ):
                listener.enterResto_expresiones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResto_expresiones" ):
                listener.exitResto_expresiones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResto_expresiones" ):
                return visitor.visitResto_expresiones(self)
            else:
                return visitor.visitChildren(self)




    def resto_expresiones(self):

        localctx = compiladorParser.Resto_expresionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_resto_expresiones)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(compiladorParser.COMA)
                self.state = 216
                self.expr()
                self.state = 217
                self.resto_expresiones()
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


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladorParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladorParser.DOUBLE, 0)

        def VOID(self):
            return self.getToken(compiladorParser.VOID, 0)

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
        self.enterRule(localctx, 48, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

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
        self.enterRule(localctx, 50, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(compiladorParser.ID)
            self.state = 225
            self.match(compiladorParser.ASIG)
            self.state = 226
            self.expr()
            self.state = 227
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def expr_rest(self):
            return self.getTypedRuleContext(compiladorParser.Expr_restContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = compiladorParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.term()
            self.state = 230
            self.expr_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladorParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def expr_rest(self):
            return self.getTypedRuleContext(compiladorParser.Expr_restContext,0)


        def RESTA(self):
            return self.getToken(compiladorParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_expr_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_rest" ):
                listener.enterExpr_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_rest" ):
                listener.exitExpr_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_rest" ):
                return visitor.visitExpr_rest(self)
            else:
                return visitor.visitChildren(self)




    def expr_rest(self):

        localctx = compiladorParser.Expr_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr_rest)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(compiladorParser.SUMA)
                self.state = 233
                self.term()
                self.state = 234
                self.expr_rest()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(compiladorParser.RESTA)
                self.state = 237
                self.term()
                self.state = 238
                self.expr_rest()
                pass
            elif token in [2, 5, 7, 13, 14, 15, 16, 17, 18, 19, 20]:
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


        def term_rest(self):
            return self.getTypedRuleContext(compiladorParser.Term_restContext,0)


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
        self.enterRule(localctx, 56, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.factor()
            self.state = 244
            self.term_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladorParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def term_rest(self):
            return self.getTypedRuleContext(compiladorParser.Term_restContext,0)


        def DIV(self):
            return self.getToken(compiladorParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladorParser.MOD, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_term_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_rest" ):
                listener.enterTerm_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_rest" ):
                listener.exitTerm_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_rest" ):
                return visitor.visitTerm_rest(self)
            else:
                return visitor.visitChildren(self)




    def term_rest(self):

        localctx = compiladorParser.Term_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_term_rest)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(compiladorParser.MULT)
                self.state = 247
                self.factor()
                self.state = 248
                self.term_rest()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(compiladorParser.DIV)
                self.state = 251
                self.factor()
                self.state = 252
                self.term_rest()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.match(compiladorParser.MOD)
                self.state = 255
                self.factor()
                self.state = 256
                self.term_rest()
                pass
            elif token in [2, 5, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20]:
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

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def NUMERO(self):
            return self.getToken(compiladorParser.NUMERO, 0)

        def llamada_funcion(self):
            return self.getTypedRuleContext(compiladorParser.Llamada_funcionContext,0)


        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def RESTA(self):
            return self.getToken(compiladorParser.RESTA, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def SUMA(self):
            return self.getToken(compiladorParser.SUMA, 0)

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
        self.enterRule(localctx, 60, self.RULE_factor)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(compiladorParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self.llamada_funcion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.match(compiladorParser.PA)
                self.state = 265
                self.expr()
                self.state = 266
                self.match(compiladorParser.PC)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 268
                self.match(compiladorParser.RESTA)
                self.state = 269
                self.factor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 270
                self.match(compiladorParser.SUMA)
                self.state = 271
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_logicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_and(self):
            return self.getTypedRuleContext(compiladorParser.Expr_andContext,0)


        def expr_logica_rest(self):
            return self.getTypedRuleContext(compiladorParser.Expr_logica_restContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expr_logica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_logica" ):
                listener.enterExpr_logica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_logica" ):
                listener.exitExpr_logica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_logica" ):
                return visitor.visitExpr_logica(self)
            else:
                return visitor.visitChildren(self)




    def expr_logica(self):

        localctx = compiladorParser.Expr_logicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr_logica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.expr_and()
            self.state = 275
            self.expr_logica_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_logica_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladorParser.OR, 0)

        def expr_and(self):
            return self.getTypedRuleContext(compiladorParser.Expr_andContext,0)


        def expr_logica_rest(self):
            return self.getTypedRuleContext(compiladorParser.Expr_logica_restContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expr_logica_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_logica_rest" ):
                listener.enterExpr_logica_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_logica_rest" ):
                listener.exitExpr_logica_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_logica_rest" ):
                return visitor.visitExpr_logica_rest(self)
            else:
                return visitor.visitChildren(self)




    def expr_logica_rest(self):

        localctx = compiladorParser.Expr_logica_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr_logica_rest)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(compiladorParser.OR)
                self.state = 278
                self.expr_and()
                self.state = 279
                self.expr_logica_rest()
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


    class Expr_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_comp(self):
            return self.getTypedRuleContext(compiladorParser.Expr_compContext,0)


        def expr_and_rest(self):
            return self.getTypedRuleContext(compiladorParser.Expr_and_restContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expr_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_and" ):
                listener.enterExpr_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_and" ):
                listener.exitExpr_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_and" ):
                return visitor.visitExpr_and(self)
            else:
                return visitor.visitChildren(self)




    def expr_and(self):

        localctx = compiladorParser.Expr_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr_and)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.expr_comp()
            self.state = 285
            self.expr_and_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_and_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladorParser.AND, 0)

        def expr_comp(self):
            return self.getTypedRuleContext(compiladorParser.Expr_compContext,0)


        def expr_and_rest(self):
            return self.getTypedRuleContext(compiladorParser.Expr_and_restContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expr_and_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_and_rest" ):
                listener.enterExpr_and_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_and_rest" ):
                listener.exitExpr_and_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_and_rest" ):
                return visitor.visitExpr_and_rest(self)
            else:
                return visitor.visitChildren(self)




    def expr_and_rest(self):

        localctx = compiladorParser.Expr_and_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr_and_rest)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(compiladorParser.AND)
                self.state = 288
                self.expr_comp()
                self.state = 289
                self.expr_and_rest()
                pass
            elif token in [2, 5, 20]:
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


    class Expr_compContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


        def expr_comp_rest(self):
            return self.getTypedRuleContext(compiladorParser.Expr_comp_restContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expr_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_comp" ):
                listener.enterExpr_comp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_comp" ):
                listener.exitExpr_comp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_comp" ):
                return visitor.visitExpr_comp(self)
            else:
                return visitor.visitChildren(self)




    def expr_comp(self):

        localctx = compiladorParser.Expr_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr_comp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.expr()
            self.state = 295
            self.expr_comp_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_comp_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(compiladorParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(compiladorParser.ExprContext,0)


        def NEQ(self):
            return self.getToken(compiladorParser.NEQ, 0)

        def MEN(self):
            return self.getToken(compiladorParser.MEN, 0)

        def MAY(self):
            return self.getToken(compiladorParser.MAY, 0)

        def MENIG(self):
            return self.getToken(compiladorParser.MENIG, 0)

        def MAYIG(self):
            return self.getToken(compiladorParser.MAYIG, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_expr_comp_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_comp_rest" ):
                listener.enterExpr_comp_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_comp_rest" ):
                listener.exitExpr_comp_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_comp_rest" ):
                return visitor.visitExpr_comp_rest(self)
            else:
                return visitor.visitChildren(self)




    def expr_comp_rest(self):

        localctx = compiladorParser.Expr_comp_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr_comp_rest)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(compiladorParser.EQ)
                self.state = 298
                self.expr()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(compiladorParser.NEQ)
                self.state = 300
                self.expr()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 301
                self.match(compiladorParser.MEN)
                self.state = 302
                self.expr()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 303
                self.match(compiladorParser.MAY)
                self.state = 304
                self.expr()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 305
                self.match(compiladorParser.MENIG)
                self.state = 306
                self.expr()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 307
                self.match(compiladorParser.MAYIG)
                self.state = 308
                self.expr()
                pass
            elif token in [2, 5, 19, 20]:
                self.enterOuterAlt(localctx, 7)

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






# Generated from Chibchombiano.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

 
import numpy as np
dictionary_symbols = dict() 
from ASTNode.Puts import Puts 

from ASTNode.Function import Function
from ASTNode.Arguments import Arguments

from ASTNode.And import And
from ASTNode.Or import Or
from ASTNode.Not import Not

from ASTNode.GreaterThan import GreaterThan
from ASTNode.LowerThan import LowerThan
from ASTNode.EqualsThan import EqualsThan
from ASTNode.LowerOrEqualThan import LowerOrEqualThan 
from ASTNode.GreaterOrEqualThan import GreaterOrEqualThan

from ASTNode.If import If
from ASTNode.WhileLoop import WhileLoop

from ASTNode.Addition import Addition
from ASTNode.Substraction import Substraction
from ASTNode.Multiplication import Multiplication
from ASTNode.Division import Division
from ASTNode.Module import Module
from ASTNode.Exponent import Exponent



from ASTNode.Constant import Constant
from ASTNode.VarDecl import VarDecl
from ASTNode.VarRef import VarRef
from ASTNode.VarAssign import VarAssign
from ASTNode.Array import Array

def serializedATN():
    return [
        4,1,49,304,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,68,8,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,5,5,93,8,5,10,5,12,5,96,9,5,1,5,1,5,1,5,1,5,
        1,5,1,5,5,5,104,8,5,10,5,12,5,107,9,5,1,5,3,5,110,8,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,123,8,6,10,6,12,6,126,9,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,140,8,8,10,8,
        12,8,143,9,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,151,8,9,10,9,12,9,154,9,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,163,8,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,5,11,187,8,11,10,11,12,11,190,9,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,202,8,12,
        10,12,12,12,205,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,5,13,221,8,13,10,13,12,13,224,9,13,1,14,
        1,14,1,14,1,14,1,14,1,14,5,14,232,8,14,10,14,12,14,235,9,14,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,3,15,256,8,15,1,16,1,16,1,16,3,16,261,8,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,273,8,
        17,10,17,12,17,276,9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        5,18,286,8,18,10,18,12,18,289,9,18,3,18,291,8,18,1,18,1,18,1,18,
        1,18,1,18,3,18,298,8,18,1,18,1,18,3,18,302,8,18,1,18,0,0,19,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,1,1,0,5,15,320,
        0,38,1,0,0,0,2,67,1,0,0,0,4,69,1,0,0,0,6,73,1,0,0,0,8,78,1,0,0,0,
        10,82,1,0,0,0,12,113,1,0,0,0,14,130,1,0,0,0,16,133,1,0,0,0,18,144,
        1,0,0,0,20,162,1,0,0,0,22,164,1,0,0,0,24,191,1,0,0,0,26,206,1,0,
        0,0,28,225,1,0,0,0,30,255,1,0,0,0,32,257,1,0,0,0,34,265,1,0,0,0,
        36,277,1,0,0,0,38,44,6,0,-1,0,39,40,3,2,1,0,40,41,6,0,-1,0,41,43,
        1,0,0,0,42,39,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,
        45,47,1,0,0,0,46,44,1,0,0,0,47,48,6,0,-1,0,48,1,1,0,0,0,49,50,3,
        6,3,0,50,51,6,1,-1,0,51,68,1,0,0,0,52,53,3,4,2,0,53,54,6,1,-1,0,
        54,68,1,0,0,0,55,56,3,8,4,0,56,57,6,1,-1,0,57,68,1,0,0,0,58,59,3,
        10,5,0,59,60,6,1,-1,0,60,68,1,0,0,0,61,62,3,12,6,0,62,63,6,1,-1,
        0,63,68,1,0,0,0,64,65,3,14,7,0,65,66,6,1,-1,0,66,68,1,0,0,0,67,49,
        1,0,0,0,67,52,1,0,0,0,67,55,1,0,0,0,67,58,1,0,0,0,67,61,1,0,0,0,
        67,64,1,0,0,0,68,3,1,0,0,0,69,70,5,3,0,0,70,71,5,44,0,0,71,72,6,
        2,-1,0,72,5,1,0,0,0,73,74,5,44,0,0,74,75,5,34,0,0,75,76,3,14,7,0,
        76,77,6,3,-1,0,77,7,1,0,0,0,78,79,5,4,0,0,79,80,3,14,7,0,80,81,6,
        4,-1,0,81,9,1,0,0,0,82,83,5,16,0,0,83,84,5,39,0,0,84,85,3,14,7,0,
        85,86,5,40,0,0,86,87,6,5,-1,0,87,88,6,5,-1,0,88,94,5,37,0,0,89,90,
        3,2,1,0,90,91,6,5,-1,0,91,93,1,0,0,0,92,89,1,0,0,0,93,96,1,0,0,0,
        94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,109,5,
        38,0,0,98,99,5,17,0,0,99,105,5,37,0,0,100,101,3,2,1,0,101,102,6,
        5,-1,0,102,104,1,0,0,0,103,100,1,0,0,0,104,107,1,0,0,0,105,103,1,
        0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,1,0,0,0,108,110,5,
        38,0,0,109,98,1,0,0,0,109,110,1,0,0,0,110,111,1,0,0,0,111,112,6,
        5,-1,0,112,11,1,0,0,0,113,114,5,18,0,0,114,115,5,39,0,0,115,116,
        3,14,7,0,116,117,5,40,0,0,117,118,6,6,-1,0,118,124,5,37,0,0,119,
        120,3,2,1,0,120,121,6,6,-1,0,121,123,1,0,0,0,122,119,1,0,0,0,123,
        126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,
        124,1,0,0,0,127,128,5,38,0,0,128,129,6,6,-1,0,129,13,1,0,0,0,130,
        131,3,16,8,0,131,132,6,7,-1,0,132,15,1,0,0,0,133,134,3,18,9,0,134,
        141,6,8,-1,0,135,136,5,26,0,0,136,137,3,18,9,0,137,138,6,8,-1,0,
        138,140,1,0,0,0,139,135,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,
        141,142,1,0,0,0,142,17,1,0,0,0,143,141,1,0,0,0,144,145,3,20,10,0,
        145,152,6,9,-1,0,146,147,5,25,0,0,147,148,3,20,10,0,148,149,6,9,
        -1,0,149,151,1,0,0,0,150,146,1,0,0,0,151,154,1,0,0,0,152,150,1,0,
        0,0,152,153,1,0,0,0,153,19,1,0,0,0,154,152,1,0,0,0,155,156,3,22,
        11,0,156,157,6,10,-1,0,157,163,1,0,0,0,158,159,5,27,0,0,159,160,
        3,22,11,0,160,161,6,10,-1,0,161,163,1,0,0,0,162,155,1,0,0,0,162,
        158,1,0,0,0,163,21,1,0,0,0,164,165,3,24,12,0,165,188,6,11,-1,0,166,
        167,5,28,0,0,167,168,3,24,12,0,168,169,6,11,-1,0,169,187,1,0,0,0,
        170,171,5,29,0,0,171,172,3,24,12,0,172,173,6,11,-1,0,173,187,1,0,
        0,0,174,175,5,32,0,0,175,176,3,24,12,0,176,177,6,11,-1,0,177,187,
        1,0,0,0,178,179,5,30,0,0,179,180,3,24,12,0,180,181,6,11,-1,0,181,
        187,1,0,0,0,182,183,5,31,0,0,183,184,3,24,12,0,184,185,6,11,-1,0,
        185,187,1,0,0,0,186,166,1,0,0,0,186,170,1,0,0,0,186,174,1,0,0,0,
        186,178,1,0,0,0,186,182,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,
        188,189,1,0,0,0,189,23,1,0,0,0,190,188,1,0,0,0,191,192,3,26,13,0,
        192,203,6,12,-1,0,193,194,5,19,0,0,194,195,3,26,13,0,195,196,6,12,
        -1,0,196,202,1,0,0,0,197,198,5,20,0,0,198,199,3,26,13,0,199,200,
        6,12,-1,0,200,202,1,0,0,0,201,193,1,0,0,0,201,197,1,0,0,0,202,205,
        1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,25,1,0,0,0,205,203,1,
        0,0,0,206,207,3,28,14,0,207,222,6,13,-1,0,208,209,5,21,0,0,209,210,
        3,28,14,0,210,211,6,13,-1,0,211,221,1,0,0,0,212,213,5,22,0,0,213,
        214,3,28,14,0,214,215,6,13,-1,0,215,221,1,0,0,0,216,217,5,23,0,0,
        217,218,3,28,14,0,218,219,6,13,-1,0,219,221,1,0,0,0,220,208,1,0,
        0,0,220,212,1,0,0,0,220,216,1,0,0,0,221,224,1,0,0,0,222,220,1,0,
        0,0,222,223,1,0,0,0,223,27,1,0,0,0,224,222,1,0,0,0,225,226,3,30,
        15,0,226,233,6,14,-1,0,227,228,5,24,0,0,228,229,3,30,15,0,229,230,
        6,14,-1,0,230,232,1,0,0,0,231,227,1,0,0,0,232,235,1,0,0,0,233,231,
        1,0,0,0,233,234,1,0,0,0,234,29,1,0,0,0,235,233,1,0,0,0,236,237,5,
        46,0,0,237,256,6,15,-1,0,238,239,5,45,0,0,239,256,6,15,-1,0,240,
        241,5,44,0,0,241,256,6,15,-1,0,242,243,5,43,0,0,243,256,6,15,-1,
        0,244,245,5,39,0,0,245,246,3,14,7,0,246,247,5,40,0,0,247,248,6,15,
        -1,0,248,256,1,0,0,0,249,250,3,36,18,0,250,251,6,15,-1,0,251,256,
        1,0,0,0,252,253,3,32,16,0,253,254,6,15,-1,0,254,256,1,0,0,0,255,
        236,1,0,0,0,255,238,1,0,0,0,255,240,1,0,0,0,255,242,1,0,0,0,255,
        244,1,0,0,0,255,249,1,0,0,0,255,252,1,0,0,0,256,31,1,0,0,0,257,258,
        7,0,0,0,258,260,5,39,0,0,259,261,3,34,17,0,260,259,1,0,0,0,260,261,
        1,0,0,0,261,262,1,0,0,0,262,263,5,40,0,0,263,264,6,16,-1,0,264,33,
        1,0,0,0,265,266,6,17,-1,0,266,267,3,14,7,0,267,274,6,17,-1,0,268,
        269,5,1,0,0,269,270,3,14,7,0,270,271,6,17,-1,0,271,273,1,0,0,0,272,
        268,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,
        35,1,0,0,0,276,274,1,0,0,0,277,301,6,18,-1,0,278,290,5,35,0,0,279,
        280,3,14,7,0,280,287,6,18,-1,0,281,282,5,1,0,0,282,283,3,14,7,0,
        283,284,6,18,-1,0,284,286,1,0,0,0,285,281,1,0,0,0,286,289,1,0,0,
        0,287,285,1,0,0,0,287,288,1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,
        0,290,279,1,0,0,0,290,291,1,0,0,0,291,292,1,0,0,0,292,302,5,36,0,
        0,293,294,5,45,0,0,294,297,5,42,0,0,295,296,5,45,0,0,296,298,5,42,
        0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,299,1,0,0,0,299,300,5,45,
        0,0,300,302,6,18,-1,0,301,278,1,0,0,0,301,293,1,0,0,0,302,37,1,0,
        0,0,23,44,67,94,105,109,124,141,152,162,186,188,201,203,220,222,
        233,255,260,274,287,290,297,301
    ]

class ChibchombianoParser ( Parser ):

    grammarFileName = "Chibchombiano.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'program'", "'var'", "'puts'", 
                     "'sin'", "'cos'", "'tan'", "'csc'", "'sec'", "'cot'", 
                     "'plot'", "'inv'", "'trans'", "'scatter'", "'get_elem'", 
                     "'if'", "'else'", "'while'", "'+'", "'-'", "'*'", "'/'", 
                     "'mod'", "'^'", "'and'", "'or'", "'not'", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'!='", "'='", "'['", "']'", 
                     "'{'", "'}'", "'('", "')'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PROGRAM", "VAR", "PUTS", 
                      "SIN", "COS", "TAN", "CSC", "SEC", "COT", "PLOT", 
                      "INV", "TRANS", "SCATTER", "GET_ELEM", "IF", "ELSE", 
                      "WHILE", "PLUS", "MINUS", "MULT", "DIV", "MOD", "POW", 
                      "AND", "OR", "NOT", "GT", "LT", "GEQ", "LEQ", "EQ", 
                      "NEQ", "ASSIGN", "SQUARE_BRACKET_OPEN", "SQUARE_BRACKET_CLOSE", 
                      "BRACKET_OPEN", "BRACKET_CLOSE", "PAR_OPEN", "PAR_CLOSE", 
                      "SEMICOLON", "COLON", "BOOLEAN", "ID", "NUMBER", "STRING", 
                      "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_var_decl = 2
    RULE_var_assign = 3
    RULE_std_output = 4
    RULE_conditional = 5
    RULE_while_loop = 6
    RULE_expression = 7
    RULE_or_expression = 8
    RULE_and_expression = 9
    RULE_not_expression = 10
    RULE_logical_expression = 11
    RULE_sum = 12
    RULE_factor = 13
    RULE_exponent = 14
    RULE_term = 15
    RULE_function = 16
    RULE_arguments = 17
    RULE_array = 18

    ruleNames =  [ "program", "sentence", "var_decl", "var_assign", "std_output", 
                   "conditional", "while_loop", "expression", "or_expression", 
                   "and_expression", "not_expression", "logical_expression", 
                   "sum", "factor", "exponent", "term", "function", "arguments", 
                   "array" ]

    EOF = Token.EOF
    T__0=1
    PROGRAM=2
    VAR=3
    PUTS=4
    SIN=5
    COS=6
    TAN=7
    CSC=8
    SEC=9
    COT=10
    PLOT=11
    INV=12
    TRANS=13
    SCATTER=14
    GET_ELEM=15
    IF=16
    ELSE=17
    WHILE=18
    PLUS=19
    MINUS=20
    MULT=21
    DIV=22
    MOD=23
    POW=24
    AND=25
    OR=26
    NOT=27
    GT=28
    LT=29
    GEQ=30
    LEQ=31
    EQ=32
    NEQ=33
    ASSIGN=34
    SQUARE_BRACKET_OPEN=35
    SQUARE_BRACKET_CLOSE=36
    BRACKET_OPEN=37
    BRACKET_CLOSE=38
    PAR_OPEN=39
    PAR_CLOSE=40
    SEMICOLON=41
    COLON=42
    BOOLEAN=43
    ID=44
    NUMBER=45
    STRING=46
    WS=47
    COMMENT=48
    LINE_COMMENT=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None







    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._sentence = None # SentenceContext

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.SentenceContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.SentenceContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ChibchombianoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            body=list()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 132525645496312) != 0:
                self.state = 39
                localctx._sentence = self.sentence()
                body.append(localctx._sentence.node)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            for node in body:
                node.execute(dictionary_symbols)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._var_assign = None # Var_assignContext
            self._var_decl = None # Var_declContext
            self._std_output = None # Std_outputContext
            self._conditional = None # ConditionalContext
            self._while_loop = None # While_loopContext
            self._expression = None # ExpressionContext

        def var_assign(self):
            return self.getTypedRuleContext(ChibchombianoParser.Var_assignContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(ChibchombianoParser.Var_declContext,0)


        def std_output(self):
            return self.getTypedRuleContext(ChibchombianoParser.Std_outputContext,0)


        def conditional(self):
            return self.getTypedRuleContext(ChibchombianoParser.ConditionalContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(ChibchombianoParser.While_loopContext,0)


        def expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = ChibchombianoParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                localctx._var_assign = self.var_assign()
                localctx.node =localctx._var_assign.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                localctx._var_decl = self.var_decl()
                localctx.node = localctx._var_decl.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                localctx._std_output = self.std_output()
                localctx.node = localctx._std_output.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                localctx._conditional = self.conditional()
                localctx.node=localctx._conditional.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                localctx._while_loop = self.while_loop()
                localctx.node = localctx._while_loop.node
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                localctx._expression = self.expression()
                localctx.node = localctx._expression.node
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ID = None # Token

        def VAR(self):
            return self.getToken(ChibchombianoParser.VAR, 0)

        def ID(self):
            return self.getToken(ChibchombianoParser.ID, 0)

        def getRuleIndex(self):
            return ChibchombianoParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ChibchombianoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ChibchombianoParser.VAR)
            self.state = 70
            localctx._ID = self.match(ChibchombianoParser.ID)

            localctx.node = VarDecl((None if localctx._ID is None else localctx._ID.text))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ID = None # Token
            self._expression = None # ExpressionContext

        def ID(self):
            return self.getToken(ChibchombianoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ChibchombianoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_var_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assign" ):
                listener.enterVar_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assign" ):
                listener.exitVar_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = ChibchombianoParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            localctx._ID = self.match(ChibchombianoParser.ID)
            self.state = 74
            self.match(ChibchombianoParser.ASSIGN)
            self.state = 75
            localctx._expression = self.expression()
            localctx.node = VarAssign((None if localctx._ID is None else localctx._ID.text),localctx._expression.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Std_outputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expression = None # ExpressionContext

        def PUTS(self):
            return self.getToken(ChibchombianoParser.PUTS, 0)

        def expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_std_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStd_output" ):
                listener.enterStd_output(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStd_output" ):
                listener.exitStd_output(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStd_output" ):
                return visitor.visitStd_output(self)
            else:
                return visitor.visitChildren(self)




    def std_output(self):

        localctx = ChibchombianoParser.Std_outputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_std_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ChibchombianoParser.PUTS)
            self.state = 79
            localctx._expression = self.expression()
            localctx.node = Puts(localctx._expression.node) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expression = None # ExpressionContext
            self.s1 = None # SentenceContext
            self.s2 = None # SentenceContext

        def IF(self):
            return self.getToken(ChibchombianoParser.IF, 0)

        def PAR_OPEN(self):
            return self.getToken(ChibchombianoParser.PAR_OPEN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,0)


        def PAR_CLOSE(self):
            return self.getToken(ChibchombianoParser.PAR_CLOSE, 0)

        def BRACKET_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.BRACKET_OPEN)
            else:
                return self.getToken(ChibchombianoParser.BRACKET_OPEN, i)

        def BRACKET_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.BRACKET_CLOSE)
            else:
                return self.getToken(ChibchombianoParser.BRACKET_CLOSE, i)

        def ELSE(self):
            return self.getToken(ChibchombianoParser.ELSE, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.SentenceContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.SentenceContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = ChibchombianoParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ChibchombianoParser.IF)
            self.state = 83
            self.match(ChibchombianoParser.PAR_OPEN)
            self.state = 84
            localctx._expression = self.expression()
            self.state = 85
            self.match(ChibchombianoParser.PAR_CLOSE)
            body=list()
            elseBody=list()
            self.state = 88
            self.match(ChibchombianoParser.BRACKET_OPEN)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 132525645496312) != 0:
                self.state = 89
                localctx.s1 = self.sentence()
                body.append(localctx.s1.node)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(ChibchombianoParser.BRACKET_CLOSE)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 98
                self.match(ChibchombianoParser.ELSE)
                self.state = 99
                self.match(ChibchombianoParser.BRACKET_OPEN)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 132525645496312) != 0:
                    self.state = 100
                    localctx.s2 = self.sentence()
                    elseBody.append(localctx.s2.node)
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 108
                self.match(ChibchombianoParser.BRACKET_CLOSE)


            localctx.node = If(localctx._expression.node,body,elseBody)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expression = None # ExpressionContext
            self.s1 = None # SentenceContext

        def WHILE(self):
            return self.getToken(ChibchombianoParser.WHILE, 0)

        def PAR_OPEN(self):
            return self.getToken(ChibchombianoParser.PAR_OPEN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,0)


        def PAR_CLOSE(self):
            return self.getToken(ChibchombianoParser.PAR_CLOSE, 0)

        def BRACKET_OPEN(self):
            return self.getToken(ChibchombianoParser.BRACKET_OPEN, 0)

        def BRACKET_CLOSE(self):
            return self.getToken(ChibchombianoParser.BRACKET_CLOSE, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.SentenceContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.SentenceContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = ChibchombianoParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ChibchombianoParser.WHILE)
            self.state = 114
            self.match(ChibchombianoParser.PAR_OPEN)
            self.state = 115
            localctx._expression = self.expression()
            self.state = 116
            self.match(ChibchombianoParser.PAR_CLOSE)
            body=list()
            self.state = 118
            self.match(ChibchombianoParser.BRACKET_OPEN)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 132525645496312) != 0:
                self.state = 119
                localctx.s1 = self.sentence()
                body.append(localctx.s1.node)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(ChibchombianoParser.BRACKET_CLOSE)
            localctx.node = WhileLoop(localctx._expression.node,body)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._or_expression = None # Or_expressionContext

        def or_expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.Or_expressionContext,0)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ChibchombianoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            localctx._or_expression = self.or_expression()
            localctx.node=localctx._or_expression.node
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # And_expressionContext
            self.e2 = None # And_expressionContext

        def and_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.And_expressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.And_expressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.OR)
            else:
                return self.getToken(ChibchombianoParser.OR, i)

        def getRuleIndex(self):
            return ChibchombianoParser.RULE_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_expression" ):
                listener.enterOr_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_expression" ):
                listener.exitOr_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_expression" ):
                return visitor.visitOr_expression(self)
            else:
                return visitor.visitChildren(self)




    def or_expression(self):

        localctx = ChibchombianoParser.Or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_or_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            localctx.e1 = self.and_expression()
            localctx.node=localctx.e1.node
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 135
                self.match(ChibchombianoParser.OR)
                self.state = 136
                localctx.e2 = self.and_expression()
                localctx.node=Or(localctx.node,localctx.e2.node)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # Not_expressionContext
            self.e2 = None # Not_expressionContext

        def not_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.Not_expressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.Not_expressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.AND)
            else:
                return self.getToken(ChibchombianoParser.AND, i)

        def getRuleIndex(self):
            return ChibchombianoParser.RULE_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_expression" ):
                listener.enterAnd_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_expression" ):
                listener.exitAnd_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expression" ):
                return visitor.visitAnd_expression(self)
            else:
                return visitor.visitChildren(self)




    def and_expression(self):

        localctx = ChibchombianoParser.And_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_and_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            localctx.e1 = self.not_expression()
            localctx.node=localctx.e1.node
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 146
                self.match(ChibchombianoParser.AND)
                self.state = 147
                localctx.e2 = self.not_expression()
                localctx.node=And(localctx.node,localctx.e2.node)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # Logical_expressionContext
            self.e2 = None # Logical_expressionContext

        def NOT(self):
            return self.getToken(ChibchombianoParser.NOT, 0)

        def logical_expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.Logical_expressionContext,0)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_not_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_expression" ):
                listener.enterNot_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_expression" ):
                listener.exitNot_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_expression" ):
                return visitor.visitNot_expression(self)
            else:
                return visitor.visitChildren(self)




    def not_expression(self):

        localctx = ChibchombianoParser.Not_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_not_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 35, 39, 43, 44, 45, 46]:
                self.state = 155
                localctx.e1 = self.logical_expression()
                localctx.node=localctx.e1.node
                pass
            elif token in [27]:
                self.state = 158
                self.match(ChibchombianoParser.NOT)
                self.state = 159
                localctx.e2 = self.logical_expression()
                localctx.node=Not(localctx.e2.node)
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


    class Logical_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # SumContext
            self.e2 = None # SumContext
            self.e3 = None # SumContext
            self.e4 = None # SumContext
            self.e5 = None # SumContext
            self.e6 = None # SumContext

        def sum_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.SumContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.SumContext,i)


        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.GT)
            else:
                return self.getToken(ChibchombianoParser.GT, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.LT)
            else:
                return self.getToken(ChibchombianoParser.LT, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.EQ)
            else:
                return self.getToken(ChibchombianoParser.EQ, i)

        def GEQ(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.GEQ)
            else:
                return self.getToken(ChibchombianoParser.GEQ, i)

        def LEQ(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.LEQ)
            else:
                return self.getToken(ChibchombianoParser.LEQ, i)

        def getRuleIndex(self):
            return ChibchombianoParser.RULE_logical_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_expression" ):
                listener.enterLogical_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_expression" ):
                listener.exitLogical_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)




    def logical_expression(self):

        localctx = ChibchombianoParser.Logical_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logical_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            localctx.e1 = self.sum_()
            localctx.node=localctx.e1.node
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 8321499136) != 0:
                self.state = 186
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [28]:
                    self.state = 166
                    self.match(ChibchombianoParser.GT)
                    self.state = 167
                    localctx.e2 = self.sum_()
                    localctx.node=GreaterThan(localctx.node,localctx.e2.node)
                    pass
                elif token in [29]:
                    self.state = 170
                    self.match(ChibchombianoParser.LT)
                    self.state = 171
                    localctx.e3 = self.sum_()
                    localctx.node=LowerThan(localctx.node,localctx.e3.node)
                    pass
                elif token in [32]:
                    self.state = 174
                    self.match(ChibchombianoParser.EQ)
                    self.state = 175
                    localctx.e4 = self.sum_()
                    localctx.node=EqualsThan(localctx.node,localctx.e4.node)
                    pass
                elif token in [30]:
                    self.state = 178
                    self.match(ChibchombianoParser.GEQ)
                    self.state = 179
                    localctx.e5 = self.sum_()
                    localctx.node=GreaterOrEqualThan(localctx.node,localctx.e5.node)
                    pass
                elif token in [31]:
                    self.state = 182
                    self.match(ChibchombianoParser.LEQ)
                    self.state = 183
                    localctx.e6 = self.sum_()
                    localctx.node=LowerOrEqualThan(localctx.node,localctx.e6.node)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.t1 = None # FactorContext
            self.t2 = None # FactorContext
            self.t3 = None # FactorContext

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.FactorContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.FactorContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.PLUS)
            else:
                return self.getToken(ChibchombianoParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.MINUS)
            else:
                return self.getToken(ChibchombianoParser.MINUS, i)

        def getRuleIndex(self):
            return ChibchombianoParser.RULE_sum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)




    def sum_(self):

        localctx = ChibchombianoParser.SumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            localctx.t1 = self.factor()
            localctx.node= localctx.t1.node
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 201
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [19]:
                    self.state = 193
                    self.match(ChibchombianoParser.PLUS)
                    self.state = 194
                    localctx.t2 = self.factor()
                    localctx.node= Addition(localctx.node,localctx.t2.node)
                    pass
                elif token in [20]:
                    self.state = 197
                    self.match(ChibchombianoParser.MINUS)
                    self.state = 198
                    localctx.t3 = self.factor()
                    localctx.node = Substraction(localctx.node,localctx.t3.node)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.node = None
            self.t1 = None # ExponentContext
            self.t2 = None # ExponentContext
            self.t3 = None # ExponentContext
            self.t4 = None # ExponentContext

        def exponent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.ExponentContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.ExponentContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.MULT)
            else:
                return self.getToken(ChibchombianoParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.DIV)
            else:
                return self.getToken(ChibchombianoParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.MOD)
            else:
                return self.getToken(ChibchombianoParser.MOD, i)

        def getRuleIndex(self):
            return ChibchombianoParser.RULE_factor

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

        localctx = ChibchombianoParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            localctx.t1 = self.exponent()
            localctx.node = localctx.t1.node 
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0:
                self.state = 220
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [21]:
                    self.state = 208
                    self.match(ChibchombianoParser.MULT)
                    self.state = 209
                    localctx.t2 = self.exponent()
                    localctx.node = Multiplication(localctx.node, localctx.t2.node)
                    pass
                elif token in [22]:
                    self.state = 212
                    self.match(ChibchombianoParser.DIV)
                    self.state = 213
                    localctx.t3 = self.exponent()
                    localctx.node = Division(localctx.node,localctx.t3.node)
                    pass
                elif token in [23]:
                    self.state = 216
                    self.match(ChibchombianoParser.MOD)
                    self.state = 217
                    localctx.t4 = self.exponent()
                    localctx.node =  Module(localctx.node,localctx.t4.node)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.t1 = None # TermContext
            self.t2 = None # TermContext

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.TermContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.TermContext,i)


        def POW(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.POW)
            else:
                return self.getToken(ChibchombianoParser.POW, i)

        def getRuleIndex(self):
            return ChibchombianoParser.RULE_exponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponent" ):
                listener.enterExponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponent" ):
                listener.exitExponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)




    def exponent(self):

        localctx = ChibchombianoParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exponent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            localctx.t1 = self.term()
            localctx.node=localctx.t1.node
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 227
                self.match(ChibchombianoParser.POW)
                self.state = 228
                localctx.t2 = self.term()
                localctx.node = Exponent(localctx.node,localctx.t2.node)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.node = None
            self._STRING = None # Token
            self._NUMBER = None # Token
            self._ID = None # Token
            self._BOOLEAN = None # Token
            self.e1 = None # ExpressionContext
            self._array = None # ArrayContext
            self._function = None # FunctionContext

        def STRING(self):
            return self.getToken(ChibchombianoParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ChibchombianoParser.NUMBER, 0)

        def ID(self):
            return self.getToken(ChibchombianoParser.ID, 0)

        def BOOLEAN(self):
            return self.getToken(ChibchombianoParser.BOOLEAN, 0)

        def PAR_OPEN(self):
            return self.getToken(ChibchombianoParser.PAR_OPEN, 0)

        def PAR_CLOSE(self):
            return self.getToken(ChibchombianoParser.PAR_CLOSE, 0)

        def expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,0)


        def array(self):
            return self.getTypedRuleContext(ChibchombianoParser.ArrayContext,0)


        def function(self):
            return self.getTypedRuleContext(ChibchombianoParser.FunctionContext,0)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_term

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

        localctx = ChibchombianoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_term)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                localctx._STRING = self.match(ChibchombianoParser.STRING)
                localctx.node=Constant((None if localctx._STRING is None else localctx._STRING.text))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                localctx._NUMBER = self.match(ChibchombianoParser.NUMBER)

                splitted = (None if localctx._NUMBER is None else localctx._NUMBER.text).split(".") 
                if len(splitted)==1:
                        localctx.node = Constant(int((None if localctx._NUMBER is None else localctx._NUMBER.text)))
                elif len(splitted)==2:
                        localctx.node = Constant(float((None if localctx._NUMBER is None else localctx._NUMBER.text)))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                localctx._ID = self.match(ChibchombianoParser.ID)
                localctx.node = VarRef((None if localctx._ID is None else localctx._ID.text))
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
                localctx._BOOLEAN = self.match(ChibchombianoParser.BOOLEAN)

                put_bool=lambda x: x=="true"
                localctx.node= Constant(put_bool((None if localctx._BOOLEAN is None else localctx._BOOLEAN.text)))
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.match(ChibchombianoParser.PAR_OPEN)
                self.state = 245
                localctx.e1 = self.expression()
                self.state = 246
                self.match(ChibchombianoParser.PAR_CLOSE)
                localctx.node=localctx.e1.node
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 249
                localctx._array = self.array()
                localctx.node=localctx._array.node
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 252
                localctx._function = self.function()
                localctx.node = localctx._function.node
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # Token
            self._arguments = None # ArgumentsContext

        def PAR_OPEN(self):
            return self.getToken(ChibchombianoParser.PAR_OPEN, 0)

        def PAR_CLOSE(self):
            return self.getToken(ChibchombianoParser.PAR_CLOSE, 0)

        def SIN(self):
            return self.getToken(ChibchombianoParser.SIN, 0)

        def COS(self):
            return self.getToken(ChibchombianoParser.COS, 0)

        def TAN(self):
            return self.getToken(ChibchombianoParser.TAN, 0)

        def CSC(self):
            return self.getToken(ChibchombianoParser.CSC, 0)

        def SEC(self):
            return self.getToken(ChibchombianoParser.SEC, 0)

        def COT(self):
            return self.getToken(ChibchombianoParser.COT, 0)

        def PLOT(self):
            return self.getToken(ChibchombianoParser.PLOT, 0)

        def SCATTER(self):
            return self.getToken(ChibchombianoParser.SCATTER, 0)

        def GET_ELEM(self):
            return self.getToken(ChibchombianoParser.GET_ELEM, 0)

        def INV(self):
            return self.getToken(ChibchombianoParser.INV, 0)

        def TRANS(self):
            return self.getToken(ChibchombianoParser.TRANS, 0)

        def arguments(self):
            return self.getTypedRuleContext(ChibchombianoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ChibchombianoParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            localctx.e1 = self._input.LT(1)
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 65504) != 0):
                localctx.e1 = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 258
            self.match(ChibchombianoParser.PAR_OPEN)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 132525645168608) != 0:
                self.state = 259
                localctx._arguments = self.arguments()


            self.state = 262
            self.match(ChibchombianoParser.PAR_CLOSE)
            localctx.node = Function((None if localctx.e1 is None else localctx.e1.text),localctx._arguments.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = ChibchombianoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.node = Arguments()
            self.state = 266
            localctx.e1 = self.expression()
            localctx.node.add(localctx.e1.node)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 268
                self.match(ChibchombianoParser.T__0)
                self.state = 269
                localctx.e2 = self.expression()
                localctx.node.add(localctx.e2.node)
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext
            self.n1 = None # Token
            self.n2 = None # Token
            self.n3 = None # Token

        def SQUARE_BRACKET_OPEN(self):
            return self.getToken(ChibchombianoParser.SQUARE_BRACKET_OPEN, 0)

        def SQUARE_BRACKET_CLOSE(self):
            return self.getToken(ChibchombianoParser.SQUARE_BRACKET_CLOSE, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.COLON)
            else:
                return self.getToken(ChibchombianoParser.COLON, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.NUMBER)
            else:
                return self.getToken(ChibchombianoParser.NUMBER, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ChibchombianoParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.node = Array()
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.state = 278
                self.match(ChibchombianoParser.SQUARE_BRACKET_OPEN)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 132525645168608) != 0:
                    self.state = 279
                    localctx.e1 = self.expression()
                    localctx.node.add(localctx.e1.node)
                    self.state = 287
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 281
                        self.match(ChibchombianoParser.T__0)
                        self.state = 282
                        localctx.e2 = self.expression()
                        localctx.node.add(localctx.e2.node)
                        self.state = 289
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 292
                self.match(ChibchombianoParser.SQUARE_BRACKET_CLOSE)
                pass
            elif token in [45]:
                self.state = 293
                localctx.n1 = self.match(ChibchombianoParser.NUMBER)
                self.state = 294
                self.match(ChibchombianoParser.COLON)
                self.state = 297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 295
                    localctx.n2 = self.match(ChibchombianoParser.NUMBER)
                    self.state = 296
                    self.match(ChibchombianoParser.COLON)


                self.state = 299
                localctx.n3 = self.match(ChibchombianoParser.NUMBER)
                localctx.node.arange(localctx.n1,localctx.n2,localctx.n3)
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






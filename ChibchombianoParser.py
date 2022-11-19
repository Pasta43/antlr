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
        4,1,35,226,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,55,8,1,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,5,5,80,8,5,10,5,12,5,83,9,5,1,5,1,5,1,5,1,
        5,1,5,1,5,5,5,91,8,5,10,5,12,5,94,9,5,1,5,3,5,97,8,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,110,8,6,10,6,12,6,113,9,6,1,
        6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,143,8,8,10,8,12,
        8,146,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,158,8,9,10,
        9,12,9,161,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,177,8,10,10,10,12,10,180,9,10,1,11,1,11,
        1,11,1,11,1,11,1,11,5,11,188,8,11,10,11,12,11,191,9,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        207,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,217,8,13,10,
        13,12,13,220,9,13,3,13,222,8,13,1,13,1,13,1,13,0,0,14,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,0,0,237,0,28,1,0,0,0,2,54,1,0,0,0,4,56,
        1,0,0,0,6,60,1,0,0,0,8,65,1,0,0,0,10,69,1,0,0,0,12,100,1,0,0,0,14,
        117,1,0,0,0,16,120,1,0,0,0,18,147,1,0,0,0,20,162,1,0,0,0,22,181,
        1,0,0,0,24,206,1,0,0,0,26,208,1,0,0,0,28,34,6,0,-1,0,29,30,3,2,1,
        0,30,31,6,0,-1,0,31,33,1,0,0,0,32,29,1,0,0,0,33,36,1,0,0,0,34,32,
        1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,6,0,-1,0,
        38,1,1,0,0,0,39,40,3,6,3,0,40,41,6,1,-1,0,41,55,1,0,0,0,42,43,3,
        4,2,0,43,44,6,1,-1,0,44,55,1,0,0,0,45,46,3,8,4,0,46,47,6,1,-1,0,
        47,55,1,0,0,0,48,49,3,10,5,0,49,50,6,1,-1,0,50,55,1,0,0,0,51,52,
        3,12,6,0,52,53,6,1,-1,0,53,55,1,0,0,0,54,39,1,0,0,0,54,42,1,0,0,
        0,54,45,1,0,0,0,54,48,1,0,0,0,54,51,1,0,0,0,55,3,1,0,0,0,56,57,5,
        3,0,0,57,58,5,32,0,0,58,59,6,2,-1,0,59,5,1,0,0,0,60,61,5,32,0,0,
        61,62,5,23,0,0,62,63,3,14,7,0,63,64,6,3,-1,0,64,7,1,0,0,0,65,66,
        5,4,0,0,66,67,3,14,7,0,67,68,6,4,-1,0,68,9,1,0,0,0,69,70,5,5,0,0,
        70,71,5,28,0,0,71,72,3,14,7,0,72,73,5,29,0,0,73,74,6,5,-1,0,74,75,
        6,5,-1,0,75,81,5,26,0,0,76,77,3,2,1,0,77,78,6,5,-1,0,78,80,1,0,0,
        0,79,76,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,
        1,0,0,0,83,81,1,0,0,0,84,96,5,27,0,0,85,86,5,6,0,0,86,92,5,26,0,
        0,87,88,3,2,1,0,88,89,6,5,-1,0,89,91,1,0,0,0,90,87,1,0,0,0,91,94,
        1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,
        95,97,5,27,0,0,96,85,1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,6,
        5,-1,0,99,11,1,0,0,0,100,101,5,7,0,0,101,102,5,28,0,0,102,103,3,
        14,7,0,103,104,5,29,0,0,104,105,6,6,-1,0,105,111,5,26,0,0,106,107,
        3,2,1,0,107,108,6,6,-1,0,108,110,1,0,0,0,109,106,1,0,0,0,110,113,
        1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,111,
        1,0,0,0,114,115,5,27,0,0,115,116,6,6,-1,0,116,13,1,0,0,0,117,118,
        3,16,8,0,118,119,6,7,-1,0,119,15,1,0,0,0,120,121,3,18,9,0,121,144,
        6,8,-1,0,122,123,5,17,0,0,123,124,3,14,7,0,124,125,6,8,-1,0,125,
        143,1,0,0,0,126,127,5,18,0,0,127,128,3,14,7,0,128,129,6,8,-1,0,129,
        143,1,0,0,0,130,131,5,21,0,0,131,132,3,14,7,0,132,133,6,8,-1,0,133,
        143,1,0,0,0,134,135,5,19,0,0,135,136,3,14,7,0,136,137,6,8,-1,0,137,
        143,1,0,0,0,138,139,5,20,0,0,139,140,3,14,7,0,140,141,6,8,-1,0,141,
        143,1,0,0,0,142,122,1,0,0,0,142,126,1,0,0,0,142,130,1,0,0,0,142,
        134,1,0,0,0,142,138,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,
        145,1,0,0,0,145,17,1,0,0,0,146,144,1,0,0,0,147,148,3,20,10,0,148,
        159,6,9,-1,0,149,150,5,8,0,0,150,151,3,20,10,0,151,152,6,9,-1,0,
        152,158,1,0,0,0,153,154,5,9,0,0,154,155,3,20,10,0,155,156,6,9,-1,
        0,156,158,1,0,0,0,157,149,1,0,0,0,157,153,1,0,0,0,158,161,1,0,0,
        0,159,157,1,0,0,0,159,160,1,0,0,0,160,19,1,0,0,0,161,159,1,0,0,0,
        162,163,3,22,11,0,163,178,6,10,-1,0,164,165,5,10,0,0,165,166,3,22,
        11,0,166,167,6,10,-1,0,167,177,1,0,0,0,168,169,5,11,0,0,169,170,
        3,22,11,0,170,171,6,10,-1,0,171,177,1,0,0,0,172,173,5,12,0,0,173,
        174,3,22,11,0,174,175,6,10,-1,0,175,177,1,0,0,0,176,164,1,0,0,0,
        176,168,1,0,0,0,176,172,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,
        178,179,1,0,0,0,179,21,1,0,0,0,180,178,1,0,0,0,181,182,3,24,12,0,
        182,189,6,11,-1,0,183,184,5,13,0,0,184,185,3,24,12,0,185,186,6,11,
        -1,0,186,188,1,0,0,0,187,183,1,0,0,0,188,191,1,0,0,0,189,187,1,0,
        0,0,189,190,1,0,0,0,190,23,1,0,0,0,191,189,1,0,0,0,192,193,5,33,
        0,0,193,207,6,12,-1,0,194,195,5,32,0,0,195,207,6,12,-1,0,196,197,
        5,31,0,0,197,207,6,12,-1,0,198,199,5,28,0,0,199,200,3,14,7,0,200,
        201,5,29,0,0,201,202,6,12,-1,0,202,207,1,0,0,0,203,204,3,26,13,0,
        204,205,6,12,-1,0,205,207,1,0,0,0,206,192,1,0,0,0,206,194,1,0,0,
        0,206,196,1,0,0,0,206,198,1,0,0,0,206,203,1,0,0,0,207,25,1,0,0,0,
        208,209,6,13,-1,0,209,221,5,24,0,0,210,211,3,14,7,0,211,218,6,13,
        -1,0,212,213,5,1,0,0,213,214,3,14,7,0,214,215,6,13,-1,0,215,217,
        1,0,0,0,216,212,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,
        1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,221,210,1,0,0,0,221,222,
        1,0,0,0,222,223,1,0,0,0,223,224,5,25,0,0,224,27,1,0,0,0,16,34,54,
        81,92,96,111,142,144,157,159,176,178,189,206,218,221
    ]

class ChibchombianoParser ( Parser ):

    grammarFileName = "Chibchombiano.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'program'", "'var'", "'puts'", 
                     "'if'", "'else'", "'while'", "'+'", "'-'", "'*'", "'/'", 
                     "'mod'", "'^'", "'and'", "'or'", "'not'", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'!='", "'='", "'['", "']'", 
                     "'{'", "'}'", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PROGRAM", "VAR", "PUTS", 
                      "IF", "ELSE", "WHILE", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "POW", "AND", "OR", "NOT", "GT", "LT", "GEQ", 
                      "LEQ", "EQ", "NEQ", "ASSIGN", "SQUARE_BRACKET_OPEN", 
                      "SQUARE_BRACKET_CLOSE", "BRACKET_OPEN", "BRACKET_CLOSE", 
                      "PAR_OPEN", "PAR_CLOSE", "SEMICOLON", "BOOLEAN", "ID", 
                      "NUMBER", "STRING", "WS" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_var_decl = 2
    RULE_var_assign = 3
    RULE_std_output = 4
    RULE_conditional = 5
    RULE_while_loop = 6
    RULE_expression = 7
    RULE_logical_expression = 8
    RULE_sum = 9
    RULE_factor = 10
    RULE_exponent = 11
    RULE_term = 12
    RULE_array = 13

    ruleNames =  [ "program", "sentence", "var_decl", "var_assign", "std_output", 
                   "conditional", "while_loop", "expression", "logical_expression", 
                   "sum", "factor", "exponent", "term", "array" ]

    EOF = Token.EOF
    T__0=1
    PROGRAM=2
    VAR=3
    PUTS=4
    IF=5
    ELSE=6
    WHILE=7
    PLUS=8
    MINUS=9
    MULT=10
    DIV=11
    MOD=12
    POW=13
    AND=14
    OR=15
    NOT=16
    GT=17
    LT=18
    GEQ=19
    LEQ=20
    EQ=21
    NEQ=22
    ASSIGN=23
    SQUARE_BRACKET_OPEN=24
    SQUARE_BRACKET_CLOSE=25
    BRACKET_OPEN=26
    BRACKET_CLOSE=27
    PAR_OPEN=28
    PAR_CLOSE=29
    SEMICOLON=30
    BOOLEAN=31
    ID=32
    NUMBER=33
    STRING=34
    WS=35

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
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4294967480) != 0:
                self.state = 29
                localctx._sentence = self.sentence()
                body.append(localctx._sentence.node)
                self.state = 36
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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                localctx._var_assign = self.var_assign()
                localctx.node =localctx._var_assign.node
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                localctx._var_decl = self.var_decl()
                localctx.node = localctx._var_decl.node
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                localctx._std_output = self.std_output()
                localctx.node = localctx._std_output.node
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                localctx._conditional = self.conditional()
                localctx.node=localctx._conditional.node
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                localctx._while_loop = self.while_loop()
                localctx.node = localctx._while_loop.node
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
            self.state = 56
            self.match(ChibchombianoParser.VAR)
            self.state = 57
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
            self.state = 60
            localctx._ID = self.match(ChibchombianoParser.ID)
            self.state = 61
            self.match(ChibchombianoParser.ASSIGN)
            self.state = 62
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
            self.state = 65
            self.match(ChibchombianoParser.PUTS)
            self.state = 66
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
            self.state = 69
            self.match(ChibchombianoParser.IF)
            self.state = 70
            self.match(ChibchombianoParser.PAR_OPEN)
            self.state = 71
            localctx._expression = self.expression()
            self.state = 72
            self.match(ChibchombianoParser.PAR_CLOSE)
            body=list()
            elseBody=list()
            self.state = 75
            self.match(ChibchombianoParser.BRACKET_OPEN)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4294967480) != 0:
                self.state = 76
                localctx.s1 = self.sentence()
                body.append(localctx.s1.node)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(ChibchombianoParser.BRACKET_CLOSE)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 85
                self.match(ChibchombianoParser.ELSE)
                self.state = 86
                self.match(ChibchombianoParser.BRACKET_OPEN)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4294967480) != 0:
                    self.state = 87
                    localctx.s2 = self.sentence()
                    elseBody.append(localctx.s2.node)
                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 95
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
            self.state = 100
            self.match(ChibchombianoParser.WHILE)
            self.state = 101
            self.match(ChibchombianoParser.PAR_OPEN)
            self.state = 102
            localctx._expression = self.expression()
            self.state = 103
            self.match(ChibchombianoParser.PAR_CLOSE)
            body=list()
            self.state = 105
            self.match(ChibchombianoParser.BRACKET_OPEN)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4294967480) != 0:
                self.state = 106
                localctx.s1 = self.sentence()
                body.append(localctx.s1.node)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
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
            self._logical_expression = None # Logical_expressionContext

        def logical_expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.Logical_expressionContext,0)


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
            self.state = 117
            localctx._logical_expression = self.logical_expression()
            localctx.node=localctx._logical_expression.node
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
            self.e2 = None # ExpressionContext
            self.e3 = None # ExpressionContext
            self.e4 = None # ExpressionContext
            self.e5 = None # ExpressionContext
            self.e6 = None # ExpressionContext

        def sum_(self):
            return self.getTypedRuleContext(ChibchombianoParser.SumContext,0)


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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,i)


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
        self.enterRule(localctx, 16, self.RULE_logical_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            localctx.e1 = self.sum_()
            localctx.node=localctx.e1.node
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 142
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [17]:
                        self.state = 122
                        self.match(ChibchombianoParser.GT)
                        self.state = 123
                        localctx.e2 = self.expression()
                        localctx.node=GreaterThan(localctx.e1.node,localctx.e2.node)
                        pass
                    elif token in [18]:
                        self.state = 126
                        self.match(ChibchombianoParser.LT)
                        self.state = 127
                        localctx.e3 = self.expression()
                        localctx.node=LowerThan(localctx.e1.node,localctx.e3.node)
                        pass
                    elif token in [21]:
                        self.state = 130
                        self.match(ChibchombianoParser.EQ)
                        self.state = 131
                        localctx.e4 = self.expression()
                        localctx.node=Equals(localctx.e1.node,localctx.e4.node)
                        pass
                    elif token in [19]:
                        self.state = 134
                        self.match(ChibchombianoParser.GEQ)
                        self.state = 135
                        localctx.e5 = self.expression()
                        localctx.node=GreaterOrEqualThan(localctx.e1.node,localctx.e5.node)
                        pass
                    elif token in [20]:
                        self.state = 138
                        self.match(ChibchombianoParser.LEQ)
                        self.state = 139
                        localctx.e6 = self.expression()
                        localctx.node=LowerOrEqualThan(localctx.e1.node,localctx.e6.node)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_sum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            localctx.t1 = self.factor()
            localctx.node= localctx.t1.node
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 157
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 149
                    self.match(ChibchombianoParser.PLUS)
                    self.state = 150
                    localctx.t2 = self.factor()
                    localctx.node= Addition(localctx.node,localctx.t2.node)
                    pass
                elif token in [9]:
                    self.state = 153
                    self.match(ChibchombianoParser.MINUS)
                    self.state = 154
                    localctx.t3 = self.factor()
                    localctx.node = Substraction(localctx.node,localctx.t3.node)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 161
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
        self.enterRule(localctx, 20, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            localctx.t1 = self.exponent()
            localctx.node = localctx.t1.node 
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0:
                self.state = 176
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10]:
                    self.state = 164
                    self.match(ChibchombianoParser.MULT)
                    self.state = 165
                    localctx.t2 = self.exponent()
                    localctx.node = Multiplication(localctx.node, localctx.t2.node)
                    pass
                elif token in [11]:
                    self.state = 168
                    self.match(ChibchombianoParser.DIV)
                    self.state = 169
                    localctx.t3 = self.exponent()
                    localctx.node = Division(localctx.node,localctx.t3.node)
                    pass
                elif token in [12]:
                    self.state = 172
                    self.match(ChibchombianoParser.MOD)
                    self.state = 173
                    localctx.t4 = self.exponent()
                    localctx.node =  Module(localctx.node,localctx.t4.node)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 180
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
        self.enterRule(localctx, 22, self.RULE_exponent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            localctx.t1 = self.term()
            localctx.node=localctx.t1.node
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 183
                self.match(ChibchombianoParser.POW)
                self.state = 184
                localctx.t2 = self.term()
                localctx.node = Exponent(localctx.node,localctx.t2.node)
                self.state = 191
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
            self._NUMBER = None # Token
            self._ID = None # Token
            self._BOOLEAN = None # Token
            self._expression = None # ExpressionContext
            self._array = None # ArrayContext

        def NUMBER(self):
            return self.getToken(ChibchombianoParser.NUMBER, 0)

        def ID(self):
            return self.getToken(ChibchombianoParser.ID, 0)

        def BOOLEAN(self):
            return self.getToken(ChibchombianoParser.BOOLEAN, 0)

        def PAR_OPEN(self):
            return self.getToken(ChibchombianoParser.PAR_OPEN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,0)


        def PAR_CLOSE(self):
            return self.getToken(ChibchombianoParser.PAR_CLOSE, 0)

        def array(self):
            return self.getTypedRuleContext(ChibchombianoParser.ArrayContext,0)


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
        self.enterRule(localctx, 24, self.RULE_term)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                localctx._NUMBER = self.match(ChibchombianoParser.NUMBER)

                splitted = (None if localctx._NUMBER is None else localctx._NUMBER.text).split(".") 
                if len(splitted)==1:
                        localctx.node = Constant(int((None if localctx._NUMBER is None else localctx._NUMBER.text)))
                elif len(splitted)==2:
                        localctx.node = Constant(float((None if localctx._NUMBER is None else localctx._NUMBER.text)))

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                localctx._ID = self.match(ChibchombianoParser.ID)
                localctx.node = VarRef((None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                localctx._BOOLEAN = self.match(ChibchombianoParser.BOOLEAN)

                put_bool=lambda x: x=="true"
                localctx.node= Constant(put_bool((None if localctx._BOOLEAN is None else localctx._BOOLEAN.text)))
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 198
                self.match(ChibchombianoParser.PAR_OPEN)
                self.state = 199
                localctx._expression = self.expression()
                self.state = 200
                self.match(ChibchombianoParser.PAR_CLOSE)
                localctx.node=localctx._expression.node
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 203
                localctx._array = self.array()
                localctx.node=localctx._array.node
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def SQUARE_BRACKET_OPEN(self):
            return self.getToken(ChibchombianoParser.SQUARE_BRACKET_OPEN, 0)

        def SQUARE_BRACKET_CLOSE(self):
            return self.getToken(ChibchombianoParser.SQUARE_BRACKET_CLOSE, 0)

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
        self.enterRule(localctx, 26, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.node = Array()
            self.state = 209
            self.match(ChibchombianoParser.SQUARE_BRACKET_OPEN)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 15317598208) != 0:
                self.state = 210
                localctx.e1 = self.expression()
                localctx.node.add(localctx.e1.node)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 212
                    self.match(ChibchombianoParser.T__0)
                    self.state = 213
                    localctx.e2 = self.expression()
                    localctx.node.add(localctx.e2.node)
                    self.state = 220
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 223
            self.match(ChibchombianoParser.SQUARE_BRACKET_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






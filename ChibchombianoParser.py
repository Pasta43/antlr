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

def serializedATN():
    return [
        4,1,32,231,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,5,0,41,8,
        0,10,0,12,0,44,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,85,8,5,10,5,
        12,5,88,9,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,96,8,5,10,5,12,5,99,9,5,
        1,5,3,5,102,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        115,8,6,10,6,12,6,118,9,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,126,8,7,10,
        7,12,7,129,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,3,8,146,8,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,
        14,183,8,14,10,14,12,14,186,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,202,8,15,10,15,12,15,
        205,9,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,213,8,16,10,16,12,16,
        216,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        3,17,229,8,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,0,1,1,0,13,14,234,0,36,1,0,0,0,2,59,1,0,0,0,4,61,1,0,0,
        0,6,65,1,0,0,0,8,70,1,0,0,0,10,74,1,0,0,0,12,105,1,0,0,0,14,122,
        1,0,0,0,16,145,1,0,0,0,18,147,1,0,0,0,20,152,1,0,0,0,22,157,1,0,
        0,0,24,162,1,0,0,0,26,167,1,0,0,0,28,172,1,0,0,0,30,187,1,0,0,0,
        32,206,1,0,0,0,34,228,1,0,0,0,36,42,6,0,-1,0,37,38,3,2,1,0,38,39,
        6,0,-1,0,39,41,1,0,0,0,40,37,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,
        42,43,1,0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,6,0,-1,0,46,1,1,
        0,0,0,47,48,3,6,3,0,48,49,6,1,-1,0,49,60,1,0,0,0,50,51,3,4,2,0,51,
        52,6,1,-1,0,52,60,1,0,0,0,53,54,3,8,4,0,54,55,6,1,-1,0,55,60,1,0,
        0,0,56,57,3,10,5,0,57,58,6,1,-1,0,58,60,1,0,0,0,59,47,1,0,0,0,59,
        50,1,0,0,0,59,53,1,0,0,0,59,56,1,0,0,0,60,3,1,0,0,0,61,62,5,2,0,
        0,62,63,5,29,0,0,63,64,6,2,-1,0,64,5,1,0,0,0,65,66,5,29,0,0,66,67,
        5,22,0,0,67,68,3,28,14,0,68,69,6,3,-1,0,69,7,1,0,0,0,70,71,5,3,0,
        0,71,72,3,28,14,0,72,73,6,4,-1,0,73,9,1,0,0,0,74,75,5,4,0,0,75,76,
        5,25,0,0,76,77,3,14,7,0,77,78,5,26,0,0,78,79,6,5,-1,0,79,80,6,5,
        -1,0,80,86,5,23,0,0,81,82,3,2,1,0,82,83,6,5,-1,0,83,85,1,0,0,0,84,
        81,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,
        0,88,86,1,0,0,0,89,101,5,24,0,0,90,91,5,5,0,0,91,97,5,23,0,0,92,
        93,3,2,1,0,93,94,6,5,-1,0,94,96,1,0,0,0,95,92,1,0,0,0,96,99,1,0,
        0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,
        102,5,24,0,0,101,90,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,
        104,6,5,-1,0,104,11,1,0,0,0,105,106,5,6,0,0,106,107,5,25,0,0,107,
        108,3,14,7,0,108,109,5,26,0,0,109,110,6,6,-1,0,110,116,5,23,0,0,
        111,112,3,2,1,0,112,113,6,6,-1,0,113,115,1,0,0,0,114,111,1,0,0,0,
        115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,
        118,116,1,0,0,0,119,120,5,24,0,0,120,121,6,6,-1,0,121,13,1,0,0,0,
        122,123,3,16,8,0,123,127,6,7,-1,0,124,126,7,0,0,0,125,124,1,0,0,
        0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,15,1,0,0,0,
        129,127,1,0,0,0,130,131,3,18,9,0,131,132,6,8,-1,0,132,146,1,0,0,
        0,133,134,3,20,10,0,134,135,6,8,-1,0,135,146,1,0,0,0,136,137,3,22,
        11,0,137,138,6,8,-1,0,138,146,1,0,0,0,139,140,3,24,12,0,140,141,
        6,8,-1,0,141,146,1,0,0,0,142,143,3,26,13,0,143,144,6,8,-1,0,144,
        146,1,0,0,0,145,130,1,0,0,0,145,133,1,0,0,0,145,136,1,0,0,0,145,
        139,1,0,0,0,145,142,1,0,0,0,146,17,1,0,0,0,147,148,3,28,14,0,148,
        149,5,16,0,0,149,150,3,28,14,0,150,151,6,9,-1,0,151,19,1,0,0,0,152,
        153,3,28,14,0,153,154,5,17,0,0,154,155,3,28,14,0,155,156,6,10,-1,
        0,156,21,1,0,0,0,157,158,3,28,14,0,158,159,5,20,0,0,159,160,3,28,
        14,0,160,161,6,11,-1,0,161,23,1,0,0,0,162,163,3,28,14,0,163,164,
        5,18,0,0,164,165,3,28,14,0,165,166,6,12,-1,0,166,25,1,0,0,0,167,
        168,3,28,14,0,168,169,5,19,0,0,169,170,3,28,14,0,170,171,6,13,-1,
        0,171,27,1,0,0,0,172,173,3,30,15,0,173,184,6,14,-1,0,174,175,5,7,
        0,0,175,176,3,30,15,0,176,177,6,14,-1,0,177,183,1,0,0,0,178,179,
        5,8,0,0,179,180,3,30,15,0,180,181,6,14,-1,0,181,183,1,0,0,0,182,
        174,1,0,0,0,182,178,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,
        185,1,0,0,0,185,29,1,0,0,0,186,184,1,0,0,0,187,188,3,32,16,0,188,
        203,6,15,-1,0,189,190,5,9,0,0,190,191,3,32,16,0,191,192,6,15,-1,
        0,192,202,1,0,0,0,193,194,5,10,0,0,194,195,3,32,16,0,195,196,6,15,
        -1,0,196,202,1,0,0,0,197,198,5,11,0,0,198,199,3,32,16,0,199,200,
        6,15,-1,0,200,202,1,0,0,0,201,189,1,0,0,0,201,193,1,0,0,0,201,197,
        1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,31,1,
        0,0,0,205,203,1,0,0,0,206,207,3,34,17,0,207,214,6,16,-1,0,208,209,
        5,12,0,0,209,210,3,34,17,0,210,211,6,16,-1,0,211,213,1,0,0,0,212,
        208,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,
        33,1,0,0,0,216,214,1,0,0,0,217,218,5,30,0,0,218,229,6,17,-1,0,219,
        220,5,29,0,0,220,229,6,17,-1,0,221,222,5,28,0,0,222,229,6,17,-1,
        0,223,224,5,25,0,0,224,225,3,28,14,0,225,226,5,26,0,0,226,227,6,
        17,-1,0,227,229,1,0,0,0,228,217,1,0,0,0,228,219,1,0,0,0,228,221,
        1,0,0,0,228,223,1,0,0,0,229,35,1,0,0,0,14,42,59,86,97,101,116,127,
        145,182,184,201,203,214,228
    ]

class ChibchombianoParser ( Parser ):

    grammarFileName = "Chibchombiano.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'var'", "'puts'", "'if'", 
                     "'else'", "'while'", "'+'", "'-'", "'*'", "'/'", "'mod'", 
                     "'^'", "'and'", "'or'", "'not'", "'>'", "'<'", "'>='", 
                     "'<='", "'=='", "'!='", "'='", "'{'", "'}'", "'('", 
                     "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "VAR", "PUTS", "IF", "ELSE", 
                      "WHILE", "PLUS", "MINUS", "MULT", "DIV", "MOD", "POW", 
                      "AND", "OR", "NOT", "GT", "LT", "GEQ", "LEQ", "EQ", 
                      "NEQ", "ASSIGN", "BRACKET_OPEN", "BRACKET_CLOSE", 
                      "PAR_OPEN", "PAR_CLOSE", "SEMICOLON", "BOOLEAN", "ID", 
                      "NUMBER", "STRING", "WS" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_var_decl = 2
    RULE_var_assign = 3
    RULE_std_output = 4
    RULE_conditional = 5
    RULE_while_loop = 6
    RULE_condition = 7
    RULE_comparison = 8
    RULE_greater_than = 9
    RULE_lower_than = 10
    RULE_equals = 11
    RULE_greater_or_equal_than = 12
    RULE_lower_or_equal_than = 13
    RULE_expression = 14
    RULE_factor = 15
    RULE_exponent = 16
    RULE_term = 17

    ruleNames =  [ "program", "sentence", "var_decl", "var_assign", "std_output", 
                   "conditional", "while_loop", "condition", "comparison", 
                   "greater_than", "lower_than", "equals", "greater_or_equal_than", 
                   "lower_or_equal_than", "expression", "factor", "exponent", 
                   "term" ]

    EOF = Token.EOF
    PROGRAM=1
    VAR=2
    PUTS=3
    IF=4
    ELSE=5
    WHILE=6
    PLUS=7
    MINUS=8
    MULT=9
    DIV=10
    MOD=11
    POW=12
    AND=13
    OR=14
    NOT=15
    GT=16
    LT=17
    GEQ=18
    LEQ=19
    EQ=20
    NEQ=21
    ASSIGN=22
    BRACKET_OPEN=23
    BRACKET_CLOSE=24
    PAR_OPEN=25
    PAR_CLOSE=26
    SEMICOLON=27
    BOOLEAN=28
    ID=29
    NUMBER=30
    STRING=31
    WS=32

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
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 536870940) != 0:
                self.state = 37
                localctx._sentence = self.sentence()
                body.append(localctx._sentence.node)
                self.state = 44
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

        def var_assign(self):
            return self.getTypedRuleContext(ChibchombianoParser.Var_assignContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(ChibchombianoParser.Var_declContext,0)


        def std_output(self):
            return self.getTypedRuleContext(ChibchombianoParser.Std_outputContext,0)


        def conditional(self):
            return self.getTypedRuleContext(ChibchombianoParser.ConditionalContext,0)


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
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                localctx._var_assign = self.var_assign()
                localctx.node =localctx._var_assign.node
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                localctx._var_decl = self.var_decl()
                localctx.node = localctx._var_decl.node
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                localctx._std_output = self.std_output()
                localctx.node = localctx._std_output.node
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                localctx._conditional = self.conditional()
                localctx.node=localctx._conditional.node
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
            self.state = 61
            self.match(ChibchombianoParser.VAR)
            self.state = 62
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
            self.state = 65
            localctx._ID = self.match(ChibchombianoParser.ID)
            self.state = 66
            self.match(ChibchombianoParser.ASSIGN)
            self.state = 67
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
            self.state = 70
            self.match(ChibchombianoParser.PUTS)
            self.state = 71
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
            self._condition = None # ConditionContext
            self.s1 = None # SentenceContext
            self.s2 = None # SentenceContext

        def IF(self):
            return self.getToken(ChibchombianoParser.IF, 0)

        def PAR_OPEN(self):
            return self.getToken(ChibchombianoParser.PAR_OPEN, 0)

        def condition(self):
            return self.getTypedRuleContext(ChibchombianoParser.ConditionContext,0)


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
            self.state = 74
            self.match(ChibchombianoParser.IF)
            self.state = 75
            self.match(ChibchombianoParser.PAR_OPEN)
            self.state = 76
            localctx._condition = self.condition()
            self.state = 77
            self.match(ChibchombianoParser.PAR_CLOSE)
            body=list()
            elseBody=list()
            self.state = 80
            self.match(ChibchombianoParser.BRACKET_OPEN)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 536870940) != 0:
                self.state = 81
                localctx.s1 = self.sentence()
                body.append(localctx.s1.node)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(ChibchombianoParser.BRACKET_CLOSE)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 90
                self.match(ChibchombianoParser.ELSE)
                self.state = 91
                self.match(ChibchombianoParser.BRACKET_OPEN)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 536870940) != 0:
                    self.state = 92
                    localctx.s2 = self.sentence()
                    elseBody.append(localctx.s2.node)
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 100
                self.match(ChibchombianoParser.BRACKET_CLOSE)


            localctx.node = If(localctx._condition.node,body,elseBody)
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
            self._condition = None # ConditionContext
            self.s1 = None # SentenceContext

        def WHILE(self):
            return self.getToken(ChibchombianoParser.WHILE, 0)

        def PAR_OPEN(self):
            return self.getToken(ChibchombianoParser.PAR_OPEN, 0)

        def condition(self):
            return self.getTypedRuleContext(ChibchombianoParser.ConditionContext,0)


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
            self.state = 105
            self.match(ChibchombianoParser.WHILE)
            self.state = 106
            self.match(ChibchombianoParser.PAR_OPEN)
            self.state = 107
            localctx._condition = self.condition()
            self.state = 108
            self.match(ChibchombianoParser.PAR_CLOSE)
            body=list()
            self.state = 110
            self.match(ChibchombianoParser.BRACKET_OPEN)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 536870940) != 0:
                self.state = 111
                localctx.s1 = self.sentence()
                body.append(localctx.s1.node)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(ChibchombianoParser.BRACKET_CLOSE)
            localctx.node = WhileLoop(localctx._condition.node,body)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._comparison = None # ComparisonContext

        def comparison(self):
            return self.getTypedRuleContext(ChibchombianoParser.ComparisonContext,0)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.AND)
            else:
                return self.getToken(ChibchombianoParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ChibchombianoParser.OR)
            else:
                return self.getToken(ChibchombianoParser.OR, i)

        def getRuleIndex(self):
            return ChibchombianoParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = ChibchombianoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            localctx._comparison = self.comparison()
            localctx.node=localctx._comparison.node
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 124
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # Greater_thanContext
            self.e2 = None # Lower_thanContext
            self.e3 = None # EqualsContext
            self.e4 = None # Greater_or_equal_thanContext
            self.e5 = None # Lower_or_equal_thanContext

        def greater_than(self):
            return self.getTypedRuleContext(ChibchombianoParser.Greater_thanContext,0)


        def lower_than(self):
            return self.getTypedRuleContext(ChibchombianoParser.Lower_thanContext,0)


        def equals(self):
            return self.getTypedRuleContext(ChibchombianoParser.EqualsContext,0)


        def greater_or_equal_than(self):
            return self.getTypedRuleContext(ChibchombianoParser.Greater_or_equal_thanContext,0)


        def lower_or_equal_than(self):
            return self.getTypedRuleContext(ChibchombianoParser.Lower_or_equal_thanContext,0)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = ChibchombianoParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 130
                localctx.e1 = self.greater_than()
                localctx.node=localctx.e1.node
                pass

            elif la_ == 2:
                self.state = 133
                localctx.e2 = self.lower_than()
                localctx.node=localctx.e2.node
                pass

            elif la_ == 3:
                self.state = 136
                localctx.e3 = self.equals()
                localctx.node=localctx.e3.node
                pass

            elif la_ == 4:
                self.state = 139
                localctx.e4 = self.greater_or_equal_than()
                localctx.node=localctx.e4.node
                pass

            elif la_ == 5:
                self.state = 142
                localctx.e5 = self.lower_or_equal_than()
                localctx.node=localctx.e5.node
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Greater_thanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def GT(self):
            return self.getToken(ChibchombianoParser.GT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_greater_than

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreater_than" ):
                listener.enterGreater_than(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreater_than" ):
                listener.exitGreater_than(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreater_than" ):
                return visitor.visitGreater_than(self)
            else:
                return visitor.visitChildren(self)




    def greater_than(self):

        localctx = ChibchombianoParser.Greater_thanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_greater_than)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            localctx.e1 = self.expression()
            self.state = 148
            self.match(ChibchombianoParser.GT)
            self.state = 149
            localctx.e2 = self.expression()
            localctx.node=GreaterThan(localctx.e1.node,localctx.e2.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lower_thanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def LT(self):
            return self.getToken(ChibchombianoParser.LT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_lower_than

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLower_than" ):
                listener.enterLower_than(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLower_than" ):
                listener.exitLower_than(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLower_than" ):
                return visitor.visitLower_than(self)
            else:
                return visitor.visitChildren(self)




    def lower_than(self):

        localctx = ChibchombianoParser.Lower_thanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_lower_than)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            localctx.e1 = self.expression()
            self.state = 153
            self.match(ChibchombianoParser.LT)
            self.state = 154
            localctx.e2 = self.expression()
            localctx.node=LowerThan(localctx.e1.node,localctx.e2.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def EQ(self):
            return self.getToken(ChibchombianoParser.EQ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_equals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquals" ):
                listener.enterEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquals" ):
                listener.exitEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquals" ):
                return visitor.visitEquals(self)
            else:
                return visitor.visitChildren(self)




    def equals(self):

        localctx = ChibchombianoParser.EqualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_equals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            localctx.e1 = self.expression()
            self.state = 158
            self.match(ChibchombianoParser.EQ)
            self.state = 159
            localctx.e2 = self.expression()
            localctx.node=Equals(localctx.e1.node,localctx.e2.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Greater_or_equal_thanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def GEQ(self):
            return self.getToken(ChibchombianoParser.GEQ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_greater_or_equal_than

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreater_or_equal_than" ):
                listener.enterGreater_or_equal_than(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreater_or_equal_than" ):
                listener.exitGreater_or_equal_than(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreater_or_equal_than" ):
                return visitor.visitGreater_or_equal_than(self)
            else:
                return visitor.visitChildren(self)




    def greater_or_equal_than(self):

        localctx = ChibchombianoParser.Greater_or_equal_thanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_greater_or_equal_than)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            localctx.e1 = self.expression()
            self.state = 163
            self.match(ChibchombianoParser.GEQ)
            self.state = 164
            localctx.e2 = self.expression()
            localctx.node=GreaterOrEqualThan(localctx.e1.node,localctx.e2.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lower_or_equal_thanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def LEQ(self):
            return self.getToken(ChibchombianoParser.LEQ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ChibchombianoParser.RULE_lower_or_equal_than

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLower_or_equal_than" ):
                listener.enterLower_or_equal_than(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLower_or_equal_than" ):
                listener.exitLower_or_equal_than(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLower_or_equal_than" ):
                return visitor.visitLower_or_equal_than(self)
            else:
                return visitor.visitChildren(self)




    def lower_or_equal_than(self):

        localctx = ChibchombianoParser.Lower_or_equal_thanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lower_or_equal_than)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            localctx.e1 = self.expression()
            self.state = 168
            self.match(ChibchombianoParser.LEQ)
            self.state = 169
            localctx.e2 = self.expression()
            localctx.node=LowerOrEqualThan(localctx.e1.node,localctx.e2.node)
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
        self.enterRule(localctx, 28, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            localctx.t1 = self.factor()
            localctx.node= localctx.t1.node
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 182
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 174
                    self.match(ChibchombianoParser.PLUS)
                    self.state = 175
                    localctx.t2 = self.factor()
                    localctx.node= Addition(localctx.node,localctx.t2.node)
                    pass
                elif token in [8]:
                    self.state = 178
                    self.match(ChibchombianoParser.MINUS)
                    self.state = 179
                    localctx.t3 = self.factor()
                    localctx.node = Substraction(localctx.node,localctx.t3.node)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 186
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
        self.enterRule(localctx, 30, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            localctx.t1 = self.exponent()
            localctx.node = localctx.t1.node 
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0:
                self.state = 201
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9]:
                    self.state = 189
                    self.match(ChibchombianoParser.MULT)
                    self.state = 190
                    localctx.t2 = self.exponent()
                    localctx.node = Multiplication(localctx.node, localctx.t2.node)
                    pass
                elif token in [10]:
                    self.state = 193
                    self.match(ChibchombianoParser.DIV)
                    self.state = 194
                    localctx.t3 = self.exponent()
                    localctx.node = Division(localctx.node,localctx.t3.node)
                    pass
                elif token in [11]:
                    self.state = 197
                    self.match(ChibchombianoParser.MOD)
                    self.state = 198
                    localctx.t4 = self.exponent()
                    localctx.node =  Module(localctx.node,localctx.t4.node)
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
        self.enterRule(localctx, 32, self.RULE_exponent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            localctx.t1 = self.term()
            localctx.node=localctx.t1.node
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 208
                self.match(ChibchombianoParser.POW)
                self.state = 209
                localctx.t2 = self.term()
                localctx.node = Exponent(localctx.node,localctx.t2.node)
                self.state = 216
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
        self.enterRule(localctx, 34, self.RULE_term)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                localctx._NUMBER = self.match(ChibchombianoParser.NUMBER)

                splitted = (None if localctx._NUMBER is None else localctx._NUMBER.text).split(".") 
                if len(splitted)==1:
                        localctx.node = Constant(int((None if localctx._NUMBER is None else localctx._NUMBER.text)))
                elif len(splitted)==2:
                        localctx.node = Constant(float((None if localctx._NUMBER is None else localctx._NUMBER.text)))

                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                localctx._ID = self.match(ChibchombianoParser.ID)
                localctx.node = VarRef((None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                localctx._BOOLEAN = self.match(ChibchombianoParser.BOOLEAN)

                put_bool=lambda x: x=="true"
                localctx.node= Constant(put_bool((None if localctx._BOOLEAN is None else localctx._BOOLEAN.text)))
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.match(ChibchombianoParser.PAR_OPEN)
                self.state = 224
                localctx._expression = self.expression()
                self.state = 225
                self.match(ChibchombianoParser.PAR_CLOSE)
                localctx.node=localctx._expression.node
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






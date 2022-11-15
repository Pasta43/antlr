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
        4,1,32,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,
        8,90,8,8,10,8,12,8,93,9,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,101,8,8,10,
        8,12,8,104,9,8,1,8,3,8,107,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,5,9,120,8,9,10,9,12,9,123,9,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,138,8,10,10,10,12,10,
        141,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,5,11,157,8,11,10,11,12,11,160,9,11,1,12,1,12,1,12,
        1,12,1,12,1,12,5,12,168,8,12,10,12,12,12,171,9,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,184,8,13,1,13,0,0,14,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,0,188,0,28,1,0,0,0,2,51,1,
        0,0,0,4,53,1,0,0,0,6,57,1,0,0,0,8,62,1,0,0,0,10,66,1,0,0,0,12,70,
        1,0,0,0,14,75,1,0,0,0,16,79,1,0,0,0,18,110,1,0,0,0,20,127,1,0,0,
        0,22,142,1,0,0,0,24,161,1,0,0,0,26,183,1,0,0,0,28,34,6,0,-1,0,29,
        30,3,2,1,0,30,31,6,0,-1,0,31,33,1,0,0,0,32,29,1,0,0,0,33,36,1,0,
        0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,
        6,0,-1,0,38,1,1,0,0,0,39,40,3,12,6,0,40,41,6,1,-1,0,41,52,1,0,0,
        0,42,43,3,4,2,0,43,44,6,1,-1,0,44,52,1,0,0,0,45,46,3,14,7,0,46,47,
        6,1,-1,0,47,52,1,0,0,0,48,49,3,16,8,0,49,50,6,1,-1,0,50,52,1,0,0,
        0,51,39,1,0,0,0,51,42,1,0,0,0,51,45,1,0,0,0,51,48,1,0,0,0,52,3,1,
        0,0,0,53,54,5,2,0,0,54,55,5,29,0,0,55,56,6,2,-1,0,56,5,1,0,0,0,57,
        58,3,20,10,0,58,59,5,16,0,0,59,60,3,20,10,0,60,61,6,3,-1,0,61,7,
        1,0,0,0,62,63,3,20,10,0,63,64,5,17,0,0,64,65,3,20,10,0,65,9,1,0,
        0,0,66,67,3,20,10,0,67,68,5,20,0,0,68,69,3,20,10,0,69,11,1,0,0,0,
        70,71,5,29,0,0,71,72,5,22,0,0,72,73,3,20,10,0,73,74,6,6,-1,0,74,
        13,1,0,0,0,75,76,5,3,0,0,76,77,3,20,10,0,77,78,6,7,-1,0,78,15,1,
        0,0,0,79,80,5,4,0,0,80,81,5,25,0,0,81,82,3,20,10,0,82,83,5,26,0,
        0,83,84,6,8,-1,0,84,85,6,8,-1,0,85,91,5,23,0,0,86,87,3,2,1,0,87,
        88,6,8,-1,0,88,90,1,0,0,0,89,86,1,0,0,0,90,93,1,0,0,0,91,89,1,0,
        0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,1,0,0,0,94,106,5,24,0,0,95,
        96,5,5,0,0,96,102,5,23,0,0,97,98,3,2,1,0,98,99,6,8,-1,0,99,101,1,
        0,0,0,100,97,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,
        0,0,103,105,1,0,0,0,104,102,1,0,0,0,105,107,5,24,0,0,106,95,1,0,
        0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,6,8,-1,0,109,17,1,0,
        0,0,110,111,5,6,0,0,111,112,5,25,0,0,112,113,3,20,10,0,113,114,5,
        26,0,0,114,115,6,9,-1,0,115,121,5,23,0,0,116,117,3,2,1,0,117,118,
        6,9,-1,0,118,120,1,0,0,0,119,116,1,0,0,0,120,123,1,0,0,0,121,119,
        1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,
        5,24,0,0,125,126,6,9,-1,0,126,19,1,0,0,0,127,128,3,22,11,0,128,139,
        6,10,-1,0,129,130,5,7,0,0,130,131,3,22,11,0,131,132,6,10,-1,0,132,
        138,1,0,0,0,133,134,5,8,0,0,134,135,3,22,11,0,135,136,6,10,-1,0,
        136,138,1,0,0,0,137,129,1,0,0,0,137,133,1,0,0,0,138,141,1,0,0,0,
        139,137,1,0,0,0,139,140,1,0,0,0,140,21,1,0,0,0,141,139,1,0,0,0,142,
        143,3,24,12,0,143,158,6,11,-1,0,144,145,5,9,0,0,145,146,3,24,12,
        0,146,147,6,11,-1,0,147,157,1,0,0,0,148,149,5,10,0,0,149,150,3,24,
        12,0,150,151,6,11,-1,0,151,157,1,0,0,0,152,153,5,11,0,0,153,154,
        3,24,12,0,154,155,6,11,-1,0,155,157,1,0,0,0,156,144,1,0,0,0,156,
        148,1,0,0,0,156,152,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,
        159,1,0,0,0,159,23,1,0,0,0,160,158,1,0,0,0,161,162,3,26,13,0,162,
        169,6,12,-1,0,163,164,5,12,0,0,164,165,3,26,13,0,165,166,6,12,-1,
        0,166,168,1,0,0,0,167,163,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,
        0,169,170,1,0,0,0,170,25,1,0,0,0,171,169,1,0,0,0,172,173,5,30,0,
        0,173,184,6,13,-1,0,174,175,5,29,0,0,175,184,6,13,-1,0,176,177,5,
        28,0,0,177,184,6,13,-1,0,178,179,5,25,0,0,179,180,3,20,10,0,180,
        181,5,26,0,0,181,182,6,13,-1,0,182,184,1,0,0,0,183,172,1,0,0,0,183,
        174,1,0,0,0,183,176,1,0,0,0,183,178,1,0,0,0,184,27,1,0,0,0,12,34,
        51,91,102,106,121,137,139,156,158,169,183
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
    RULE_greater_than = 3
    RULE_lower_than = 4
    RULE_equals = 5
    RULE_var_assign = 6
    RULE_std_output = 7
    RULE_conditional = 8
    RULE_while_loop = 9
    RULE_expression = 10
    RULE_factor = 11
    RULE_exponent = 12
    RULE_term = 13

    ruleNames =  [ "program", "sentence", "var_decl", "greater_than", "lower_than", 
                   "equals", "var_assign", "std_output", "conditional", 
                   "while_loop", "expression", "factor", "exponent", "term" ]

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
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 536870940) != 0:
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                localctx._var_assign = self.var_assign()
                localctx.node =localctx._var_assign.node
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                localctx._var_decl = self.var_decl()
                localctx.node = localctx._var_decl.node
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                localctx._std_output = self.std_output()
                localctx.node = localctx._std_output.node
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
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
            self.state = 53
            self.match(ChibchombianoParser.VAR)
            self.state = 54
            localctx._ID = self.match(ChibchombianoParser.ID)

            localctx.node = VarDecl((None if localctx._ID is None else localctx._ID.text))

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
        self.enterRule(localctx, 6, self.RULE_greater_than)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            localctx.e1 = self.expression()
            self.state = 58
            self.match(ChibchombianoParser.GT)
            self.state = 59
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
        self.enterRule(localctx, 8, self.RULE_lower_than)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            localctx.e1 = self.expression()
            self.state = 63
            self.match(ChibchombianoParser.LT)
            self.state = 64
            localctx.e2 = self.expression()
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
        self.enterRule(localctx, 10, self.RULE_equals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            localctx.e1 = self.expression()
            self.state = 67
            self.match(ChibchombianoParser.EQ)
            self.state = 68
            localctx.e2 = self.expression()
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
        self.enterRule(localctx, 12, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            localctx._ID = self.match(ChibchombianoParser.ID)
            self.state = 71
            self.match(ChibchombianoParser.ASSIGN)
            self.state = 72
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
        self.enterRule(localctx, 14, self.RULE_std_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ChibchombianoParser.PUTS)
            self.state = 76
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
        self.enterRule(localctx, 16, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ChibchombianoParser.IF)
            self.state = 80
            self.match(ChibchombianoParser.PAR_OPEN)
            self.state = 81
            localctx._expression = self.expression()
            self.state = 82
            self.match(ChibchombianoParser.PAR_CLOSE)
            body=list()
            elseBody=list()
            self.state = 85
            self.match(ChibchombianoParser.BRACKET_OPEN)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 536870940) != 0:
                self.state = 86
                localctx.s1 = self.sentence()
                body.append(localctx.s1.node)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(ChibchombianoParser.BRACKET_CLOSE)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 95
                self.match(ChibchombianoParser.ELSE)
                self.state = 96
                self.match(ChibchombianoParser.BRACKET_OPEN)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 536870940) != 0:
                    self.state = 97
                    localctx.s2 = self.sentence()
                    elseBody.append(localctx.s2.node)
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 105
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
        self.enterRule(localctx, 18, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ChibchombianoParser.WHILE)
            self.state = 111
            self.match(ChibchombianoParser.PAR_OPEN)
            self.state = 112
            localctx._expression = self.expression()
            self.state = 113
            self.match(ChibchombianoParser.PAR_CLOSE)
            body=list()
            self.state = 115
            self.match(ChibchombianoParser.BRACKET_OPEN)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 536870940) != 0:
                self.state = 116
                localctx.s1 = self.sentence()
                body.append(localctx.s1.node)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
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
        self.enterRule(localctx, 20, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            localctx.t1 = self.factor()
            localctx.node= localctx.t1.node
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 137
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 129
                    self.match(ChibchombianoParser.PLUS)
                    self.state = 130
                    localctx.t2 = self.factor()
                    localctx.node= Addition(localctx.node,localctx.t2.node)
                    pass
                elif token in [8]:
                    self.state = 133
                    self.match(ChibchombianoParser.MINUS)
                    self.state = 134
                    localctx.t3 = self.factor()
                    localctx.node -= localctx.t3.node
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 141
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
        self.enterRule(localctx, 22, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            localctx.t1 = self.exponent()
            localctx.node = localctx.t1.node 
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0:
                self.state = 156
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9]:
                    self.state = 144
                    self.match(ChibchombianoParser.MULT)
                    self.state = 145
                    localctx.t2 = self.exponent()
                    localctx.node = Multiplication(localctx.node, localctx.t2.node)
                    pass
                elif token in [10]:
                    self.state = 148
                    self.match(ChibchombianoParser.DIV)
                    self.state = 149
                    localctx.t3 = self.exponent()
                    localctx.node /= localctx.t3.node
                    pass
                elif token in [11]:
                    self.state = 152
                    self.match(ChibchombianoParser.MOD)
                    self.state = 153
                    localctx.t4 = self.exponent()
                    localctx.node %=  localctx.t4.node
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 160
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
        self.enterRule(localctx, 24, self.RULE_exponent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            localctx.t1 = self.term()
            localctx.node=localctx.t1.node
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 163
                self.match(ChibchombianoParser.POW)
                self.state = 164
                localctx.t2 = self.term()
                localctx.node = Exponent(localctx.node,localctx.t2.node)
                self.state = 171
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
        self.enterRule(localctx, 26, self.RULE_term)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                localctx._NUMBER = self.match(ChibchombianoParser.NUMBER)

                splitted = (None if localctx._NUMBER is None else localctx._NUMBER.text).split(".") 
                if len(splitted)==1:
                        localctx.node = Constant(int((None if localctx._NUMBER is None else localctx._NUMBER.text)))
                elif len(splitted)==2:
                        localctx.node = Constant(float((None if localctx._NUMBER is None else localctx._NUMBER.text)))

                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                localctx._ID = self.match(ChibchombianoParser.ID)
                localctx.node = VarRef((None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                localctx._BOOLEAN = self.match(ChibchombianoParser.BOOLEAN)

                put_bool=lambda x: x=="true"
                localctx.node= Constant(put_bool((None if localctx._BOOLEAN is None else localctx._BOOLEAN.text)))
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.match(ChibchombianoParser.PAR_OPEN)
                self.state = 179
                localctx._expression = self.expression()
                self.state = 180
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






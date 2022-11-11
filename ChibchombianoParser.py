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

def serializedATN():
    return [
        4,1,28,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,56,8,5,10,5,
        12,5,59,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,5,6,75,8,6,10,6,12,6,78,9,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,86,8,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,97,8,8,1,8,0,0,9,0,2,4,
        6,8,10,12,14,16,0,0,100,0,21,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,
        34,1,0,0,0,8,40,1,0,0,0,10,45,1,0,0,0,12,60,1,0,0,0,14,79,1,0,0,
        0,16,96,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,21,1,0,0,0,24,28,3,4,2,0,25,
        28,3,6,3,0,26,28,3,8,4,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,
        0,28,3,1,0,0,0,29,30,5,2,0,0,30,31,5,25,0,0,31,32,5,24,0,0,32,33,
        6,2,-1,0,33,5,1,0,0,0,34,35,5,25,0,0,35,36,5,19,0,0,36,37,3,10,5,
        0,37,38,5,24,0,0,38,39,6,3,-1,0,39,7,1,0,0,0,40,41,5,3,0,0,41,42,
        3,10,5,0,42,43,5,24,0,0,43,44,6,4,-1,0,44,9,1,0,0,0,45,46,3,12,6,
        0,46,57,6,5,-1,0,47,48,5,4,0,0,48,49,3,12,6,0,49,50,6,5,-1,0,50,
        56,1,0,0,0,51,52,5,5,0,0,52,53,3,12,6,0,53,54,6,5,-1,0,54,56,1,0,
        0,0,55,47,1,0,0,0,55,51,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,
        1,0,0,0,58,11,1,0,0,0,59,57,1,0,0,0,60,61,3,14,7,0,61,76,6,6,-1,
        0,62,63,5,6,0,0,63,64,3,14,7,0,64,65,6,6,-1,0,65,75,1,0,0,0,66,67,
        5,7,0,0,67,68,3,14,7,0,68,69,6,6,-1,0,69,75,1,0,0,0,70,71,5,8,0,
        0,71,72,3,14,7,0,72,73,6,6,-1,0,73,75,1,0,0,0,74,62,1,0,0,0,74,66,
        1,0,0,0,74,70,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,
        77,13,1,0,0,0,78,76,1,0,0,0,79,80,3,16,8,0,80,85,6,7,-1,0,81,82,
        5,9,0,0,82,83,3,16,8,0,83,84,6,7,-1,0,84,86,1,0,0,0,85,81,1,0,0,
        0,85,86,1,0,0,0,86,15,1,0,0,0,87,88,5,26,0,0,88,97,6,8,-1,0,89,90,
        5,25,0,0,90,97,6,8,-1,0,91,92,5,22,0,0,92,93,3,10,5,0,93,94,5,23,
        0,0,94,95,6,8,-1,0,95,97,1,0,0,0,96,87,1,0,0,0,96,89,1,0,0,0,96,
        91,1,0,0,0,97,17,1,0,0,0,8,21,27,55,57,74,76,85,96
    ]

class ChibchombianoParser ( Parser ):

    grammarFileName = "Chibchombiano.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'var'", "'puts'", "'+'", 
                     "'-'", "'*'", "'/'", "'mod'", "'^'", "'and'", "'or'", 
                     "'not'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'='", "'{'", "'}'", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "VAR", "PUTS", "PLUS", "MINUS", 
                      "MULT", "DIV", "MOD", "POW", "AND", "OR", "NOT", "GT", 
                      "LT", "GEQ", "LEQ", "EQ", "NEQ", "ASSIGN", "BRACKET_OPEN", 
                      "BRACKET_CLOSE", "PAR_OPEN", "PAR_CLOSE", "SEMICOLON", 
                      "ID", "NUMBER", "STRING", "WS" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_var_decl = 2
    RULE_var_assign = 3
    RULE_std_output = 4
    RULE_expression = 5
    RULE_factor = 6
    RULE_exponent = 7
    RULE_term = 8

    ruleNames =  [ "program", "sentence", "var_decl", "var_assign", "std_output", 
                   "expression", "factor", "exponent", "term" ]

    EOF = Token.EOF
    PROGRAM=1
    VAR=2
    PUTS=3
    PLUS=4
    MINUS=5
    MULT=6
    DIV=7
    MOD=8
    POW=9
    AND=10
    OR=11
    NOT=12
    GT=13
    LT=14
    GEQ=15
    LEQ=16
    EQ=17
    NEQ=18
    ASSIGN=19
    BRACKET_OPEN=20
    BRACKET_CLOSE=21
    PAR_OPEN=22
    PAR_CLOSE=23
    SEMICOLON=24
    ID=25
    NUMBER=26
    STRING=27
    WS=28

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 33554444) != 0:
                self.state = 18
                self.sentence()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def var_decl(self):
            return self.getTypedRuleContext(ChibchombianoParser.Var_declContext,0)


        def var_assign(self):
            return self.getTypedRuleContext(ChibchombianoParser.Var_assignContext,0)


        def std_output(self):
            return self.getTypedRuleContext(ChibchombianoParser.Std_outputContext,0)


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
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.var_decl()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.var_assign()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.std_output()
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
            self._ID = None # Token

        def VAR(self):
            return self.getToken(ChibchombianoParser.VAR, 0)

        def ID(self):
            return self.getToken(ChibchombianoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(ChibchombianoParser.SEMICOLON, 0)

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
            self.state = 29
            self.match(ChibchombianoParser.VAR)
            self.state = 30
            localctx._ID = self.match(ChibchombianoParser.ID)
            self.state = 31
            self.match(ChibchombianoParser.SEMICOLON)

            dictionary_symbols[(None if localctx._ID is None else localctx._ID.text)]=""

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
            self._ID = None # Token
            self._expression = None # ExpressionContext

        def ID(self):
            return self.getToken(ChibchombianoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ChibchombianoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(ChibchombianoParser.SEMICOLON, 0)

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
            self.state = 34
            localctx._ID = self.match(ChibchombianoParser.ID)
            self.state = 35
            self.match(ChibchombianoParser.ASSIGN)
            self.state = 36
            localctx._expression = self.expression()
            self.state = 37
            self.match(ChibchombianoParser.SEMICOLON)
            dictionary_symbols[(None if localctx._ID is None else localctx._ID.text)]=localctx._expression.value
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
            self._expression = None # ExpressionContext

        def PUTS(self):
            return self.getToken(ChibchombianoParser.PUTS, 0)

        def expression(self):
            return self.getTypedRuleContext(ChibchombianoParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(ChibchombianoParser.SEMICOLON, 0)

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
            self.state = 40
            self.match(ChibchombianoParser.PUTS)
            self.state = 41
            localctx._expression = self.expression()
            self.state = 42
            self.match(ChibchombianoParser.SEMICOLON)
            print(localctx._expression.value)
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
            self.value = None
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
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            localctx.t1 = self.factor()
            localctx.value= localctx.t1.value
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 47
                    self.match(ChibchombianoParser.PLUS)
                    self.state = 48
                    localctx.t2 = self.factor()
                    localctx.value+= localctx.t2.value
                    pass
                elif token in [5]:
                    self.state = 51
                    self.match(ChibchombianoParser.MINUS)
                    self.state = 52
                    localctx.t3 = self.factor()
                    localctx.value -= localctx.t3.value
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 59
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
            self.value = None
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
        self.enterRule(localctx, 12, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            localctx.t1 = self.exponent()
            localctx.value = localctx.t1.value 
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0:
                self.state = 74
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 62
                    self.match(ChibchombianoParser.MULT)
                    self.state = 63
                    localctx.t2 = self.exponent()
                    localctx.value *= localctx.t2.value
                    pass
                elif token in [7]:
                    self.state = 66
                    self.match(ChibchombianoParser.DIV)
                    self.state = 67
                    localctx.t3 = self.exponent()
                    localctx.value /= localctx.t3.value
                    pass
                elif token in [8]:
                    self.state = 70
                    self.match(ChibchombianoParser.MOD)
                    self.state = 71
                    localctx.t4 = self.exponent()
                    localctx.value %=  localctx.t4.value
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 78
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
            self.value = None
            self.t1 = None # TermContext
            self.t2 = None # TermContext

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChibchombianoParser.TermContext)
            else:
                return self.getTypedRuleContext(ChibchombianoParser.TermContext,i)


        def POW(self):
            return self.getToken(ChibchombianoParser.POW, 0)

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
        self.enterRule(localctx, 14, self.RULE_exponent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            localctx.t1 = self.term()
            localctx.value=localctx.t1.value
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 81
                self.match(ChibchombianoParser.POW)
                self.state = 82
                localctx.t2 = self.term()
                localctx.value = localctx.value**localctx.t2.value


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
            self.value = None
            self._NUMBER = None # Token
            self._ID = None # Token
            self._expression = None # ExpressionContext

        def NUMBER(self):
            return self.getToken(ChibchombianoParser.NUMBER, 0)

        def ID(self):
            return self.getToken(ChibchombianoParser.ID, 0)

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
        self.enterRule(localctx, 16, self.RULE_term)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                localctx._NUMBER = self.match(ChibchombianoParser.NUMBER)

                splitted = (None if localctx._NUMBER is None else localctx._NUMBER.text).split(".") 
                if len(splitted)==1:
                        localctx.value = int((None if localctx._NUMBER is None else localctx._NUMBER.text))
                elif len(splitted)==2:
                        localctx.value = float((None if localctx._NUMBER is None else localctx._NUMBER.text))

                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                localctx._ID = self.match(ChibchombianoParser.ID)
                localctx.value = dictionary_symbols.get((None if localctx._ID is None else localctx._ID.text),None)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(ChibchombianoParser.PAR_OPEN)
                self.state = 92
                localctx._expression = self.expression()
                self.state = 93
                self.match(ChibchombianoParser.PAR_CLOSE)
                localctx.value=localctx._expression.value
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






# Generated from Chibchombiano.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ChibchombianoParser import ChibchombianoParser
else:
    from ChibchombianoParser import ChibchombianoParser
 
import numpy as np
dictionary_symbols = dict()  


# This class defines a complete listener for a parse tree produced by ChibchombianoParser.
class ChibchombianoListener(ParseTreeListener):

    # Enter a parse tree produced by ChibchombianoParser#program.
    def enterProgram(self, ctx:ChibchombianoParser.ProgramContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#program.
    def exitProgram(self, ctx:ChibchombianoParser.ProgramContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#sentence.
    def enterSentence(self, ctx:ChibchombianoParser.SentenceContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#sentence.
    def exitSentence(self, ctx:ChibchombianoParser.SentenceContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#var_decl.
    def enterVar_decl(self, ctx:ChibchombianoParser.Var_declContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#var_decl.
    def exitVar_decl(self, ctx:ChibchombianoParser.Var_declContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#var_assign.
    def enterVar_assign(self, ctx:ChibchombianoParser.Var_assignContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#var_assign.
    def exitVar_assign(self, ctx:ChibchombianoParser.Var_assignContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#std_output.
    def enterStd_output(self, ctx:ChibchombianoParser.Std_outputContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#std_output.
    def exitStd_output(self, ctx:ChibchombianoParser.Std_outputContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#expression.
    def enterExpression(self, ctx:ChibchombianoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#expression.
    def exitExpression(self, ctx:ChibchombianoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#factor.
    def enterFactor(self, ctx:ChibchombianoParser.FactorContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#factor.
    def exitFactor(self, ctx:ChibchombianoParser.FactorContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#exponent.
    def enterExponent(self, ctx:ChibchombianoParser.ExponentContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#exponent.
    def exitExponent(self, ctx:ChibchombianoParser.ExponentContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#term.
    def enterTerm(self, ctx:ChibchombianoParser.TermContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#term.
    def exitTerm(self, ctx:ChibchombianoParser.TermContext):
        pass



del ChibchombianoParser
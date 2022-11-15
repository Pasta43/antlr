# Generated from Chibchombiano.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ChibchombianoParser import ChibchombianoParser
else:
    from ChibchombianoParser import ChibchombianoParser
 
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


    # Enter a parse tree produced by ChibchombianoParser#greater_than.
    def enterGreater_than(self, ctx:ChibchombianoParser.Greater_thanContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#greater_than.
    def exitGreater_than(self, ctx:ChibchombianoParser.Greater_thanContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#lower_than.
    def enterLower_than(self, ctx:ChibchombianoParser.Lower_thanContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#lower_than.
    def exitLower_than(self, ctx:ChibchombianoParser.Lower_thanContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#equals.
    def enterEquals(self, ctx:ChibchombianoParser.EqualsContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#equals.
    def exitEquals(self, ctx:ChibchombianoParser.EqualsContext):
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


    # Enter a parse tree produced by ChibchombianoParser#conditional.
    def enterConditional(self, ctx:ChibchombianoParser.ConditionalContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#conditional.
    def exitConditional(self, ctx:ChibchombianoParser.ConditionalContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#while_loop.
    def enterWhile_loop(self, ctx:ChibchombianoParser.While_loopContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#while_loop.
    def exitWhile_loop(self, ctx:ChibchombianoParser.While_loopContext):
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
# Generated from Chibchombiano.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ChibchombianoParser import ChibchombianoParser
else:
    from ChibchombianoParser import ChibchombianoParser
 
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


    # Enter a parse tree produced by ChibchombianoParser#or_expression.
    def enterOr_expression(self, ctx:ChibchombianoParser.Or_expressionContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#or_expression.
    def exitOr_expression(self, ctx:ChibchombianoParser.Or_expressionContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#and_expression.
    def enterAnd_expression(self, ctx:ChibchombianoParser.And_expressionContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#and_expression.
    def exitAnd_expression(self, ctx:ChibchombianoParser.And_expressionContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#not_expression.
    def enterNot_expression(self, ctx:ChibchombianoParser.Not_expressionContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#not_expression.
    def exitNot_expression(self, ctx:ChibchombianoParser.Not_expressionContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#logical_expression.
    def enterLogical_expression(self, ctx:ChibchombianoParser.Logical_expressionContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#logical_expression.
    def exitLogical_expression(self, ctx:ChibchombianoParser.Logical_expressionContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#sum.
    def enterSum(self, ctx:ChibchombianoParser.SumContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#sum.
    def exitSum(self, ctx:ChibchombianoParser.SumContext):
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


    # Enter a parse tree produced by ChibchombianoParser#function.
    def enterFunction(self, ctx:ChibchombianoParser.FunctionContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#function.
    def exitFunction(self, ctx:ChibchombianoParser.FunctionContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#arguments.
    def enterArguments(self, ctx:ChibchombianoParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#arguments.
    def exitArguments(self, ctx:ChibchombianoParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by ChibchombianoParser#array.
    def enterArray(self, ctx:ChibchombianoParser.ArrayContext):
        pass

    # Exit a parse tree produced by ChibchombianoParser#array.
    def exitArray(self, ctx:ChibchombianoParser.ArrayContext):
        pass



del ChibchombianoParser
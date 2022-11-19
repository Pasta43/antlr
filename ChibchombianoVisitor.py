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


# This class defines a complete generic visitor for a parse tree produced by ChibchombianoParser.

class ChibchombianoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ChibchombianoParser#program.
    def visitProgram(self, ctx:ChibchombianoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#sentence.
    def visitSentence(self, ctx:ChibchombianoParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#var_decl.
    def visitVar_decl(self, ctx:ChibchombianoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#var_assign.
    def visitVar_assign(self, ctx:ChibchombianoParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#std_output.
    def visitStd_output(self, ctx:ChibchombianoParser.Std_outputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#conditional.
    def visitConditional(self, ctx:ChibchombianoParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#while_loop.
    def visitWhile_loop(self, ctx:ChibchombianoParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#expression.
    def visitExpression(self, ctx:ChibchombianoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#logical_expression.
    def visitLogical_expression(self, ctx:ChibchombianoParser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#sum.
    def visitSum(self, ctx:ChibchombianoParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#factor.
    def visitFactor(self, ctx:ChibchombianoParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#exponent.
    def visitExponent(self, ctx:ChibchombianoParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#term.
    def visitTerm(self, ctx:ChibchombianoParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChibchombianoParser#array.
    def visitArray(self, ctx:ChibchombianoParser.ArrayContext):
        return self.visitChildren(ctx)



del ChibchombianoParser
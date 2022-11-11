# Generated from Chibchombiano.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ChibchombianoParser import ChibchombianoParser
else:
    from ChibchombianoParser import ChibchombianoParser
 
import numpy as np
dictionary_symbols = dict()  


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


    # Visit a parse tree produced by ChibchombianoParser#expression.
    def visitExpression(self, ctx:ChibchombianoParser.ExpressionContext):
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



del ChibchombianoParser
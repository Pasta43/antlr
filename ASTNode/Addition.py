import numpy as np
from ASTNode.ASTNode import ASTNode
class Addition(ASTNode):
    def __init__(self,n1:ASTNode,n2:ASTNode):
        """
            Constructor of addition class

            Params:
            n1: operand1
            n2: operand2
        """
        self.n1=n1
        self.n2=n2

    def execute(self,symbolTable:list):
        exprLeft=self.n1.execute(symbolTable)
        exprRight=self.n2.execute(symbolTable)
        if type(exprLeft)== list and type(exprRight) == list:
            exprLeft=np.matrix(exprLeft)
            exprRight=np.matrix(exprRight)
        return exprLeft + exprRight
import numpy as np

from ASTNode.ASTNode import ASTNode
class Arguments(ASTNode):
    def __init__(self):
        """
            Constructor of arguments class
        """
        self.arr= list()

    def execute(self,symbolTable:list):
        return [i.execute(symbolTable) for i in self.arr]
    
    def add(self,element:ASTNode):
        self.arr.append(element)
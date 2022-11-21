import numpy as np

from ASTNode.ASTNode import ASTNode
from ASTNode.Constant import Constant
class Array(ASTNode):
    def __init__(self):
        """
            Constructor of array class
        """
        self.arr= list()

    def execute(self,symbolTable:list):
        return [i.execute(symbolTable) for i in self.arr]
    
    def add(self,element:ASTNode):
        self.arr.append(element)
    def arange(self,n1,n2,n3):
        if n2 is None:
            arr=np.arange(float(n1.text),float(n3.text)+1).tolist()
            [self.add(Constant(a)) for a in arr]
        else:
            arr=np.arange(float(n1.text),float(n3.text)+1,float(n2.text)).tolist()
            [self.add(Constant(a)) for a in arr]
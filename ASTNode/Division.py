from ASTNode.ASTNode import ASTNode
class Division(ASTNode):
    def __init__(self,n1:ASTNode,n2:ASTNode):
        """
            Constructor of division class

            Params:
            n1: operand1
            n2: operand2
        """
        self.n1=n1
        self.n2=n2

    def execute(self,symbolTable:list):
        return self.n1.execute(symbolTable) / self.n2.execute(symbolTable)
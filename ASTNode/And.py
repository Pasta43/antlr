from ASTNode.ASTNode import ASTNode
class And(ASTNode):
    def __init__(self,e1:ASTNode,e2:ASTNode):
        """
            Constructor of AND class

            Params:
            e1: expr1
            e2: expr2
        """
        self.e1=e1
        self.e2=e2

    def execute(self,symbolTable:list):
        return self.e1.execute(symbolTable) and self.e2.execute(symbolTable)
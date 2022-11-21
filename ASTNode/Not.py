from ASTNode.ASTNode import ASTNode
class Not(ASTNode):
    def __init__(self,e1:ASTNode):
        """
            Constructor of NOT class

            Params:
            e1: expr1
        """
        self.e1=e1

    def execute(self,symbolTable:list):
        return not self.e1.execute(symbolTable)
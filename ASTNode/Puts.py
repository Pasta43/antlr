from ASTNode.ASTNode import ASTNode
class Puts(ASTNode):
    def __init__(self,data:ASTNode):
        """
            Constructor of console output class

            Params:
            data: node
        """
        self.data=data

    def execute(self,symbolTable:list):
        print(self.data.execute(symbolTable))
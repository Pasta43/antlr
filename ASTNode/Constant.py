from ASTNode.ASTNode import ASTNode
class Constant(ASTNode):
    def __init__(self,value):
        """
            Constructor of constant value class

            Params:
            value: integer, float or bool
        """
        self.value=value

    def execute(self,symbolTable:list):
        return self.value
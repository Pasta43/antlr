from ASTNode.ASTNode import ASTNode
class VarDecl(ASTNode):
    def __init__(self,name:str):
        """
            Constructor of multiplication class

            Params:
            name: variable name
        """
        self.name=name

    def execute(self,symbolTable:list):
        symbolTable[self.name]="" 
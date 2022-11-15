from ASTNode.ASTNode import ASTNode
class VarRef(ASTNode):
    def __init__(self,name:str):
        """
            Constructor of multiplication class

            Params:
            name: variable name
        """
        self.name=name

    def execute(self,symbolTable:list):
        return symbolTable.get(self.name,None) 
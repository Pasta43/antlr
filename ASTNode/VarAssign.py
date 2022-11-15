from ASTNode.ASTNode import ASTNode
class VarAssign(ASTNode):
    def __init__(self,name:str,expression:ASTNode):
        """
            Constructor of multiplication class

            Params:
            name: variable name
        """
        self.name=name
        self.expression = expression

    def execute(self,symbolTable:list):
        symbolTable[self.name]=self.expression.execute(symbolTable)
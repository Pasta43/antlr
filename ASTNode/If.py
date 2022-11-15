from ASTNode.ASTNode import ASTNode
class If(ASTNode):
    def __init__(self,condition:ASTNode,body:list,elseBody:list):
        """
            Constructor of conditional class

            Params:
            condition: boolean
            body: list
        """
        self.condition=condition
        self.body=body
        self.elseBody=elseBody

    def execute(self,symbolTable:list):
        if self.condition.execute(symbolTable):
            for node in self.body:
                node.execute(symbolTable)
        else:
            for node in self.elseBody:
                node.execute(symbolTable)
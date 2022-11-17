from ASTNode.ASTNode import ASTNode
class WhileLoop(ASTNode):
    def __init__(self,condition:ASTNode,body:list):
        """
            Constructor of conditional class

            Params:
            condition: boolean
            body: list
        """
        self.condition=condition
        self.body=body

    def execute(self,symbolTable:list):
        while self.condition.execute(symbolTable):
            for node in self.body:
                node.execute(symbolTable)
        
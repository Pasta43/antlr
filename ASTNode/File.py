from ASTNode.ASTNode import ASTNode
class File(ASTNode):
    def __init__(self,path,open_mode):
        """
            Constructor of file value class

            Params:
            path: pathfile
            open_mode: the file's open mode 
        """
        self.path=path
        self.open_mode=open_mode
        self.file=open(path,open_mode)

    def execute(self,symbolTable:list):
        return self.file
    
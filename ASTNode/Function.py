import numpy as np
import matplotlib.pyplot as plt

from ASTNode.ASTNode import ASTNode
from ASTNode.File import File
class Function(ASTNode):
    def __init__(self,function_name:str,arguments:ASTNode):
        """
            Constructor of function class
        """
        self.function_name=function_name
        self.arguments=arguments

    def execute(self,symbolTable:list):
        res=None
        if self.function_name=="sin":
            res =np.sin(self.arguments.execute(symbolTable)).tolist()
        elif self.function_name=="cos":
            res= np.cos(self.arguments.execute(symbolTable))
        elif self.function_name=="tan":
            res= np.tan(self.arguments.execute(symbolTable))
        elif self.function_name=="csc":
            res= 1/np.sin(self.arguments.execute(symbolTable))
        elif self.function_name=="sec":
            res= 1/np.cos(self.arguments.execute(symbolTable))
        elif self.function_name=="cot":
            res= 1/np.tan(self.arguments.execute(symbolTable))
        elif self.function_name=="get_elem":
            args=self.arguments.execute(symbolTable)
            res=[args[0][args[1]]]
        elif self.function_name=="plot":
            args = self.arguments.execute(symbolTable)
            plt.plot(args[0],args[1])
            if (args[2]):
                plt.show()
        elif self.function_name=="scatter":
            args = self.arguments.execute(symbolTable)
            plt.scatter(args[0],args[1])
            if (args[2]):
                plt.show()
        elif self.function_name=="trans":
            args=self.arguments.execute(symbolTable)
            m= np.matrix(args[0])
            res = [m.T]
        elif self.function_name=="inv":
            args=self.arguments.execute(symbolTable)
            m = np.matrix(args[0])
            res = [m.I]
        elif self.function_name=="open":
            args = self.arguments.execute(symbolTable)
            res=[File(args[0].replace("\"",""),args[1].replace("\"",""))]
        elif self.function_name=="writeFile":
            args =self.arguments.execute(symbolTable)
            file=args[0].execute(symbolTable)
            new_line=args[1]
            file.write(new_line)
        elif self.function_name=="hasNextLine":
            args =self.arguments.execute(symbolTable)
            file=args[0].execute(symbolTable)
            curr_pos = file.tell()
            file.seek(0, 2)      # go to end of file
            eof = file.tell()    # get end-of-file position
            file.seek(curr_pos)      # go back to start of file
            res=[not file.tell()==eof]
        elif self.function_name=="getNextLine":
            args =self.arguments.execute(symbolTable)
            file=args[0].execute(symbolTable)
            res=[file.readline()]
        elif self.function_name=="readAll":
            args =self.arguments.execute(symbolTable)
            file=args[0].execute(symbolTable)
            res=["".join(file.readlines())]
        elif self.function_name=="closeFile":
            args =self.arguments.execute(symbolTable)
            file=args[0].execute(symbolTable)
            file.close()
        return res[0] if res != None and len(res)==1 else res
            
    
    def add(self,element:ASTNode):
        self.arr.append(element)
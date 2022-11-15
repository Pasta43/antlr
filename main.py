import sys
from antlr4 import *
from ChibchombianoLexer import ChibchombianoLexer
from ChibchombianoParser import ChibchombianoParser
from ChibchombianoVisitor import ChibchombianoVisitor




def main(argv):
    if len(argv)>1:
        print("Interpretando archivo",argv[1])
        input_stream = FileStream(argv[1]) # entrada
        
        lexer = ChibchombianoLexer(input_stream) # Analizador léxico
        
        stream = CommonTokenStream(lexer) #Flujo de tokens
        
        parser = ChibchombianoParser(stream) # Análisis sintáctico
        
        
        tree = parser.program()  # Árbol de sintaxis concreta
        

        # Análisis semántico
        visitor = ChibchombianoVisitor()
        output = visitor.visit(tree)
        
        
        print("Interpretación finalizada")
    else:
        while True:
            try:
                input_stream = InputStream(input("> ")) # entrada
                
                lexer = ChibchombianoLexer(input_stream) # Analizador léxico
                
                stream = CommonTokenStream(lexer) #Flujo de tokens
                
                parser = ChibchombianoParser(stream) # Análisis sintáctico
                
                
                tree = parser.program()  # Árbol de sintaxis concreta
                

                # Análisis semántico
                visitor = ChibchombianoVisitor()
                output = visitor.visit(tree)
            except KeyboardInterrupt:
                print("Finished!")
                exit(0)
        
if __name__ == '__main__':
    main(sys.argv)
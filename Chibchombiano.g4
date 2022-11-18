grammar Chibchombiano;		

@parser::header { 
import numpy as np
dictionary_symbols = dict() 
from ASTNode.Puts import Puts 

from ASTNode.GreaterThan import GreaterThan
from ASTNode.LowerThan import LowerThan
from ASTNode.EqualsThan import EqualsThan
from ASTNode.LowerOrEqualThan import LowerOrEqualThan 
from ASTNode.GreaterOrEqualThan import GreaterOrEqualThan

from ASTNode.If import If
from ASTNode.WhileLoop import WhileLoop

from ASTNode.Addition import Addition
from ASTNode.Substraction import Substraction
from ASTNode.Multiplication import Multiplication
from ASTNode.Division import Division
from ASTNode.Module import Module
from ASTNode.Exponent import Exponent



from ASTNode.Constant import Constant
from ASTNode.VarDecl import VarDecl
from ASTNode.VarRef import VarRef
from ASTNode.VarAssign import VarAssign
}

@parser::members {

}
program:
        {body=list()}
        (sentence {body.append($sentence.node)})* 
{
for node in body:
    node.execute(dictionary_symbols)
}
        ;

sentence returns [node]:  
        var_assign {$node =$var_assign.node}
        |
        var_decl {$node = $var_decl.node}
        |
        std_output {$node = $std_output.node}
        | 
        conditional {$node=$conditional.node};
var_decl returns [node]: VAR ID  
{
$node = VarDecl($ID.text)
} ;


var_assign returns[node]: ID ASSIGN expression
        {$node = VarAssign($ID.text,$expression.node)};
        
std_output returns[node]: PUTS expression  
            {$node = Puts($expression.node) };

conditional returns[node]: IF PAR_OPEN expression PAR_CLOSE
        {body=list()}
        {elseBody=list()}
        BRACKET_OPEN (s1=sentence {body.append($s1.node)})* BRACKET_CLOSE
        (ELSE 
        BRACKET_OPEN (s2=sentence {elseBody.append($s2.node)})* BRACKET_CLOSE)?
        {$node = If($expression.node,body,elseBody)}
;

while_loop returns[node]: WHILE PAR_OPEN expression PAR_CLOSE
        {body=list()}
        BRACKET_OPEN (s1= sentence {body.append($s1.node)})* BRACKET_CLOSE
        {$node = WhileLoop($expression.node,body)}
;       
condition returns[node]: comparison {$node=$comparison.node}
 (
        AND
        |
        OR
)*;
comparison returns[node]: (
        e1=greater_than
        {$node=$e1.node} 
        | 
        e2=lower_than 
        {$node=$e2.node}
        | 
        e3=equals 
        {$node=$e3.node}
        | 
        e4=greater_or_equal_than
        {$node=$e4.node}
        |
        e5=lower_or_equal_than
        {$node=$e5.node} ) ;

greater_than returns[node]: e1=expression GT e2=expression
{$node=GreaterThan($e1.node,$e2.node)};

lower_than returns[node]: e1=expression LT e2=expression
{$node=LowerThan($e1.node,$e2.node)};

equals returns[node]: e1=expression EQ e2=expression
{$node=Equals($e1.node,$e2.node)};

greater_or_equal_than returns[node]: e1=expression GEQ e2=expression
{$node=GreaterOrEqualThan($e1.node,$e2.node)};

lower_or_equal_than returns[node]: e1=expression LEQ e2=expression
{$node=LowerOrEqualThan($e1.node,$e2.node)};


expression returns [node]:
        t1=factor {$node= $t1.node}
        (
                PLUS t2=factor 
                {$node= Addition($node,$t2.node)}
                |
                MINUS t3=factor 
                {$node = Substraction($node,$t3.node)}
                |
                condition
        )*;
factor returns [node]:
        t1=exponent {$node = $t1.node }
        (
                MULT t2=exponent
                {$node = Multiplication($node, $t2.node)}
                |
                DIV  t3=exponent
                {$node = Division($node,$t3.node)}
                |
                MOD  t4=exponent
                {$node =  Module($node,$t4.node)}
        )*;

exponent returns[node]:
        t1= term {$node=$t1.node}
        (
                POW t2= term {$node = Exponent($node,$t2.node)}
        )*;

term returns [node]: NUMBER {
splitted = $NUMBER.text.split(".") 
if len(splitted)==1:
        $node = Constant(int($NUMBER.text))
elif len(splitted)==2:
        $node = Constant(float($NUMBER.text))
}
|
ID {$node = VarRef($ID.text)}
|
BOOLEAN {
put_bool=lambda x: x=="true"
$node= Constant(put_bool($BOOLEAN.text))}
|
PAR_OPEN expression PAR_CLOSE {$node=$expression.node};

PROGRAM: 'program';
VAR: 'var';
PUTS: 'puts';

IF: 'if';
ELSE: 'else';

WHILE: 'while';


PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: 'mod';
POW: '^';

AND: 'and';
OR: 'or';
NOT: 'not';

GT: '>';
LT: '<';
GEQ: '>=';
LEQ: '<=';
EQ: '==';
NEQ: '!=';

ASSIGN: '=';

BRACKET_OPEN: '{';
BRACKET_CLOSE: '}';

PAR_OPEN: '(';
PAR_CLOSE: ')';

SEMICOLON: ';';

BOOLEAN: 'true'|'false';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

NUMBER: [0-9]+[.]?[0-9]*;

STRING: [a-zA-Z]+;

WS: [ \t\n\r]+ -> skip;


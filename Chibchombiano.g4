grammar Chibchombiano;		

@parser::header { 
import numpy as np
dictionary_symbols = dict() 
from ASTNode.Puts import Puts 

from ASTNode.Function import Function
from ASTNode.Arguments import Arguments

from ASTNode.And import And
from ASTNode.Or import Or
from ASTNode.Not import Not

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
from ASTNode.Array import Array
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
        std_output {$node = $std_output.node}
        | 
        conditional {$node=$conditional.node}
        |
        while_loop {$node = $while_loop.node}
        |
        expression {$node = $expression.node}
;


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

expression returns[node]: or_expression {$node=$or_expression.node};

or_expression returns[node]: e1=and_expression {$node=$e1.node} 
(
        OR e2=and_expression {$node=Or($node,$e2.node)} 
)*;
and_expression returns[node]: e1=not_expression{$node=$e1.node} 
(
        AND e2=not_expression {$node=And($node,$e2.node)}
)*;
not_expression returns [node]: (
        e1=logical_expression {$node=$e1.node} 
        |
        NOT e2=logical_expression{$node=Not($e2.node)});
logical_expression returns[node]: 
        e1=sum {$node=$e1.node}
        (
                GT e2=sum
                {$node=GreaterThan($node,$e2.node)}
                |
                LT e3=sum
                {$node=LowerThan($node,$e3.node)}
                |
                EQ e4=sum
                {$node=EqualsThan($node,$e4.node)}
                |
                GEQ e5=sum
                {$node=GreaterOrEqualThan($node,$e5.node)}
                |
                LEQ e6=sum
                {$node=LowerOrEqualThan($node,$e6.node)}  
        )*

;

sum returns [node]:
        t1=factor {$node= $t1.node}
        (
                PLUS t2=factor 
                {$node= Addition($node,$t2.node)}
                |
                MINUS t3=factor 
                {$node = Substraction($node,$t3.node)}
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

term returns [node]: 
STRING {$node=Constant($STRING.text)} 
|
NUMBER {
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
PAR_OPEN e1=expression PAR_CLOSE {$node=$e1.node}
|
array {$node=$array.node}
|
function {$node = $function.node}
;


function returns[node]: 
        e1=(
                SIN
                |COS
                |TAN
                |CSC
                |SEC
                |COT
                |PLOT
                |SCATTER
                |GET_ELEM
                |INV
                |TRANS
                |OPEN_FILE
                |READ_LINE
                |HAS_NEXT_LINE
                |WRITE_FILE
                |READ_ALL_LINES
                |CLOSE_FILE
        ) PAR_OPEN arguments? PAR_CLOSE
{$node = Function($e1.text,$arguments.node)}
;

arguments returns[node]: 
{$node = Arguments()}
e1=expression {$node.add($e1.node)}
 (','e2=expression{$node.add($e2.node)})*;

array returns[node]: 
 
{$node = Array()}
 (
        SQUARE_BRACKET_OPEN (e1=expression{$node.add($e1.node)}
        ( ',' e2=expression {$node.add($e2.node)})*)? 
        SQUARE_BRACKET_CLOSE
        |
        n1=NUMBER COLON (n2=NUMBER COLON)? n3=NUMBER
        {$node.arange($n1,$n2,$n3)}
 );

PUTS: 'puts';
SIN: 'sin';
COS: 'cos';
TAN: 'tan';
CSC: 'csc';
SEC: 'sec';
COT: 'cot';
PLOT: 'plot';
INV: 'inv';
TRANS: 'trans';
SCATTER: 'scatter';
GET_ELEM: 'getElem';
OPEN_FILE: 'open';
READ_LINE: 'getNextLine';
HAS_NEXT_LINE: 'hasNextLine';
WRITE_FILE: 'writeFile';
READ_ALL_LINES: 'readAll';
CLOSE_FILE: 'closeFile';

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

SQUARE_BRACKET_OPEN: '[';
SQUARE_BRACKET_CLOSE: ']';

BRACKET_OPEN: '{';
BRACKET_CLOSE: '}';

PAR_OPEN: '(';
PAR_CLOSE: ')';

SEMICOLON: ';';
COLON: ':';

BOOLEAN: 'true'|'false';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

NUMBER: [0-9]+[.]?[0-9]*;

STRING: '"' ('\\' ["\\] | ~["\\\r\n])* '"';

WS: [ \t\n\r]+ -> skip;


COMMENT
    : '/*' .*? '*/' -> skip
;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
;
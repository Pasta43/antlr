grammar Chibchombiano;		

@parser::header { 
import numpy as np
dictionary_symbols = dict()  
}

@parser::members {

}
program: 
        sentence* 
        ;

sentence: var_decl | var_assign | std_output ;
var_decl: VAR ID SEMICOLON 
{
dictionary_symbols[$ID.text]=""
} ;

var_assign: ID ASSIGN expression SEMICOLON
        {dictionary_symbols[$ID.text]=$expression.value};
        

std_output: PUTS expression SEMICOLON 
            {print($expression.value)};
conditional: IF PAR_OPEN expression PAR_CLOSE
        BRACKET_OPEN sentence* BRACKET_CLOSE
;

expression returns [value]:  
        t1=factor {$value= $t1.value}
        (
                PLUS t2=factor 
                {$value+= $t2.value}
                |
                MINUS t3=factor 
                {$value -= $t3.value}
        )*;
factor returns [value]:
        t1=exponent {$value = $t1.value }
        (
                MULT t2=exponent
                {$value *= $t2.value}
                |
                DIV  t3=exponent
                {$value /= $t3.value}
                |
                MOD  t4=exponent
                {$value %=  $t4.value}
        )*;

exponent returns[value]:
        t1= term {$value=$t1.value}
        (
                POW t2= term {$value = $value**$t2.value}
        )*;

term returns [value]: NUMBER {
splitted = $NUMBER.text.split(".") 
if len(splitted)==1:
        $value = int($NUMBER.text)
elif len(splitted)==2:
        $value = float($NUMBER.text)
}
|
ID {$value = dictionary_symbols.get($ID.text,None)}
|
BOOLEAN {
put_bool=lambda x: True if x=="true" else False
$value= put_bool($BOOLEAN.text)}
|
PAR_OPEN expression PAR_CLOSE {$value=$expression.value};

PROGRAM: 'program';
VAR: 'var';
PUTS: 'puts';

IF: 'if';
ELSE: 'else';


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

NUMBER: [-]?[0-9]+[.]?[0-9]*;

STRING: [a-zA-Z]+;

WS: [ \t\n\r]+ -> skip;


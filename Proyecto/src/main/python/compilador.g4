grammar compilador;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

PA : '(' ;
PC : ')' ;
LLA : '{' ;
LLC : '}' ;
PYC : ';' ;
ASIG : '=' ;
COMA : ',' ;
LA : '[' ;
LC : ']' ;
SUMA : '+' ;
RESTA : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
INCDEC : '++' | '--' ;
AND : '&&' ;
OR : '||' ;
COMP : '==' | '!=' | '<' | '<=' | '>' | '>=' ;
LIT : 'true' | 'false' ;

NUMERO : DIGITO+ ;
DECIMAL : DIGITO+ '.' DIGITO+ ;
STRING : '"' (~["\n\r])* '"' ;

INT : 'int' ;
DOUBLE : 'double' ;
IF :    'if' ;
ELSE :  'else' ;
FOR :   'for' ;
WHILE : 'while' ;
RETURN : 'return' ;
BREAK : 'break' ;
CONTINUE : 'continue' ;
SWITCH : 'switch' ;
CASE : 'case' ;
DEFAULT : 'default' ;
DO : 'do' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \n\r\t] -> skip ;
OTRO : . ;

programa : instrucciones EOF ;

instrucciones : instruccion instrucciones
              |
              ;

instruccion : asignacion PYC
            | declaracion PYC
            | iincdec PYC
            | ireturn PYC
            | ifor
            | iif
            | iwhile
            | idowhile
            | iswitch
            | BREAK PYC
            | CONTINUE PYC
            | funcion
            | proto
            | llamada PYC
            | bloque
            ;

bloque : LLA instrucciones LLC ;

iwhile : WHILE PA condicion PC instruccion;

idowhile : DO instruccion WHILE PA condicion PC PYC ;

iif : IF PA condicion PC instruccion ielse2 ;

ielse2 : ELSE iif
       | ELSE instruccion
       |
       ;

iswitch : SWITCH PA condicion PC LLA casosSwitch LLC ;

casosSwitch : CASE opal PC instrucciones casosSwitch
            | DEFAULT PC instrucciones
            |
            ;

condicion : orExp ;

orExp : andExp orExpRest ;

orExpRest : OR andExp orExpRest
          |
          ;

andExp : comparacion andExpRest ;

andExpRest : AND comparacion andExpRest
           |
           ;

comparacion : termino comparacionRest ;

comparacionRest : COMP termino
                |
                ;

termino : opal
        | LIT
        | PA condicion PC
        ;

ifor :FOR PA (asignacion | declaracion | opal |) PYC (comparacion|) PYC (iincdec|)  PC instruccion
     ;
     
declaracion : tipo ID inic listavar
            ;

listavar : COMA ID inic listavar
         |
         ;

inic : ASIG opal
     |
     ;

tipo : INT
     | DOUBLE
     | INT LA LC
     | DOUBLE LA LC
     ;

iincdec : ID INCDEC
        | INCDEC ID
        ;

asignacion : ID ASIG opal
           | ID LA exp LC ASIG opal
           ;

funcion: tipo ID PA argumento PC bloque;

proto: tipo ID PA argumento PC PYC ;

llamada: ID PA argumentosLlamada PC ;

argumento: tipo ID listaParametros|;
           
listaParametros : COMA tipo ID listaParametros |;
listaArgumentos : COMA opal listaArgumentos |;
              
argumentosLlamada :  opal listaArgumentos|;

ireturn : RETURN (opal|) ;

opal : exp
     ;

exp : term e ;

e : SUMA term e
  | RESTA term e
  |
  ;

term : factor t ;

t : MULT factor t
  | DIV factor t
  | MOD factor t
  |
  ;

factor : NUMERO
       | DECIMAL
       | STRING
       | ID
       | ID LA exp LC
       | PA exp PC
       | llamada
       ;
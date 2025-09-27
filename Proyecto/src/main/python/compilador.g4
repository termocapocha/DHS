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
SUMA : '+' ;
RESTA : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
INCDEC : '++' | '--' ;
COMP : '==' | '!=' | '<' | '<=' | '>' | '>=' ;

NUMERO : DIGITO+ ;

INT : 'int' ;
DOUBLE : 'double' ;
IF :    'if' ;
ELSE :  'else' ;
FOR :   'for' ;
WHILE : 'while' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \n\r\t] -> skip ;
OTRO : . ;

// s : ID     {print("ID ->" + $ID.text + "<--") }         s
//   | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
//   | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
//   | EOF
//   ;

// s : PA s PC s
//   |
//   ;

programa : instrucciones EOF ; //entrada

instrucciones : instruccion instrucciones
              |
              ;

instruccion : asignacion PYC
            | declaracion PYC
            | iincdec PYC
            | ifor
            | iif
            | iwhile
            | bloque
            ;

bloque : LLA instrucciones LLC ;

iwhile : WHILE PA opal PC instruccion 
       | WHILE PA opal PC bloque
       | WHILE PA comparator PC instruccion
       | WHILE PA comparator PC bloque
       ;

iif : IF PA opal PC instruccion ielse ;

ielse : ELSE instruccion
      |
      ;

ifor :FOR PA (inicializacion|) PYC (comparator|) PYC (iincdec|)  PC (bloque | instruccion)
     ;  //en teoria, todos los for
     
declaracion : tipo ID inic listavar
            | tipo ID inic listavar PYC
            ;

listavar : COMA ID inic listavar
         |
         ;

inic : ASIG opal
     |
     ;

tipo : INT
     | DOUBLE
     ;

inicializacion :ID  //new
               | asignacion
               | declaracion
               ;

iincdec : ID INCDEC //new
        | INCDEC ID
        ;

comparator : ID COMP ID //new
            | ID COMP NUMERO 
            | NUMERO COMP ID
            | NUMERO COMP NUMERO
            ;

asignacion : ID ASIG opal ;

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
       | ID
       | PA exp PC
       ;
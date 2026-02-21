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
AND : '&&' ;
OR : '||' ;
COMP : '==' | '!=' | '<' | '<=' | '>' | '>=' ;
LIT : 'true' | 'false' ;


NUMERO : DIGITO+ ;
DECIMAL : DIGITO+ '.' DIGITO+ ;

INT : 'int' ;
DOUBLE : 'double' ;
IF :    'if' ;
ELSE :  'else' ;
FOR :   'for' ;
WHILE : 'while' ;
RETURN : 'return' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \n\r\t] -> skip ;
OTRO : . ;



programa : instrucciones EOF ; //entrada

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
            | funcion
            | proto
            | llamada PYC
            | bloque
            ;

bloque : LLA instrucciones LLC ;

iwhile : WHILE PA condicion PC instruccion;

iif : IF PA condicion PC instruccion ielse ;

condicion : orExp ;

orExp : andExp orExpRest ;  // maneja los OR

orExpRest : OR andExp orExpRest
          |
          ;

andExp : comparacion andExpRest ; // maneja los AND

andExpRest : AND comparacion andExpRest
           |
           ;

comparacion : termino comparacionRest ; //lo que dice el nombre

comparacionRest : COMP termino
                |
                ;

termino : opal      //soluciona problema de los ()
        | LIT 
        | PA condicion PC
        ;

ielse : ELSE instruccion
      |
      ;

ifor :FOR PA (asignacion | declaracion |) PYC (comparacion|) PYC (iincdec|)  PC instruccion
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
     ;



iincdec : ID INCDEC //new
        | INCDEC ID
        ;

asignacion : ID ASIG opal ;

funcion: tipo ID PA argumento PC bloque; //int funcion(int x, double y,..){}

proto: tipo ID PA argumento PC PYC ; //int funcion(int x, double y,...);

llamada: ID PA argumentosLlamada PC ; //funcion(x,y,...);

argumento: tipo ID listaParametros|;  //el vacio es por si llego a tener una llamada "imprimir()"
           
listaParametros : COMA tipo ID listaParametros |; //mod
listaArgumentos : COMA opal listaArgumentos |;
              
argumentosLlamada :  opal listaArgumentos|;

ireturn : RETURN (opal|LIT|condicion|) ;

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
       | ID
       | PA exp PC
       | llamada
       ;
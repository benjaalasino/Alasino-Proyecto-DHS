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

EQ  : '==';
NEQ : '!=';
MEN : '<';
MAY : '>';
MENIG : '<=';
MAYIG : '>=';
AND : '&&';
OR  : '||';
NOT : '!';

NUMERO : DIGITO+ ;

INT : 'int' ;
DOUBLE : 'double' ;
VOID : 'void' ;

IF : 'if' ;
ELSE : 'else' ;
FOR : 'for' ;
WHILE : 'while' ;
RETURN : 'return' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \n\r\t] -> skip ;
OTRO : . ;

programa : elemento_programa 
         | EOF
         ;

elemento_programa : declaracion_variable
                  | declaracion_funcion 
                  | prototipo_funcion
                  | instruccion
                  ;

instrucciones : instruccion instrucciones
              |
              ;

instruccion : asignacion
            | declaracion_variable
            | iif
            | iwhile
            | ifor
            | ireturn
            | llamada_funcion PYC
            ;

bloque : LLA instrucciones LLC ;

// Estructuras de control 
iwhile : WHILE PA expr_logica PC bloque ;

iif : IF PA expr_logica PC bloque ielse ;

ielse : ELSE bloque
      |
      ;

ifor : FOR PA declaracion_for expr_logica PYC asignacion_for PC bloque ;

declaracion_for : declaracion_variable
                | asignacion
                |
                ;

asignacion_for : ID ASIG expr
               |
               ;

ireturn : RETURN expr PYC
        | RETURN PYC
        ;

// Declaraciones de variables 
declaracion_variable : tipo ID inic listavar PYC ;

inic : ASIG expr
     | 
     ;

listavar : COMA ID inic listavar   
         |                          
         ;

// Funciones: prototipos, declaraciones y llamada
prototipo_funcion : tipo ID PA parametros_formales PC PYC ;

declaracion_funcion : tipo ID PA parametros_formales PC bloque ;

parametros_formales : lista_parametros
                    |
                    ;

lista_parametros : tipo ID resto_parametros ;

resto_parametros : COMA tipo ID resto_parametros
                 |
                 ;

llamada_funcion : ID PA parametros_reales PC ;

parametros_reales : lista_expresiones
                  |
                  ;

lista_expresiones : expr resto_expresiones ;

resto_expresiones : COMA expr resto_expresiones
                  |
                  ;

// Tipos de datos
tipo : INT
     | DOUBLE
     | VOID
     ;

// Asignaciones
asignacion : ID ASIG expr PYC ;

// Expresiones aritméticas
expr : term expr_rest ;

expr_rest : SUMA term expr_rest
          | RESTA term expr_rest
          |
          ;

term : factor term_rest ;

term_rest : MULT factor term_rest
          | DIV factor term_rest
          | MOD factor term_rest
          |
          ;

factor : ID
       | NUMERO
       | llamada_funcion
       | PA expr PC
       | RESTA factor
       | SUMA factor
       ;

// Expresiones lógicas y de comparación
expr_logica : expr_and expr_logica_rest ;

expr_logica_rest : OR expr_and expr_logica_rest
                 |
                 ;

expr_and : expr_comp expr_and_rest ;

expr_and_rest : AND expr_comp expr_and_rest
              |
              ;

expr_comp : expr expr_comp_rest ;

expr_comp_rest : EQ expr
               | NEQ expr
               | MEN expr
               | MAY expr
               | MENIG expr
               | MAYIG expr
               |
               ;

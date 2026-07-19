# INFORME DEL COMPILADOR DHS 2025

## 1. Resumen del Proyecto

Compilador académico para un lenguaje de programación de tipo C simplificado, desarrollado como proyecto de la materia DHS 2025. El compilador realiza análisis léxico, sintáctico y semántico, y genera código de tres direcciones con optimizaciones. Está implementado en Python 3 con ANTLR 4 como generador de parser.

**Arquitectura general:**

```
Archivo fuente (.txt)
    |
    v
[ANTLR 4] --> Lexer + Parser --> Árbol de sintaxis abstracta (AST)
    |
    v
[Escucha.py] --> Análisis Semántico + Tabla de Símbolos
    |
    v
[Caminante.py] --> Generación de Código de Tres Direcciones
    |
    v
[Optimizaciones] --> Código optimizado
    |
    v
Archivos de salida (output/)
```

---

## 2. Componentes del Compilador

### 2.1. Gramática ANTLR (`compilador.g4`)

Gramática combinada (lexer + parser) de 161 líneas que define un lenguaje C-like.

#### Tokens Léxicos (30 tokens)

| Token | Patrón | Descripción |
|-------|--------|-------------|
| `PA`, `PC` | `(`, `)` | Paréntesis |
| `LLA`, `LLC` | `{`, `}` | Llaves (bloques) |
| `PYC` | `;` | Punto y coma |
| `ASIG` | `=` | Asignación |
| `COMA` | `,` | Coma |
| `SUMA`, `RESTA`, `MULT`, `DIV`, `MOD` | `+`, `-`, `*`, `/`, `%` | Operadores aritméticos |
| `INCDEC` | `++`, `--` | Incremento/decremento |
| `AND`, `OR` | `&&`, `\|\|` | Operadores lógicos |
| `COMP` | `==`, `!=`, `<`, `<=`, `>`, `>=` | Operadores de comparación |
| `LIT` | `true`, `false` | Literales booleanos |
| `NUMERO` | `[0-9]+` | Enteros |
| `DECIMAL` | `[0-9]+.[0-9]+` | Flotantes |
| `INT`, `DOUBLE` | `int`, `double` | Tipos de datos |
| `IF`, `ELSE`, `FOR`, `WHILE`, `RETURN` | Palabras clave | Estructuras de control |
| `ID` | `[a-zA-Z_][a-zA-Z0-9_]*` | Identificadores |
| `WS` | `[\n\r\t]` | Espacios en blanco (se skipean) |
| `OTRO` | `.` | Caracter no reconocido (fallback) |

#### Reglas Sintácticas Principales

**Programa:**
```
programa : instrucciones EOF ;
instrucciones : instruccion instrucciones | ;
```

**Instrucciones:**
```
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
```

**Estructuras de control:**
```
iif     : IF PA condicion PC instruccion ielse ;
iwhile  : WHILE PA condicion PC instruccion ;
ifor    : FOR PA (asignacion | declaracion | opal |) PYC (comparacion|) PYC (iincdec|) PC instruccion ;
ielse   : ELSE instruccion | ;
```

**Expresiones (con precedencia correcta):**
```
opal  : exp ;
exp   : term e ;
e     : SUMA term e | RESTA term e | ;
term  : factor t ;
t     : MULT factor t | DIV factor t | MOD factor t | ;
factor: NUMERO | DECIMAL | ID | PA exp PC | llamada ;
```

**Condiciones:**
```
condicion     : orExp ;
orExp         : andExp orExpRest ;
orExpRest     : OR andExp orExpRest | ;
andExp        : comparacion andExpRest ;
andExpRest    : AND comparacion andExpRest | ;
comparacion   : termino comparacionRest ;
comparacionRest : COMP termino | ;
termino       : opal | LIT | PA condicion PC ;
```

**Funciones:**
```
funcion  : tipo ID PA argumento PC bloque ;
proto    : tipo ID PA argumento PC PYC ;
llamada  : ID PA argumentosLlamada PC ;
argumento: tipo ID listaParametros | ;
```

---

### 2.2. Analizador Semántico (`Escucha.py`)

Clase que extiende `compiladorListener` (patrón Listener de ANTLR). Se ejecuta *durante* el parseo, reaccionando a eventos de entrada/salida de cada regla.

#### Funcionalidades

1. **Manejo de contextos (scopes)**
   - Al entrar a un bloque (`enterBloque`), crea un nuevo contexto en la tabla de símbolos.
   - Determina el tipo de contexto (global, función, if, else, while) según el padre en el AST.
   - Al salir del bloque (`exitBloque`), elimina el contexto y lo archiva en el historial.

2. **Declaración de variables**
   - Verifica que el tipo sea válido (`int` o `double`).
   - Detecta redeclaraciones en el mismo ámbito.
   - Soporta declaración múltiple: `int x = 0, y, z = x;`

3. **Declaración de funciones**
   - Prototipos (`exitProto`) y definiciones (`exitFuncion`).
   - Si una función ya fue declarada como prototipo, la definición actualiza sus parámetros.
   - Registra los parámetros formales para su validación posterior.

4. **Verificación de uso de variables**
   - En `exitFactor` (uso en expresiones) y `exitIincdec` (incremento/decremento).
   - Marca variables como utilizadas para el reporte final.

5. **Asignaciones con verificación de tipos**
   - Compara el tipo del lado izquierdo con el tipo del lado derecho.
   - Reporta `ERROR SEMANTICO: Incompatibilidad de tipos`.

6. **Validación de llamadas a funciones**
   - Verifica que la función exista.
   - **Cuenta argumentos:** reporta error si la cantidad no coincide.
   - **Verifica tipos:** compara el tipo de cada argumento con el tipo del parámetro esperado.

7. **Verificación de existencia de `main`:**
   - Al finalizar el programa, si `main` no fue declarada, reporta error semántico.

8. **Reporte final:** lista variables/funciones declaradas pero nunca utilizadas.

---

### 2.3. Tabla de Símbolos (`TablaSimbolos.py`)

Implementación con patrón **Singleton**: solo existe una instancia de la tabla en todo el programa.

#### Estructura interna

```
TablaSimbolos
├── contexto: list[dict]    → Pila de scopes (cada uno es un dict nombre → ID)
├── historial: list         → Scopes cerrados (para exportar)
├── tiposContexto: dict     → Mapea ID de contexto a tipo (global, funcion, if, ...)
└── indiceAId: dict         → Mapea índice en la pila a ID de contexto
```

#### Clase `ID`
Representa un símbolo (variable o función):
- `nombre`, `tipo` (int/double), `varFunc` (variable/funcion)
- `utilizada` (bool), `esParametro` (bool)

#### Clase `FuncionCompilador` (hereda de `ID`)
- Agrega `parametros: list[ID]`

#### Métodos principales
- `agregarContexto(tipo)` / `quitarContexto()` → push/pop de scope
- `agregarId(id)` / `devolverID(nombre)` → insertar y buscar (búsqueda anidada)
- `marcarUtilizada(nombre)` / `obtenerNoUtilizadas()` → tracking de uso
- `exportarTabla(archivo)` → exporta TODOS los contextos (activos + historial) a un archivo

---

### 2.4. Generador de Código de Tres Direcciones (`Caminante.py`)

Clase que extiende `compiladorVisitor` (patrón Visitor de ANTLR). Recorre el AST después del parseo para generar código de tres direcciones y optimizarlo.

---

## 3. MANUAL DEL CÓDIGO DE TRES DIRECCIONES

El código de tres direcciones (TAC, Three-Address Code) es una representación intermedia donde cada instrucción tiene **a lo sumo tres operandos** (dos fuentes y un destino). Es la representación canónica utilizada en compiladores porque:

- Es independiente de la máquina destino.
- Facilita la aplicación de optimizaciones.
- Es fácil de traducir a ensamblador.

### 3.1. Clase Emisora (`CodigoTresDirecciones.py`)

La clase `CodigoTresDirecciones` es el **emisor de código** que mantiene:
- `self.output`: lista de strings, cada uno es una instrucción.
- `self.tempCount`: contador para generar temporales (`t0`, `t1`, ...).
- `self.labelCount`: contador para generar labels (`L0`, `L1`, ...).

#### Constructor y estado
```python
def __init__(self):
    self.output = []       # Lista de instrucciones generadas
    self.tempCount = 0     # Próximo índice de temporal
    self.labelCount = 0    # Próximo índice de label
```

#### Generación de temporales y labels
```python
t = c3d.nuevaTemporal()   # → "t0", "t1", "t2", ...
l = c3d.nuevoLabel()      # → "L0", "L1", "L2", ...
```

#### Instrucciones emitidas

##### `asignacion(destino, valor)`
```
destino = valor
```
Emite: `x = 5`, `resultado = t3`, `z = 0`

##### `operacion(destino, a, operador, b)`
```
destino = a operador b
```
Emite: `t0 = x + 1`, `t1 = a && b`, `t2 = resultado != 0`

##### `llamadaFuncion(nombre, args)`
Para `suma(x, y)` emite:
```
push x
push y
call suma, 2
t0 = pop
pop_args 2
```
Donde:
- `push valor` → apila cada argumento
- `call nombre, N` → invoca la función con N argumentos
- `t = pop` → recupera el valor de retorno en un temporal
- `pop_args N` → limpia los N argumentos de la pila

##### `retorno(valor=None)`
```
push valor    # (si hay valor)
return
```

---

### 3.2. Formato de las Instrucciones

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Asignación simple | `var = valor` | `x = 5` |
| Operación binaria | `temp = a op b` | `t0 = x + 1` |
| Push de argumento | `push valor` | `push x` |
| Llamada a función | `call nombre, N` | `call suma, 2` |
| Pop de retorno | `temp = pop` | `t0 = pop` |
| Limpieza de args | `pop_args N` | `pop_args 2` |
| Retorno de función | `return` | `return` |
| Push para return | `push valor` | `push t0` |
| Label (destino de salto) | `L0:` | `L0:` |
| Salto condicional (false) | `ifFalse cond goto L` | `ifFalse t0 goto L1` |
| Salto condicional (true) | `ifTrue cond goto L` | `ifTrue t2 goto L3` |
| Salto incondicional | `goto L` | `goto L0` |

---

### 3.3. Generación de Código por Constructo

#### Asignación (`visitAsignacion`)
```
Código fuente:   x = a + b * c
Código 3 dirs:   t0 = b * c
                 t1 = a + t0
                 x = t1
```
En la práctica, el `Caminante` hace *constant folding* en línea, así que si `a + b * c` son constantes, lo reduce directamente.

#### Incremento/Decremento (`visitIincdec`)
```
Código fuente:   x++           |   --y
Código 3 dirs:   t0 = x + 1    |   t0 = y - 1
                 x = t0        |   y = t0
```

#### If (`visitIif`)
```
Código fuente:   if (x > 0) { ... } else { ... }

Código 3 dirs (simple):
    ifFalse x > 0 goto L0
    [cuerpo del if]
    goto L1
    L0:
    [cuerpo del else]
    L1:

Código 3 dirs (complejo con &&/||):
    [código de short-circuit para evaluar la condición → t0]
    ifFalse t0 goto L0
    [cuerpo del if]
    goto L1
    L0:
    [cuerpo del else]
    L1:
```

#### While (`visitIwhile`)
```
Código fuente:   while (x > 0) { x = x - 1; }

Código 3 dirs:
    L0:
    [evaluar condición → t0]
    ifFalse t0 goto L1
    [cuerpo del while]
    goto L0
    L1:
```

#### For (`visitIfor`)
```
Código fuente:   for (i = 0; i < 10; i++) { ... }

Código 3 dirs:
    i = 0            ← init
    L0:
    [evaluar i < 10 → t0]
    ifFalse t0 goto L1
    [cuerpo del for]
    t1 = i + 1       ← incremento
    i = t1
    goto L0
    L1:
```

#### Condiciones booleanas compuestas (short-circuit)

Para `a > 0 && b > 0`:
```
t0 = a > 0          ← evaluar primera comparación
ifFalse t0 goto L0  ← si es false, saltear el resto (short-circuit)
t1 = b > 0          ← evaluar segunda comparación
t2 = t0 && t1       ← combinar con AND
ifFalse t2 goto L0  ← si es false, saltear
[ ... ]
L0:
t0 = 0              ← resultado final (false)
```

Para `a > 0 || b > 0`:
```
t0 = a > 0          ← evaluar primera comparación
ifTrue t0 goto L1   ← si es true, saltear el resto (short-circuit)
t1 = b > 0          ← evaluar segunda comparación
ifTrue t1 goto L1   ← si es true, vamos al final
[ ... ]
L1:
[continuar]
```

#### Declaración de variable (`visitDeclaracion`)
```
Código fuente:   int x = 5;
Código 3 dirs:   x = 5

Código fuente:   double y;
Código 3 dirs:   y = 0.0

Código fuente:   int z;
Código 3 dirs:   z = 0
```

#### Función (`visitFuncion`)
```
Código fuente:   int suma(int a, int b) { return a + b; }

Código 3 dirs:
    suma:              ← label con nombre de la función
    [código del cuerpo]
    t0 = a + b
    push t0
    return
```

#### Llamada a función (`visitLlamada`)
```
Código fuente:   resultado = suma(x, y);

Código 3 dirs:
    push x
    push y
    call suma, 2
    t0 = pop
    pop_args 2
    resultado = t0
```

---

### 3.4. Evaluación de Expresiones con Constant Folding

El generador intenta plegar constantes *durante la generación*. Cuando visita un nodo de expresión, si ambos operandos son números, calcula el resultado en el momento y devuelve el valor directamente sin generar código.

#### Proceso recursivo para `2 + 3 * 4`:
1. `visitExp` → `visitTerm` → `visitFactor(2)` → `"2"`
   - `_procesarTermRest` → encuentra `*`, visita factor `3` y `4`
   - Como ambos son números, calcula `3 * 4 = 12`
   - Devuelve `"12"`
2. Continúa con la suma: `visitExp` → encuentra `+`, term izquierdo `"2"`, term derecho `"12"`
   - Calcula `2 + 12 = 14`
   - Devuelve `"14"`

**Resultado:** se genera `x = 14` en lugar de `t0 = 3 * 4; t1 = 2 + t0; x = t1`.

Si la expresión contiene variables (ej. `x + 5`), no se pliega y se devuelve la expresión en notación parentizada: `(x + 5)`, que luego se asigna a un temporal o directamente a la variable destino.

#### Evaluación de comparaciones constantes
Similar al constant folding pero para operadores relacionales:
```
2 == 2   →   1 (true)
3 != 3   →   0 (false)
5 < 3    →   0 (false)
```

---

### 3.5. Optimizaciones del Código de Tres Direcciones

Se aplican hasta 5 pasadas de optimización, iterando hasta 25 veces o hasta que no haya más cambios (punto fijo).

#### 3.5.1. Constant Folding (`constantFolding`)

Busca asignaciones del tipo `x = expresión_constante` y reemplaza la expresión por su valor numérico.

**Antes:**
```
t0 = 2 + 3
t1 = t0 * 4
```
**Después:**
```
t0 = 5
t1 = 20
```

Algoritmo mejorado: `evalArit` ahora respeta precedencia de operadores y paréntesis anidados, escaneando caracter por caracter y contando paréntesis para encontrar el operador correcto en cada nivel. No usa `split(op)` que fallaba con expresiones como `(2+3)*(4+5)`.

#### 3.5.2. Eliminación de Saltos Redundantes (`eliminarSaltosRedundantes`)

Elimina `goto L` cuando la siguiente línea es exactamente `L:`.

**Antes:**
```
    goto L0
    L0:
    x = 1
```
**Después:**
```
    L0:
    x = 1
```

#### 3.5.3. Propagación de Copias y Chaining (`propagarYCadenas`)

Reemplaza usos de temporales por sus valores conocidos, y encadena propagaciones.

**Antes:**
```
t0 = x + 1
t1 = t0
t2 = t1 * 2
```
**Después:** (t0 → x+1, t1 → x+1)
```
t0 = x + 1
t1 = x + 1
t2 = (x + 1) * 2
```

Usa `(?<!\w){temp}(?!\w)` en lugar de `\b` para evitar reemplazar `t1` dentro de `t10`.

#### 3.5.4. Eliminación de Temporales Redundantes (`eliminarTemporalesRedundantes`)

Elimina asignaciones a temporales que nunca son leídos después.

**Antes:**
```
t0 = 5        ← t0 nunca usado
x = t0 + 1
```
**Después:**
```
x = t0 + 1    ← (t0 se eliminaría solo si no se usa... pero en este caso SÍ se usa)
```

**Ejemplo real:**
```
t0 = 10       ← si t0 nunca aparece en el RHS de otra línea ni en un if, se elimina
```

#### 3.5.5. Simplificación de Expresiones (`simplificarExpresiones`)

Simplifica auto-comparaciones:
```
x == x   →   1
x != x   →   0
x > x    →   0
x < x    →   0
```

---

### 3.6. Ejemplo Completo: De Código Fuente a Código de 3 Direcciones

#### Código fuente (`test.txt`):
```c
int escaneo(int a, int b, int c, int f) {
    int r = 0;
    if (a > b && b > c) {
        r = 1;
    } else {
        r = 2;
    }
    f = 9;
    while (r > 0 && (a > 0 && b > 0)) {
        r = r - 1;
    }
    return r;
}

int main() {
    int x = 5;
    int y = 4;
    int z = 3;
    int resultado;
    int f = 67;
    resultado = escaneo(x, y, z, f);
    if (resultado != 0 && resultado <= 10) {
        resultado = resultado + 1;
    }
    return 0;
}
```

#### Código de 3 direcciones generado:

```
escaneo:
r = 0
t0 = a > b
ifFalse t0 goto L0
t1 = b > c
t2 = t0 && t1
ifFalse t2 goto L0
r = 1
goto L1
L0:
r = 0
r = 2
L1:
f = 9
L2:
t3 = r > 0
ifFalse t3 goto L3
t4 = a > 0
t5 = t4 && 1
t6 = b > 0
t7 = t5 && t6
ifFalse t7 goto L3
t8 = r - 1
r = t8
goto L2
L3:
push r
return

main:
x = 5
y = 4
z = 3
resultado = 0
f = 67
push x
push y
push z
push f
call escaneo, 4
t9 = pop
pop_args 4
resultado = t9
t10 = resultado != 0
ifFalse t10 goto L5
t11 = resultado <= 10
t12 = t10 && t11
ifFalse t12 goto L5
t13 = resultado + 1
resultado = t13
goto L4
L5:
resultado = 0
L4:
push 0
return
```

#### Código optimizado:

```
escaneo:
r = 0
t0 = a > b
ifFalse t0 goto L0
t1 = b > c
ifFalse t1 goto L0
r = 1
goto L1
L0:
r = 2
L1:
f = 9
L2:
t3 = r > 0
ifFalse t3 goto L3
t4 = a > 0
ifFalse t4 goto L3
t6 = b > 0
ifFalse t6 goto L3
t8 = r - 1
r = t8
goto L2
L3:
push r
return

main:
x = 5
y = 4
z = 3
resultado = 0
f = 67
push x
push y
push z
push f
call escaneo, 4
t9 = pop
pop_args 4
resultado = t9
t10 = resultado != 0
ifFalse t10 goto L5
t11 = resultado <= 10
ifFalse t11 goto L5
t13 = resultado + 1
resultado = t13
L5:
push 0
return
```

Las optimizaciones eliminaron:
1. Comparaciones redundantes (`t2 = t0 && t1` → innecesario, se usa `ifFalse t0` directamente)
2. Asignaciones muertas (el `L0: r = 0` se eliminó porque `r = 2` lo sobrescribe)
3. Saltos redundantes
4. Temporales nunca usados

---

## 4. Módulo Principal (`App.py`)

Orquestador del pipeline completo:

1. Lee el archivo fuente (por CLI o default `input/if.txt`).
2. Reinicia la tabla de símbolos (Singleton).
3. Crea el `Escucha` (listener) y lo adjunta al parser.
4. Ejecuta `parser.programa()` → el listener se ejecuta durante el parseo.
5. Exporta la tabla de símbolos a `output/tablaSimbolos.txt`.
6. Crea el `Caminante` (visitor) y recorre el AST.
7. El visitor genera el código de 3 direcciones y lo optimiza.
8. Exporta `output/CodigoIntermedio.txt` y `output/CodigoOptimizado.txt`.
9. Imprime el código intermedio en consola.

Manejo de errores: captura `FileNotFoundError` y excepciones del parser/visitor, escribiendo mensajes de error en los archivos de salida.

---

## 5. Archivos de Entrada/Salida

### Directorio `input/` (archivos de prueba)

| Archivo | Descripción |
|---------|-------------|
| `if.txt` | `if` simple sin else |
| `while.txt` | Ciclos `while` anidados |
| `for.txt` | `for` anidados con varias formas (vacío, expresión, etc.) |
| `test.txt` | Programa completo con función, prototipo, `while`, `if/else`, `return` |
| `test2.txt` | Prototipo + llamada simple |
| `test3.txt` | Bloques con shadowing de variables |
| `programa.txt` | Programa completo con múltiples constructos |
| `protoYFunc.txt` | Prueba de prototipos, llamadas correctas e incorrectas |

### Directorio `output/` (salidas generadas)

| Archivo | Contenido |
|---------|-----------|
| `tablaSimbolos.txt` | Tabla de símbolos con todos los contextos y variables |
| `CodigoIntermedio.txt` | Código de 3 direcciones sin optimizar |
| `CodigoOptimizado.txt` | Código de 3 direcciones optimizado |

---

## 6. Cómo Ejecutar

```bash
cd src/main/python
python App.py input/test.txt
```

Si no se pasa argumento, usa `input/if.txt` por defecto.

### Regenerar ANTLR (si se modifica la gramática):
```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor compilador.g4 -o .
```

---

## 7. Limitaciones y Trabajo Futuro

### Bugs conocidos corregidos
- **`for(y;;)`**: ahora se parsea correctamente (se agregó `opal` como alternativa en el init).
- **`evalArit` con `split(op)`**: reemplazado por escaneo carácter por carácter respetando paréntesis y precedencia.
- **`\b regex` en propagación**: reemplazado por `(?<!\w)...(?!\w)` para no confundir `t1` con `t10`.
- **Validación de argumentos en llamadas**: ahora verifica cantidad y tipo de cada argumento.
- **Verificación de `main`**: se reporta si no existe.

### Lo que aún falta
- **VM/Intérprete**: no hay ejecutor del código de 3 direcciones. Solo se genera texto.
- **`exit`**: no valida cantidad/tipo de argumentos en llamada a funciones del sistema.
- **Sin `break`/`continue`**: no existen en la gramática.
- **Sin `else if` anidado**: requiere `else { if(...) ... }` explícito.
- **Sin chequeo de tipo de retorno**: una función `int` puede hacer `return;` sin valor.
- **Sin arrays, strings, punteros, structs, switch, do-while**: la gramática es básica.
- **Sin verificación de que `main` tenga firma correcta**: solo verifica que exista.

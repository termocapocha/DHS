import sys
from antlr4 import *
from compiladorLexer  import compiladorLexer
from compiladorParser import compiladorParser
from Escucha import Escucha
from Caminante import Caminante
from TablaSimbolos import TablaSimbolos

# En caso de no poder ejecutar el programa Python por
# problemas de version (error ATNdeserializer), se
# pueden generar los archivos a mano.
#
# Ir a la carpeta donde esta el archivo .g4 y ejecutar 
#     antlr4 -Dlanguage=Python3 -visitor compilador.g4 -o .

def main(argv):
    archivo = "input/if.txt"
    # archivo = "input/simple.txt"
    if len(argv) > 1:
        archivo = argv[1]

    # muestra que archivo se va a procesar ()
    import os
    archivo = os.path.normpath(archivo)
    print(f"Procesando archivo: {archivo}")
    
    # Reiniciar tabla de simbolos antes de cada parseo (evita residuos)
    TablaSimbolos().reiniciar()

    # Analisis lexico, sintactico y semantico
    escucha = Escucha()
    tree = None
    parseError = None
    
    try:
        inputStream = FileStream(archivo)
        lexer = compiladorLexer(inputStream)
        stream = CommonTokenStream(lexer)
        parser = compiladorParser(stream)
        parser.addParseListener(escucha)
        tree = parser.programa()
        print(escucha)
    except FileNotFoundError as e:
        parseError = f"FileNotFoundError: {e}"
    except Exception as e:
        parseError = f"ParseError: {type(e).__name__}: {e}"

    if parseError:
        print(f"Error leyendo/parsing archivo: {parseError}")

    print("\n" + "="*50)
    
    # Generar archivos de salida requeridos (siempre actualizados para esta compilacion)
    baseName = os.path.splitext(os.path.basename(archivo))[0]

    # 1. Exportar tabla de simbolos (archivo unico, actualizado)
    # Escribe la tabla en la misma carpeta que el archivo de entrada ()
    import os as _os    #esto solo es para hacerlo dinamico
    tablaFile = _os.path.join(_os.path.dirname(archivo), "tablaSimbolos.txt") 
    from datetime import datetime
    with open(tablaFile, 'w', encoding='utf-8') as f:
        if parseError:
            f.write("No se pudo generar la tabla de simbolos por error de parseo.\n")
            f.write(f"# error: {parseError}\n")
        else:
            escucha.tabla.exportarTabla(f)
    print("Tabla de simbolos exportada")
    
    # 2. Generar codigo intermedio
    caminante = Caminante()
    
    # Exporta el archivo (se sobrescribe en cada ejecucion)
    # Escribe el codigo intermedio en la misma carpeta que el archivo de entrada ()
    codigoFile = _os.path.join(_os.path.dirname(archivo), "codigoIntermedio.txt")
    from datetime import datetime as _dt
    with open(codigoFile, 'w', encoding='utf-8') as f:
        if parseError:
            f.write("No se pudo generar codigo intermedio por error de parseo.\n")
            f.write(f"# error: {parseError}\n")
        else:
            originalStdout = sys.stdout
            sys.stdout = f
            try:
                caminante.visit(tree)
            except Exception as e:
                # Registrar el error en el archivo (ante la duda)
                sys.stdout = originalStdout
                with open(codigoFile, 'a', encoding='utf-8') as fa:
                    fa.write(f"# visitorError: {type(e).__name__}: {e}\n")
            finally:
                sys.stdout = originalStdout
    print("Codigo intermedio exportado")

    # Mostrar por consola
    print("=== CODIGO INTERMEDIO ===")
    if parseError:
        print(f"No se genero codigo intermedio: {parseError}")
    else:
        try:
            caminante.visit(tree)
        except Exception as e:
            print(f"Error generando codigo en consola: {type(e).__name__}: {e}")
    print("="*50)

if __name__ == '__main__':
    main(sys.argv)
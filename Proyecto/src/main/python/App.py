import sys
from antlr4 import *
from compiladorLexer import compiladorLexer
from compiladorParser import compiladorParser
from Escucha import Escucha
from Caminante import Caminante
from TablaSimbolos import TablaSimbolos

def main(argv):
    archivo = "input/if.txt"
    if len(argv) > 1:
        archivo = argv[1]

    import os
    archivo = os.path.normpath(archivo)
    print(f"Procesando archivo: {archivo}")
    
    TablaSimbolos().reiniciar()

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
    except FileNotFoundError as e:
        parseError = f"FileNotFoundError: {e}"
    except Exception as e:
        parseError = f"ParseError: {type(e).__name__}: {e}"

    if parseError:
        print(f"Error leyendo archivo: {parseError}")

    if not parseError:
        print("Termina el parsing")
        print(escucha)
        print("Prototipo procesado")

    print("\n" + "="*50)
    
    tablaFile = "output/tablaSimbolos.txt"
    with open(tablaFile, 'w', encoding='utf-8') as f:
        if parseError:
            f.write("No se pudo generar la tabla de simbolos por error de parseo.\n")
            f.write(f"# error: {parseError}\n")
        else:
            escucha.tabla.exportarTabla(f)
    print("Tabla de simbolos exportada")
    
    codigoIntermedio = ""
    if not parseError:
        try:
            caminante = Caminante()
            caminante.visit(tree)
            cleanOutput = caminante.codigoOriginal
            optimizado = caminante.codigoOptimizado
            
            with open("output/CodigoIntermedio.txt", 'w', encoding='utf-8') as f:
                for linea in cleanOutput:
                    f.write(linea + "\n")
            
            with open("output/CodigoOptimizado.txt", 'w', encoding='utf-8') as f:
                for linea in optimizado:
                    f.write(linea + "\n")
            
            codigoIntermedio = "\n".join(cleanOutput)
            
        except Exception as e:
            with open("output/CodigoIntermedio.txt", 'w', encoding='utf-8') as f:
                f.write(f"# Error visitando arbol: {type(e).__name__}: {e}\n")
            with open("output/CodigoOptimizado.txt", 'w', encoding='utf-8') as f:
                f.write(f"# Error optimizando: {type(e).__name__}: {e}\n")
            parseError = str(e)
    else:
        with open("output/CodigoIntermedio.txt", 'w', encoding='utf-8') as f:
            f.write(f"# No se pudo generar codigo intermedio por error de parseo.\n")
            f.write(f"# error: {parseError}\n")
        with open("output/CodigoOptimizado.txt", 'w', encoding='utf-8') as f:
            f.write(f"# No se pudo generar codigo optimizado por error de parseo.\n")
            f.write(f"# error: {parseError}\n")
    
    print("Codigo intermedio exportado")
    print("Codigo optimizado exportado")

    print("=== CODIGO INTERMEDIO ===")
    if parseError:
        print(f"No se genero codigo intermedio: {parseError}")
    else:
        print(codigoIntermedio)

if __name__ == '__main__':
    main(sys.argv)

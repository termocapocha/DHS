# === IMPORTS ===
import sys
import os
from antlr4 import *
from compiladorLexer import compiladorLexer
from compiladorParser import compiladorParser
from Escucha import Escucha
from Caminante import Caminante
from TablaSimbolos import TablaSimbolos
from errores import SintacticErrorListener

# === FLUJO PRINCIPAL ===
def main(argv):
    # === CONFIGURACION ===
    archivo = "input/test_completo.txt"
    if len(argv) > 1:
        archivo = argv[1]
    archivo = os.path.normpath(archivo)
    print(f"Procesando archivo: {archivo}")
    TablaSimbolos().reiniciar()

    escucha = Escucha()
    tree = None

    # === LEXER Y PARSER ===
    input_stream = FileStream(archivo, encoding="utf-8")
    lexer = compiladorLexer(input_stream)
    lexer.removeErrorListeners()
    tokens = CommonTokenStream(lexer)
    parser = compiladorParser(tokens)
    parser.removeErrorListeners()
    sintactic_listener = SintacticErrorListener()
    parser.addErrorListener(sintactic_listener)
    parser.addParseListener(escucha)
    tree = parser.programa()

    # === VERIFICACION DE ERRORES ===
    if sintactic_listener.hay_error:
        print("Se encontraron errores sintacticos. No se puede continuar con la generacion de codigo intermedio.")
        return
    if escucha.hay_error_semantico:
        print("Se encontraron errores semanticos. No se puede continuar con la generacion de codigo intermedio.")
        return

    print("Termina el parsing")
    print(escucha)
    print("\n" + "="*50)

    # === EXPORTACION: TABLA DE SIMBOLOS ===
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "output")
    os.makedirs(output_dir, exist_ok=True)
    tablaFile = os.path.join(output_dir, "tablaSimbolos.txt")
    with open(tablaFile, 'w', encoding='utf-8') as f:
        escucha.tabla.exportarTabla(f)
    print("Tabla de simbolos exportada")

    # === GENERACION Y OPTIMIZACION DE CODIGO ===
    caminante = Caminante()
    caminante.visit(tree)
    cleanOutput = caminante.codigoOriginal
    optimizado = caminante.codigoOptimizado

    # === EXPORTACION: CODIGO INTERMEDIO Y OPTIMIZADO ===
    with open(os.path.join(output_dir, "CodigoIntermedio.txt"), 'w', encoding='utf-8') as f:
        for linea in cleanOutput:
            f.write(linea + "\n")
    with open(os.path.join(output_dir, "CodigoOptimizado.txt"), 'w', encoding='utf-8') as f:
        for linea in optimizado:
            f.write(linea + "\n")
    print("Codigo intermedio exportado")
    print("Codigo optimizado exportado")

    print("=== CODIGO INTERMEDIO ===")
    print("\n".join(cleanOutput))

# === ENTRY POINT ===
if __name__ == '__main__':
    main(sys.argv)

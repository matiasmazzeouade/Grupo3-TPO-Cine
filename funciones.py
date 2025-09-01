# Función para imprimir matrices
def imprimir_matriz(titulo, matriz):
    print(f"{titulo.upper()}")

    # Verifica si la matriz esta vacia antes de imprimir
    if not matriz:
        print("La matriz está vacía.")
    else:
        # Calcular el ancho máximo de cada columna para un formato prolijo
        anchos_columna = []
        for item in matriz[0]:
            anchos_columna.append(len(str(item)))
        for fila in matriz:
            for i, item in enumerate(fila):
                if len(str(item)) > anchos_columna[i]:
                    anchos_columna[i] = len(str(item))

        # Imprimir encabezado
        encabezado = ""
        for i, item in enumerate(matriz[0]):
            encabezado += str(item).ljust(anchos_columna[i] + 2) + "|"
        print(encabezado)
        print("-" * len(encabezado))

        # Imprimir filas de datos
        for fila in matriz[1:]:
            linea = ""
            for i, item in enumerate(fila):
                linea += str(item).ljust(anchos_columna[i] + 2) + "|"
            print(linea)

        print("")
        print("")
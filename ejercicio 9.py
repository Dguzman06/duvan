def generar_matriz(filas, columnas):
    matriz = [[0] * columnas for _ in range(filas)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


num_filas = int(input("Ingrese el número de filas: "))
num_columnas = int(input("Ingrese el número de columnas: "))


matriz_generada = generar_matriz(num_filas, num_columnas)
print("Matriz generada:")
imprimir_matriz(matriz_generada)
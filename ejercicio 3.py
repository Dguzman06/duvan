import random

def generar_lista_aleatoria(cantidad, rango_inicio, rango_fin):
    lista_aleatoria = [random.randint(rango_inicio, rango_fin) for _ in range(cantidad)]
    return lista_aleatoria

cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))
rango_inicio = int(input("Ingrese el inicio del rango: "))
rango_fin = int(input("Ingrese el fin del rango: "))

numeros_aleatorios = generar_lista_aleatoria(cantidad_numeros, rango_inicio, rango_fin)
print("Lista de números aleatorios:", numeros_aleatorios)
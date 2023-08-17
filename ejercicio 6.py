def calcular_suma_lista(lista):
    suma = sum(lista)
    return suma


elementos = input("Ingrese los elementos de la lista separados por espacios: ")


lista_numeros = [int(elemento) for elemento in elementos.split()]


suma_total = calcular_suma_lista(lista_numeros)
print("La suma de los números en la lista es:", suma_total)
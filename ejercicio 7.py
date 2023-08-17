def encontrar_minimo_maximo(lista):
    minimo = min(lista)
    maximo = max(lista)
    return minimo, maximo


elementos = input("Ingrese los elementos de la lista separados por espacios: ")


lista_numeros = [int(elemento) for elemento in elementos.split()]


minimo, maximo = encontrar_minimo_maximo(lista_numeros)


print("El número más pequeño en la lista es:", minimo)
print("El número más grande en la lista es:", maximo)
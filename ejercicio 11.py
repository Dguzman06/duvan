def generar_lista_pares(inicio, fin):
    lista_pares = [num for num in range(inicio, fin+1) if num % 2 == 0]
    return lista_pares


lista_pares = generar_lista_pares(1, 100)
print("Lista de números pares entre 1 y 100:", lista_pares)
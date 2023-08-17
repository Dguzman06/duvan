def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida


elementos = input("Ingrese los elementos de la lista separados por espacios: ")


lista_original = elementos.split()


lista_invertida = invertir_lista(lista_original)


print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)
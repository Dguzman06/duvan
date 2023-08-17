def calcular_media_aritmetica(lista):
    if len(lista) == 0:
        return None

    suma = sum(lista)
    media = suma / len(lista)
    return media


elementos = input("Ingrese los elementos de la lista separados por espacios: ")

lista_numeros = [float(elemento) for elemento in elementos.split()]


media_aritmetica = calcular_media_aritmetica(lista_numeros)

if media_aritmetica is not None:
    print("La media aritmética de la lista es:", media_aritmetica)
else:
    print("La lista está vacía.")


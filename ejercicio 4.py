def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero_ingresado = int(input("Ingrese un número: "))


if es_par(numero_ingresado):
    print(numero_ingresado, "es un número par.")
else:
    print(numero_ingresado, "es un número impar.")



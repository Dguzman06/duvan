def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]


cadena_ingresada = input("Ingrese una cadena de texto: ")


if es_palindromo(cadena_ingresada):
    print("La cadena ingresada es un palíndromo.")
else:
    print("La cadena ingresada no es un palíndromo.")
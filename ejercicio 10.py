def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))


factorial_resultado = factorial(numero_ingresado)
print("El factorial de", numero_ingresado, "es:", factorial_resultado)
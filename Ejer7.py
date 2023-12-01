numero = int(input("Ingrese un número de dos cifras: "))

numero_invertido = (numero % 10) * 10 + numero // 10

print("El número invertido de ", numero, "es", numero_invertido)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))


if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
    if numero2 >= numero3:
        medio = numero2
        menor = numero3
    else:
        medio = numero3
        menor = numero2
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
    if numero1 >= numero3:
        medio = numero1
        menor = numero3
    else:
        medio = numero3
        menor = numero1
else:
    mayor = numero3
    if numero1 >= numero2:
        medio = numero1
        menor = numero2
    else:
        medio = numero2
        menor = numero1

print("Numeros de mayor a menor: ",mayor,",", medio,",", menor)

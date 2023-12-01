nota = float(input("Ingrese su nota: "))
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (F o M): ")


if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")

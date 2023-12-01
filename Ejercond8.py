numero_dia = int(input("Ingrese un número del 1 al 7: "))

if 1 <= numero_dia <= 7:
    if numero_dia == 1:
        print("El día correspondiente es lunes.")
    elif numero_dia == 2:
        print("El día correspondiente es martes.")
    elif numero_dia == 3:
        print("El día correspondiente es miércoles.")
    elif numero_dia == 4:
        print("El día correspondiente es jueves.")
    elif numero_dia == 5:
        print("El día correspondiente es viernes.")
    elif numero_dia == 6:
        print("El día correspondiente es sábado.")
    elif numero_dia == 7:
        print("El día correspondiente es domingo.")
else:
    print("Error: Ingrese un número del 1 al 7.")

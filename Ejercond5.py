tipo_uva = input("Ingrese el tipo de uva (A o B): ")
tamaño_uva = int(input("Ingrese el tamaño de la uva (1 o 2): "))

precio_inicial = 0

if tipo_uva == "A":
    precio_inicial = 1.2  
elif tipo_uva == 'B':
    precio_inicial = 1.5  
else:
    print("Tipo de uva no válido. Debe ser A o B.")

if tipo_uva == 'A':
    if tamaño_uva == 1:
        ganancia = precio_inicial + 0.2
    elif tamaño_uva == 2:
        ganancia = precio_inicial + 0.3
    else:
        print("Tamaño de uva no válido. Debe ser 1 o 2.")
elif tipo_uva == 'B':
    if tamaño_uva == 1:
        ganancia = precio_inicial - 0.3
    elif tamaño_uva == 2:
        ganancia = precio_inicial - 0.5
    else:
        print("Tamaño de uva no válido. Debe ser 1 o 2.")


print("\nLa ganancia obtenida por el productor es de", ganancia , "euros por kilo de uva.")

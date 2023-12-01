sueldo_base = float(input("\nIngrese el sueldo base del vendedor: "))
comision_ventas = 0.1
comision_obtenida = (sueldo_base * comision_ventas *3)
total = (sueldo_base + comision_obtenida)
print("Usted obtiene $", comision_obtenida , "dolares de comision por realizar tres ventas en el mes.")
print("El total que recibira en el mes tomando en cuenta el sueldo base y las comisiones es de $", total , "dolares.")
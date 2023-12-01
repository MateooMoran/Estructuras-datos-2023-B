cantidad_minutos = int(input("\nIngrese una cantidad de minutos: "))

horas = round(cantidad_minutos/60,2)
minutos = round(cantidad_minutos % 60,2)
print(cantidad_minutos, "minutos son ", horas , "horas y ", minutos , "minutos.")


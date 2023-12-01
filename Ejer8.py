velocidad1 = float(input("Ingrese la velocidad del vehiculo que esta detras (km/h): "))
velocidad2 = float(input("Ingrese la velocidad del vehiculo que esta adelante (km/h): "))
distancia = float(input("Ingrese la distancia entre los vehiculos (km): "))

tiempo_horas = distancia / (velocidad1 - velocidad2)
tiempo_minutos = tiempo_horas * 60

print("\nEl vehiculo que esta detras alcanzara al otro en", tiempo_minutos ,"minutos")
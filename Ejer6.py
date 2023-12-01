import math

x1 = float(input("Ingrese un punto x1 que represente un punto en el plano: "))
y1 = float(input("Ingrese un punto y2 que represente un punto en el plano: "))
x2 = float(input("Ingrese un punto x2 que represente un punto en el plano: "))
y2 = float(input("Ingrese un punto y2 que represente un punto en el plano: "))

distancia = round(math.sqrt((x2-x1)**2 + (y2-y1)**2),2)

print("Primer punto: ", {x1}, {y1})
print("Segundo punto: ", {x2},{y2})
print("\nLa distancia entre los puntos es: ",distancia)
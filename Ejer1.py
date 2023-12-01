import math

base = float(input("Ingrese la base del rectangulo :"))
altura = float(input("Ingrese la altura del rectangulo :"))

area_rectangulo = (base * altura)
perimetro_ectangulo = 2 * (base + altura)

print("El perimetro de su rectangulo es: ", perimetro_ectangulo)
print("El área de su rectangulo es: ", area_rectangulo)


radio = float(input("\nIngrese el radio de su circulo: "))

area_circulo = round(math.pi * pow(radio,2),2)
perimetro_circulo = round(2 *math.pi * radio, 2)

print("El perimetro de su circulo es: ", perimetro_circulo)
print("El area de su circulo es: ", area_circulo)

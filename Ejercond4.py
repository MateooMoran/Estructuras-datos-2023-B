A = float(input("Ingrese la longitud del lado A: "))
B = float(input("Ingrese la longitud del lado B: "))
C = float(input("Ingrese la longitud del lado C: "))


if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
    tipo_trianguo = "triángulo rectángulo"
elif A == B and B == C:
    tipo_trianguo = "triángulo equilátero"
elif A == B or A == C or B == C:
    tipo_trianguo = "triángulo isósceles"
else:
    tipo_trianguo = "triángulo escaleno"

print("\nEl triángulo con lados de ", {A}, {B}, {C}, "es un" ,tipo_trianguo)

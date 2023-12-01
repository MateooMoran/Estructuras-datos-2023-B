num_alumnos = int(input("Ingrese el número de alumnos: "))

costo_alumno = 0
costo_compania = 0

if num_alumnos >= 100:
    costo_alumno = 65
elif 50 <= num_alumnos <= 99:
    costo_alumno = 70
elif 30 <= num_alumnos <= 49:
    costo_alumno = 95
else:
    costo_compania = 4000

total_pagar_compania = num_alumnos * costo_alumno + costo_compania

print("\nCada alumno debe pagar:, ",costo_alumno, "euros.")
print("El total a pagar a la compañía de autobuses es de ",total_pagar_compania, "euros.")

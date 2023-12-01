nombre_estudiante = input("Ingrese el nombre del estudiante: ")

nota_ingles = float(input("Ingrese la nota de Inglés: "))

if 9 <= nota_ingles <= 10:
    mensaje = "Felicitaciones: ",nombre_estudiante, "su nota es",{nota_ingles}, "equivalente a excelente."
elif 7 <= nota_ingles <= 8:
    mensaje = "Siga adelante: ",nombre_estudiante, "su nota es",{nota_ingles}, "equivalente a muy buena."
elif 5 <= nota_ingles <= 6:
    mensaje = "Debe esforzarse más: ",nombre_estudiante, "su nota es",{nota_ingles}, "equivalente a buena."
elif 0 <= nota_ingles <= 4:
    mensaje = "Usted puede reprobar, ",nombre_estudiante, "su nota es",{nota_ingles}, "equivalente a regular."

print(mensaje)

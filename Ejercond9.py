def dimeTipoMotor(tipo_motor):
    switch = {
        0: "No hay establecido un valor definido para el tipo de bomba",
        1: "La bomba es una bomba de agua",
        2: "La bomba es una bomba de gasolina",
        3: "La bomba es una bomba de hormigón",
        4: "La bomba es una bomba de pasta alimenticia",
    }
    mensaje = switch.get(tipo_motor, "No existe un valor válido para tipo de bomba")
    print(mensaje)

tipo_motor = int(input("Ingrese el tipo de motor (1, 2, 3, 4): "))
dimeTipoMotor(tipo_motor)

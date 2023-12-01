
monedade1 = int(input("Ingrese cuantas monedas de 1 euro tiene: "))
monedade2 = int(input("Ingrese cuantas monedas de 2 euros tiene: "))
monedade10 = int(input("Ingrese cuantas monedas de 10 centimos tiene: "))
monedade20 = int(input("Ingrese cuantas monedas de 20 centimos tiene: "))
monedade50 = int(input("Ingrese cuantas monedas de 50 centimos tiene: "))

dinero_euros = (monedade1 * 1) + (monedade2 * 2) + (monedade10 * 0.1) + (monedade20 * 0.2) + (monedade50 * 0.5)
dinero_centimos = dinero_euros * 100

print("Tiene",int(dinero_euros), "euros y",int(dinero_centimos), "centimos.")

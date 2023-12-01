#Operadores de pertennecia

lista = [1,3,2,7,8,9,6]
4 in lista
3 in lista
4 not in lista 

#Operadores de identidad
x = 4
y = 2
lista = [1, 5]
x is lista
x is y
x is 4

#Comentarios
print("hola")
#esto es un comentario"

"""hola esto
es un
comentario
s
s
s
"""

#Tipos de datos
#enteros int
a = -1
b = a + 2
print(b)

#flotantes float
c = 1.1 + 2.2
print(c)
real = 1.1 + 2.2
print(real) 
print(f'{real:.2f}')
un_real = 1.1
otro_real = 1/2
not_client = 1.23E3
print(un_real)
print(otro_real)
print(not_client)

#complex
complejo = 1+2j
complejo.real
complejo.imag
print(complejo.real)
print(complejo.imag)

#bool
""" valores true or false"""

#cadenas
caracter_a = 'a'
print(caracter_a)
hola = 'Hola "Pythonista", soy Mateo'
hola_2 = 'Hola /Pythonista/'', soy Mateo'
hola_3 = "Hola 'Pythonista', soy Mateo"

print(hola)
print(hola_2)
print(hola_3)

#Otros tipos de datos
lista = [1,2,3,8,9]
tuple = [1,4,8,0,5]
conjunto = set ([1,3,1,4])
diccionario = {"a": 1,"b": 3,"z": 8}
print(lista)
print(tuple)
print(conjunto)
print(diccionario)

# Tipo de una variable
type (3)
print (type (3))
type(2.78)
print (type (2.78))
type("hola")
print (type ("hola"))
isinstance(3, float)
isinstance(3, int)
isinstance(3, bool)
isinstance(False, bool)


#Tipo de variable
    #Tipo de dato entero o largo
numero = 15
print(numero, type(numero))

    #Tipo de dato flotante
numero_flotante = 15.5
print(numero_flotante, type(numero_flotante))

    #Tipo de dato numero complejo
numero_complejo = 5 +6j
print(numero_complejo, type(numero_complejo))

    #Tipo de dato string
nombre = "Mateo Moran"
print(nombre, type(nombre))

    #Tipo de dato booleano
verdadero_falso = 3 == 3
print(verdadero_falso, type(verdadero_falso))

#Conversion de tipos
edad = "25"
edad = int(edad) + 10
print(edad)

edad = str(edad)
float ("18.66")
print(float)

#Insertar datos por teclado
mensaje = input("Introduce tu nombre: ")
numeroEntero = int(input("Introduce un numero entero: "))
numeroFlotante = float(input("Introduce un numero flotante: "))
numeroComplejo = complex(input("Introduce un numero complejo: "))
print("Bienvenido", mensaje)
print("El numero entero introducido es: ", numeroEntero)
print("El numero flotante introducido es: ", numeroFlotante)
print("El numero complejo introducido es: ", numeroComplejo)

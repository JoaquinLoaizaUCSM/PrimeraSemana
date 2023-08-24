"""Diseñe algoritmo que ingrese nombre y edad de dos personas, para finalmente mostrar
quien es mayor y por cuantos años. (Considere edad máxima 110 años)
"""


def ingreso_datos():
    nombre = input("Ingrese su nombre: ")
    while True:
        edad = int(input("Ingrese su edad: "))
        if edad <= 110:
            break
        print("Vuelve a ingresar la edad")
    return nombre, edad


def edadMayor(nombre1, edad1, nombre2, edad2):
    if edad1 > edad2:
        print(nombre1, "es mayor que", nombre2, "por", edad1 - edad2, "años")
    elif edad1 < edad2:
        print(nombre2, "es mayor que", nombre1, "por", edad2 - edad1, "años")
    else:
        print(nombre1, "y", nombre2, "tienen la misma edad")


nombre1, edad1 = ingreso_datos()
nombre2, edad2 = ingreso_datos()
edadMayor(nombre1, edad1, nombre2, edad2)

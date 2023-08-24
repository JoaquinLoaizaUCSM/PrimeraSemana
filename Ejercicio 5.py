"""Diseñe algoritmo donde un usuario ingrese un Nombre y un Apellido y el programa
indique cuantas vocales contiene su nombre y apellido (Ejemplo, si ingreso Rodrigo Soto
mostrar 3 vocales en el apellido y 2 vocales en el nombre)"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

vocales = "aeiouAEIOU"
vocales_nombre = 0
vocales_apellido = 0

for letra in nombre:
    if letra in vocales:
        vocales_nombre += 1
for letra in apellido:
    if letra in vocales:
        vocales_apellido += 1

print("Su nombre tiene", vocales_nombre, "vocales")
print("Su apellido tiene", vocales_apellido, "vocales")

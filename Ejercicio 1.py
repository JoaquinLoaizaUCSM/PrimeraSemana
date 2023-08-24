"""Algoritmo que lea dos números y nos diga cuál de ellos es el menor y por cuantas
unidades o bien si son iguales recuerda usar la estructura condicional SI ENTONCES"""


num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 < num2:
    print(num1, "es menor que por", num2 - num1, "unidades")
elif num1 > num2:
    print(num2, "es menor que por", num1 - num2, "unidades")
else:
    print(num1, "Los numeros son iguales")

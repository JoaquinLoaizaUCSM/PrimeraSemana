"""Algoritmo que lea tres números distintos y nos diga cuál de ellos es el mayor (utilice la
estructura condicional Si y operadores lógicos)."""


numeros = []

for i in range(3):
    numero = float(input(f"Introduce el número {i + 1}: "))
    numeros.append(numero)

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("Mayor:", mayor)

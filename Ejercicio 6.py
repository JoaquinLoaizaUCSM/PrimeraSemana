"""Crea un juego en el que generes un número aleatorio y el usuario debe adivinarlo, debe
brindarles pistas al usuario sobre cuál podría ser el numero como indicar si es un
número mayor o menor"""

import random


def adivina_numero(numero):
    intentos = 0
    while intentos < 5:
        intentos += 1
        print("Intento", intentos)
        adivinanza = int(input("Adivina un numero: "))
        if adivinanza == numero:
            print("Correcto")
            break
        elif adivinanza > numero:
            print("El numero es menor")
        else:
            print("El numero es mayor")
    print("El numero era", numero)


numeroAletorial = random.randint(0, 100)
adivina_numero(numeroAletorial)

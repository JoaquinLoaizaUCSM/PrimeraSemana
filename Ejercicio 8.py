"""Crea un juego en el que el jugador debe adivinar una palabra oculta antes de que se
agoten los intentos, le deben indicar el tamaño de la palabra y cuantas letras son
correctas"""


def palabras_adivinadas(palabra, adivinanza):
    correctos = []
    for i in range(len(adivinanza)):
        if adivinanza[i] in palabra:
            correctos += adivinanza[i]
    return print(f"Palabras correctas:\n{','.join(correctos)}")


def adivinar_palabra(cadena):
    adivinanza = input("Adivina una palabra: ")
    if adivinanza == cadena:
        print("Correcto")
        return True
    else:
        return palabras_adivinadas(cadena, adivinanza)


def inicio(palabra, intentos):
    while intentos > 0:
        intentos -= 1
        print(f"Intento numero:{intentos + 1}")
        if adivinar_palabra(palabra):
            break
    print("La palabra es", palabra)


ingrsoPalabra = input("Ingrese una palabra: ")
numeroIntentos = int(input("Ingrese el numero de intentos: "))

inicio(ingrsoPalabra, numeroIntentos)

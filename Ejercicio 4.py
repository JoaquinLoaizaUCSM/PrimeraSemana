"""Crear un algoritmo que al ingresar un número del 1 al 7, muestre un día de la semana
hasta que se ingrese un numero diferente y terminaría el algoritmo (Ejemplo, si ingreso
2 debe mostrar MARTES)"""

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

while True:
    numero = int(input("Ingrese un numero del 1 al 7: "))
    if numero in range(1, 8):
        print(dias[numero - 1])
    else:
        break

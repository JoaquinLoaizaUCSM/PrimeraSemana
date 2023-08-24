"""Desarrolla un programa que permita al usuario agregar, eliminar y mostrar elementos
de una lista de tareas pendientes."""

import os


def agregar_tarea(tareas):
    tarea = input("Ingrese una tarea: ")
    if tarea:
        tareas.append(tarea)
        print("Tarea agregada")
        return tareas
    else:
        print("Ingrese por favor la tarea")
        agregar_tarea(tareas)
        return tareas


def eliminar_tarea(tareas):
    tarea = input("Ingrese una tarea a eliminar: ")
    if tarea in tareas:
        tareas.pop(tareas.index(tarea))
        return print("Tarea eliminada")
    else:
        print("Tarea no encontrada")
        eliminar_tarea(tareas)
        return tareas


def mostrar_tareas(tareas):
    if tareas:
        for num in tareas:
            print(f"{tareas.index(num) + 1}) {num}")
    else:
        print("No hay tareas pendientes")


listaTareas = []
opcion = 0
while opcion != 4:
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        listaTareas = agregar_tarea(listaTareas)

    elif opcion == 2:
        if listaTareas:
            eliminar_tarea(listaTareas)
        else:
            print("No hay tareas pendientes")

    elif opcion == 3:
        mostrar_tareas(listaTareas)

    elif opcion == 4:
        print("Programa finalizado")
        break

    else:
        print("Opción no válida")

    input("Pulse para continuar...")
    os.system("cls")

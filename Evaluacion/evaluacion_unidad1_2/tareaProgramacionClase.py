# Creamos una lista vacía donde guardaremos las tareas
tareas = []

# Variable para controlar el menú
opcion = ""

# Controla cuando usuario desee SALIR - 4
while opcion != "4":

    # Mostramos menú
    print("\n--- LISTA DE TAREAS DE LA FÁBRICA ---")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    # Pedimos una opción al usuario
    opcion = input("Elige una opción: ")


    # OPCIÓN 1 -> AÑADIR TAREA
    if opcion == "1":

        # Pedimos nombre de tarea
        nueva_tarea = input("Escribe la nueva tarea: ")

        # Añadimos tarea a lista
        tareas.append(nueva_tarea)

        # Mensaje confirmación
        print("Tarea añadida correctamente.")


    # OPCIÓN 2 -> VER TAREAS
    elif opcion == "2":

        # Comprobamos lista está vacía
        if len(tareas) == 0:
            print("No hay tareas registradas.")

        else:
            print("\nTAREAS PENDIENTES:")

            # Recorremos lista mostrando tarea
            for i in range(len(tareas)):
                print(i + 1, "-", tareas[i])


    # OPCIÓN 3 -> ELIMINAR TAREA
    elif opcion == "3":

        # Verificamos antes eliminar
        if len(tareas) == 0:
            print("No hay tareas para eliminar.")

        else:
            print("\nTAREAS ACTUALES:")

            # Mostramos tareas numeradas
            for i in range(len(tareas)):
                print(i + 1, "-", tareas[i])

            # Pedimos número de tarea a eliminar
            numero = int(input("Número de tarea a eliminar: "))

            # Eliminamos tarea
            tareas.pop(numero - 1)

            print("Tarea eliminada correctamente.")

    # OPCIÓN 4 -> SALIR
    elif opcion == "4":

        print("Programa finalizado.")



    # OPCIÓN INCORRECTA
    else:

        print("Opción no válida.")
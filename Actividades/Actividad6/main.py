# Importamos las clases
from deportes.futbol import Futbolista
from deportes.baloncesto import Baloncesto
from deportes.natacion import Nadador

# Lista para guardar deportistas
deportistas = []



# =========================================
# FUNCIONES DE CONTROL DATO INTRODUCIDO
# =========================================

# Control de introducir núm en menú y edad
def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número, por favor.")

# Control de altura J.Baloncesto
def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: introduce un número válido (ej: 1.85 ó 2), por favor.")



# =================================
#    MENÚ PRINCIPAL APLICACIÓN
# =================================
opcion = 0

while opcion != 4:

    print("\n===== MENÚ =====")
    print("1. Crear Futbolista")
    print("2. Crear Jugador Baloncesto")
    print("3. Crear Nadador")
    print("4. Salir")

    opcion = pedir_int("Seleccione una opción: ")

    # FUTBOL
    if opcion == 1:

        nombre = input("Nombre: ")
        edad = pedir_int("Edad: ")
        pais = input("País: ")
        posicion = input("Posición: ")

        futbolista = Futbolista(nombre, edad, pais, posicion)
        deportistas.append(futbolista)

        print("✔ Futbolista creado.")

    # BALONCESTO
    elif opcion == 2:

        nombre = input("Nombre: ")
        edad = pedir_int("Edad: ")
        pais = input("País: ")
        altura = pedir_float("Altura en metros: ")

        JBaloncesto = Baloncesto(nombre, edad, pais, altura)
        deportistas.append(JBaloncesto)

        print("✔ Jugador baloncesto creado.")

    # NATACIÓN
    elif opcion == 3:

        nombre = input("Nombre: ")
        edad = pedir_int("Edad: ")
        pais = input("País: ")
        estilo = input("Estilo de natación: ")

        nadador = Nadador(nombre, edad, pais, estilo)
        deportistas.append(nadador)

        print("✔ Nadador creado.")

    # SALIR
    elif opcion == 4:
        print("\nSaliendo del programa...")

    else:
        print("Opción no válida")


# MOSTRAR RESULTADOS
print("\n===== DEPORTISTAS CREADOS =====")

for deportista in deportistas:
    deportista.mostrar_datos()
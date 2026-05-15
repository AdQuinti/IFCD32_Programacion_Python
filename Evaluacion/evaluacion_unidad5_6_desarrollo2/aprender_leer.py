import random # libreria pedir aleatorio

# Lista practicar lectura
palabras = ["casa", "perro", "escuela", "libro", "mesa"]


# FUNCIÓN: mostrar menú
def mostrar_menu():
    print("\n=== PROGRAMA DE LECTURA ===")
    print("1. Ver palabras")
    print("2. Practicar lectura")
    print("3. Salir")



# FUNCIÓN: mostrar palabras
def ver_palabras():
    print("\nPalabras disponibles:")

    for palabra in palabras: # recorre palabras
        print("-", palabra) # mostramos


# FUNCIÓN: practicar lectura
def practicar_lectura():
    palabra = random.choice(palabras)     # Elegimos palabra al azar
    respuesta = input("Escribe la palabra que ves: " + palabra + " -> ") # petición por teclado

    if respuesta == palabra: # ssi es correcta
        print("¡Correcto! Muy bien 😊")
    else:
        print("Casi... la palabra era:", palabra)



# PROGRAMA PRINCIPAL
# Variable para controlar el menú
opcion = ""

while opcion != "3": # mientras no pida salir, muestra menu
    mostrar_menu()

    # try/except evitamos que no introduzca lo que pedimos
    try:
        opcion = input("Elige una opción: ")
        if opcion == "1": # OPCIÓN VER
            ver_palabras()
        elif opcion == "2": # OPCIÓN PRACTICAR
            practicar_lectura()
        elif opcion == "3": # OPCIÓN SALIR
            print("Saliendo del programa...")
        else: # OPCIÓN NO VÁLIDA
            print("Opción no válida. Intenta otra vez.")

    # control errores inesperados
    except Exception as error:
        print("Ha ocurrido un error, pero el programa sigue funcionando.")
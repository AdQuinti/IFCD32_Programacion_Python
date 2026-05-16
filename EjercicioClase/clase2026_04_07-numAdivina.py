''' Enunciado:
El programa “piensa” un número secreto y el usuario debe adivinarlo.
El programa indica si el intento es demasiado alto, demasiado bajo o correcto. Entre 1 al 25.'''

import random

# programa "calcula" un número secreto entre 1 y 25
num_secreto = random.randint(1, 25)

print("PROGRAMA ADIVINA EL NÚMERO")

# Bucle principal para que el usuario intente hasta que acierte
while True:
      try:
            num = int(input("\nIntroduce número entre 1 a 25: "))
      except ValueError: # control si introduce txt en vez de número
            print("Error: ¡Debes introducir un número entero, no puede ser ni con decimales y ni texto!")
            continue  # Vuelve al principio del bucle sin romper el programa
  
      # Validar que el número esté dentro del rango correcto (1 al 25)
      if num < 1 or num > 25:
            print("Por favor, introduce un número válido entre 1 y 25.")
            continue  # Salta el resto del bucle y vuelve a pedir el número
                  
      # 3. Comprobar el intento del usuario e indicar las pistas
      if num < num_secreto:
            print("Demasiado bajo. ¡Inténtalo de nuevo!")
      elif num > num_secreto:
            print("Demasiado alto. ¡Inténtalo de nuevo!")
      else:
            print(f"¡Correcto! Has adivinado el número secreto: {num_secreto}\n")
            break  # Rompe el bucle porque ya acertó
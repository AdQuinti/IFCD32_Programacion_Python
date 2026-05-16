''' Enunciado:
Dado un número entero mayor que 1, determinar si es primo (solo divisible por 1 y por símismo) '''

print("COMPROBADOR DE NÚMEROS PRIMOS")

while True:
    try:
        # PEDIR NÚMERO
        num = int(input("\nIntroduce un número entero mayor que 1: "))
        
        # COMPROBAR
        if num <= 1:
            print("Error: El número debe ser mayor que 1.")
            continue
            
        break # Si es un número válido, salimos del bucle de captura
    except ValueError:
        print("Error: Debes introducir un número entero, no texto.")

# Determinar si es primo
es_primo = True

# Buscamos divisiones exactas desde 2 hasta num - 1
for i in range(2, num):
    if num % i == 0:
        es_primo = False
        break # Encontrado un divisor, no hace falta seguir buscando

# Mostrar el resultado
if es_primo:
    print(f"El número {num} SÍ es primo.\n")
else:
    print(f"El número {num} NO es primo (es divisible por {i}).\n")
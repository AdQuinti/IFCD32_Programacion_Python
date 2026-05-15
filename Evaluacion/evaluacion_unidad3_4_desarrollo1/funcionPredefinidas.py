# FUNCIÓN SUMAR
def sumar(a, b):
    return a + b     # Retornamos suma 

# FUNCIÓN RESTAR 
def restar(a, b):
    return a - b     # Retornamos resta

# FUNCIÓN MULTIPLICAR
def multiplicar(a, b):
    return a * b # Retornamos multiplicación

# FUNCIÓN DIVIDIR 
def dividir(a, b):
    # Verificamos que el divisor no sea 0
    if b != 0:
        return a / b  # Retornamos división
    else:
        # Mensaje de error
        print("No se puede dividir entre 0")
        return 0 # Retornamos para evitar error


# Pedimos números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))




# UTILIZAMOS LAS FUNCIONES


# Guardamos el resultado de la suma
resultado_suma = sumar(numero1, numero2)

# Mostramos el resultado
print("La suma es:", resultado_suma)


# Guardamos el resultado de la resta
resultado_resta = restar(numero1, numero2)

# Mostramos el resultado
print("La resta es:", resultado_resta)


# Guardamos el resultado de la multiplicación
resultado_multiplicacion = multiplicar(numero1, numero2)

# Mostramos el resultado
print("La multiplicación es:", resultado_multiplicacion)


# Guardamos el resultado de la división
resultado_division = dividir(numero1, numero2)

# Mostramos el resultado
print("La división es:", resultado_division)




# USANDO EL RESULTADO DE UNA FUNCIÓN EN OTRA

# Primero sumamos los números
suma_total = sumar(numero1, numero2)

# Después multiplicamos el resultado de la suma por 2
resultado_final = multiplicar(suma_total, 2)

# Mostramos el resultado final
print("El resultado de (suma * 2) es:", resultado_final)
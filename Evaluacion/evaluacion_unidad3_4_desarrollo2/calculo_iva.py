# FUNCIÓN: calcular IVA
def calcular_iva(precio):
    iva = precio * 0.21 # IVA al 21%
    return iva     # Devolvemos importe del IVA

# FUNCIÓN: precio final con IVA incluido
def precio_con_iva(precio):
    iva = calcular_iva(precio) # calculamos IVA
    total = precio + iva # sumamos IVA al precio producto
    return total # devolvemos precio con iva

# FUNCIÓN: calcular IRPF (ejemplo simple)
def calcular_irpf(sueldo):
    irpf = sueldo * 0.15  # IRPF fijo del 15%
    return irpf # devolvemo impuesto

# FUNCIÓN: sueldo neto
def sueldo_neto(sueldo):
    impuesto = calcular_irpf(sueldo) # Calculamos el IRPF
    neto = sueldo - impuesto # Restamos impuesto al sueldo bruto
    return neto # Devolvemos sueldo



# PROGRAMA PRINCIPAL
# Pedimos al usuario un precio de producto
precio = float(input("Introduce el precio del producto: "))

# Mostramos el IVA
print("El IVA es:", calcular_iva(precio))

# Mostramos el precio final con IVA
print("Precio final con IVA:", precio_con_iva(precio))


# Pedimos el sueldo de una persona
sueldo = float(input("\nIntroduce el sueldo: "))

# Mostramos el IRPF
print("El IRPF es:", calcular_irpf(sueldo))

# Mostramos el sueldo neto
print("Sueldo neto:", sueldo_neto(sueldo))
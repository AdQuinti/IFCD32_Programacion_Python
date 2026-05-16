''' ESTE ES COMENTARIO
MULTILINEA '''
# COMENTARIO UNA LÍNEA




# declaración variables
name = "José Antonio"
password = "Dbgiuio38948X$ag"
address = "avenida de la constitución"
text = "   Hola Mundo   "
email = "usuario@gmail.com"

# longitud de la cadena
print("La longitud de la contraseña es: ", len(password))
print("-------------------")
# primer carácter (índice 0)
print("El primer carácter de la contraseña es: ", password[0])
print("-------------------")
# último carácter
print("El último carácter de la contraseña es: ", password[-1])
print("-------------------")
# repetir cadena y concatenar
print("Concatenación y repetición: ", "ja" * 3 + password)
print("-------------------")
# convertir texto a minúsculas
print("Nombre en minúsculas: ", name.lower())
print("-------------------")
# convertir texto a mayúsculas
print("Nombre en mayúsculas: ", name.upper())
print("-------------------")
# convertir texto tipo título
print("La primera de cada palabra en mayuscula: ", address.title())
print("-------------------")
# primera letra en mayúscula
print("Primera palabra de cadena solo en mayuscula: ", name.capitalize())
print("-------------------")

# strip() → separar datos
print("Resultado de strip():")
print(text.strip())
print("-------------------")

# replace() → limpiar texto
print("Resultado de replace():")
print(text.replace("Mundo", "Python"))
print("-------------------")

# split() → quitar espacios
print("Resultado de split():")
print(email.split("@"))
print("-------------------")

# join() → construir texto
words = ["Hola", "Python"]
print("Resultado de join():")
print(" - ".join(words))
print("-------------------")

# find() → buscar
print("Resultado de find():")
print(text.find("Hola"))
print("-------------------")

# startswith()  → validar
print("Resultado de startswith():")
print(email.startswith("usuario"))
print("-------------------")

# endswith() → validar
print("Resultado de endswith():")
print(email.endswith(".com"))
print("-------------------")

# isdigit() → devuelve True si todo son números.
print("¿La cadena tiene solo números?")
print("1234".isdigit())
print("-------------------")

# isalpha() → devuelve True si todo son letras.
print("¿La cadena tiene solo letras?")
print("Python".isalpha())
print("-------------------")

# isalnum() → devuelve True si hay letras y números pero sin espacios ni símbolos
print("¿La cadena tiene letras y números sin espacios?")
print("Python123".isalnum())
print("-------------------")

# count() → cuenta cuántas veces aparece un carácter.
print("¿Cuántas veces aparece la letra 'o'?")
print(text.count("o"))
print("-------------------")

# center()  → centra un texto rellenando con caracteres.
print("Texto centrado con guiones:")
print("Python".center(20, "-"))
print("-------------------")

# zfill() → añade ceros delante.
print("Rellenar con ceros a la izquierda:")
print("25".zfill(5))
print("-------------------")

# f-string → inserta variables dentro de un texto fácilmente.
print("Mostrar variables dentro de un texto:")
print(f"Mi nombre es {name} y vivo en {address}")
print("-------------------")

# PETICIÓN POR TECLADO Y CONDICIONAL IF y ELIF
age = input("¿Tú edad? ") # pedir por teclado

if age.isdigit():
      age = int(age) # convertir String introducido a número

      if type(age) == float: # float es núm. decimales
             # \n provoca salto linea
             # f nos ayuda a introducir nuestra variale introducida para imprimir
            print(f"Error, la edad introducida no puede tenr decimales. Has introducido {age}.\n") 
      elif type (age >= 18):
            print(f"Eres mayor edad. Tienes {age} años.\n")
      else:
            print(f"Eres menor edad. Tienes {age} años.\n")
else:
      print(f"Has introducido texto: {age}, se pide un número.\n")
      
      
print("-------------------\ncambio espacio por guion con sep y abajo con replace()")
# colocacion separador entre palabras
print("Málaga", "Granada", address, "Jaén", sep="-") # solo funciona entre string no dentro de variables
# para que funcione en variable debe ser con replace()
address_modificada = address.replace(" ", "-") # cambia espacio por guión
print("\nMálaga", "Granada", address_modificada, "Jaén", sep="-")
print("-------------------")
# colocacion espacio y no salte linea
print("\nQuitamos salto linea")
print("Hoy es", end=" ") # si espacio vacio "" con espacio en medio " "
print("Martes\n")

print("-------------------")
''' Ejemplo de mensaje de compra:
      A partir de los datos del precio unitario del artículo y la cantidad comprada, 
      vamos a generar un mensaje con el importe total y el número de unidades compradas'''
quantity = 4
article = "Teclado mecánico"
unitary_price = 25.75
print(f"Su compra han sido: {quantity} {article}, por un importe total de {quantity * unitary_price} €.\n")
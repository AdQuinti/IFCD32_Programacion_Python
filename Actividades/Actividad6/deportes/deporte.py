# Clase padre

class Deportista:

    # Constructor de la clase
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    # Método para mostrar datos
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"País: {self.pais}")
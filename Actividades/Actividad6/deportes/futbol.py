from deportes.deporte import Deportista

# Clase hija Futbolista
class Futbolista(Deportista):

    def __init__(self, nombre, edad, pais, posicion):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, edad, pais)

        self.posicion = posicion

    # Sobrescribimos el método
    def mostrar_datos(self):
        print("\n--- FUTBOLISTA ---")
        super().mostrar_datos()
        print(f"Posición: {self.posicion}")
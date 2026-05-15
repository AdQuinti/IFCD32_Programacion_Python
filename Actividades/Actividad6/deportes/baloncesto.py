from deportes.deporte import Deportista

class Baloncesto(Deportista):

    def __init__(self, nombre, edad, pais, altura):
        super().__init__(nombre, edad, pais)
        self.altura = altura

    def mostrar_datos(self):
        print("\n--- JUGADOR BALONCESTO ---")
        super().mostrar_datos()
        print(f"Altura: {self.altura} metros")
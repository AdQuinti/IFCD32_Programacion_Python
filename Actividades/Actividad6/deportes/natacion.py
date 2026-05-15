from deportes.deporte import Deportista

# Clase hija Nadador
class Nadador(Deportista):

    def __init__(self, nombre, edad, pais, estilo):
        super().__init__(nombre, edad, pais)

        self.estilo = estilo

    def mostrar_datos(self):
        print("\n--- NADADOR ---")
        super().mostrar_datos()
        print(f"Estilo: {self.estilo}")
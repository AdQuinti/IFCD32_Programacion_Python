# plantilla jugadores
class Jugador:

    # Constructor: se ejecuta al crear un jugador
    def __init__(self, nombre, posicion, bateo):
        # Guardamos los datos del jugador
        self.nombre = nombre
        self.posicion = posicion
        self.bateo = bateo

    # Método para mostrar información del jugador
    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Posición:", self.posicion)
        print("Nivel de bateo:", self.bateo)


# Creamos jugadores
jugador1 = Jugador("Carlos", "Lanzador", 80)
jugador2 = Jugador("Luis", "Bateador", 90)
jugador3 = Jugador("Pedro", "Catcher", 75)

# Mostramos
jugador1.mostrar_info()
print("--------------------")
jugador2.mostrar_info()
print("--------------------")
jugador3.mostrar_info()
print("--------------------")
class ElementoMapa:
    def __init__(self):
        pass

class Habitacion(ElementoMapa):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def establecer_lado(self, direccion, elemento):
        setattr(self, direccion, elemento)

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2, abierta=False):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = abierta

class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = {}

    def agregar_habitacion(self, habitacion):
        self.habitaciones[habitacion.num] = habitacion

    def obtener_habitacion(self, num):
        return self.habitaciones.get(num)

class Juego:
    def __init__(self):
        self.laberinto = Laberinto()

    def crear_laberinto(self):
        h1 = Habitacion(1)
        h2 = Habitacion(2)
        
        p = Puerta(h1, h2)
        
        h1.establecer_lado("norte", Pared())
        h1.establecer_lado("sur", Pared())
        h1.establecer_lado("este", p)
        h1.establecer_lado("oeste", Pared())
        
        h2.establecer_lado("norte", Pared())
        h2.establecer_lado("sur", Pared())
        h2.establecer_lado("este", Pared())
        h2.establecer_lado("oeste", p)
        
        self.laberinto.agregar_habitacion(h1)
        self.laberinto.agregar_habitacion(h2)

    def jugar(self):
        print("¡Bienvenido al laberinto!")
        actual = self.laberinto.obtener_habitacion(1)
        while True:
            print(f"Estás en la habitación {actual.num}")
            movimiento = input("¿A dónde quieres ir? (norte/sur/este/oeste/salir): ").lower()
            if movimiento == "salir":
                print("¡Gracias por jugar!")
                break
            siguiente = getattr(actual, movimiento, None)
            if isinstance(siguiente, Puerta) and siguiente.abierta:
                actual = siguiente.lado2 if actual == siguiente.lado1 else siguiente.lado1
            elif isinstance(siguiente, Habitacion):
                actual = siguiente
            else:
                print("No puedes ir en esa dirección.")

if __name__ == "__main__":
    juego = Juego()
    juego.crear_laberinto()
    juego.jugar()

class ElementoMapa:
    def __init__(self):
        pass

    def entrar(self):
        pass

class Decorator(ElementoMapa):
    def __init__(self, em):
        super().__init__()
        self.em = em


class Bomba(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.activa = False

    def esBomba(self):
        return True
    

class Bicho:
    def __init__(self, vidas, poder, posicion, modo):
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion
        self.modo = modo

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.poder = 1
        self.vidas = 5

class Modo:
    def __init__(self):
        pass

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

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
        
    def entrar(self):
        print(f"Entrando en la habitación {self.num}")

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("Entrando en una pared")

    



class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        print("Entrando en una pared bomba")





class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False

    def entrar(self):
        print("Entrando en una puerta")

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = {}
    
    def entrar(self):
        print("Entrando en el laberinto")

    def agregar_habitacion(self, habitacion):
        self.habitaciones[habitacion.num] = habitacion

    def obtener_habitacion(self, num):
        return self.habitaciones.get(num)

 


class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bicho = []

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    def iniciar_juego(self):
        # Lógica para iniciar el juego
        pass

    def crearLaberinto2HabFM(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        return laberinto
    

    def crearLaberinto2HabBomba(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)

        habitacion1.sur = puerta
        habitacion2.norte = puerta

        pared1 = creator.crear_pared()
        bomba1 = creator.crear_bomba(pared1)
        habitacion1.este = bomba1

        pared2 = creator.crear_pared()
        bomba2 = creator.crear_bomba(pared2)
        habitacion2.oeste = bomba2

        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        return laberinto

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)
    

    def crearLaberinto4Hab(self, creator):
        laberinto = creator.crear_laberinto()

        hab1 = creator.crear_habitacion(1)
        hab2 = creator.crear_habitacion(2)
        hab3 = creator.crear_habitacion(3)
        hab4 = creator.crear_habitacion(4)

        puerta1 = creator.crear_puerta(hab1, hab2)
        puerta2 = creator.crear_puerta(hab1, hab3)
        puerta3 = creator.crear_puerta(hab2, hab4)
        puerta4 = creator.crear_puerta(hab3, hab4)

        hab1.sur = puerta1
        hab1.este = puerta2
        hab3.oeste = puerta2
        hab3.sur = puerta4
        hab2.norte = puerta1
        hab2.este = puerta3
        hab4.norte = puerta4
        hab4.oeste = puerta3

        bicho1 = creator.crear_bicho(5, 10, hab1, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho1)
        bicho3 = creator.crear_bicho(5, 10, hab3, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho3)
        bicho2 = creator.crear_bicho(5, 1, hab2, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho2)
        bicho4 = creator.crear_bicho(5, 1, hab4, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho4)

        hab1.bicho = bicho1
        hab2.bicho = bicho2
        hab3.bicho = bicho3
        hab4.bicho = bicho4

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        laberinto.agregar_habitacion(hab3)
        laberinto.agregar_habitacion(hab4)

        return laberinto


import copy
from laberinto import Laberinto
from bicho import Bicho
from habitacion import Habitacion
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from orientacion import Orientacion
from agresivo import Agresivo
from perezoso import Perezoso
from pared import Pared
from bomba import Bomba
from pared_bomba import ParedBomba
from ente import Personaje

class Juego:
    def __init__(self):
        self.habitaciones = {}
        self.bichos = []
        self.prototipo = None
        self.personaje=None
        self.bicho_threads = {}

    def agregar_bicho(self, bicho):
        bicho.juego = self
        self.bichos.append(bicho)

    def clonarLaberinto(self):
        return copy.deepcopy(self.prototipo)

    def lanzarBicho(self, bicho):
        import threading
        thread = threading.Thread(target=bicho.actua)
        if bicho not in self.bicho_threads:
            self.bicho_threads[bicho] = []
        self.bicho_threads[bicho].append(thread)
        thread.start()
    
    def terminarBicho(self, bicho):
        if bicho in self.bicho_threads:
            for thread in self.bicho_threads[bicho]:
                bicho.vidas = 0

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarBicho(bicho)

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)
    

    def agregar_personaje(self, nombre):
        self.personaje = Personaje(10, 1, self, nombre)
        self.laberinto.entrar(self.personaje)

    def buscarPersonaje(self,bicho):
        if bicho.posicion == self.personaje.posicion:
            print(f"El bicho {bicho} ataca al personaje {self.personaje}")
            self.personaje.esAtacadoPor(bicho)
    


    def buscarBicho(self):
        pass



    def abrir_puertas(self):
        def abrirPuertas(obj):
            if obj.esPuerta():
                print(f"Abriendo puerta", obj)
                obj.abrir()
        self.laberinto.recorrer(abrirPuertas)

    def cerrar_puertas(self):
        def cerrarPuertas(obj):
            if obj.esPuerta():
                print(f"Cerrando puerta", obj)
                obj.cerrar()
        self.laberinto.recorrer(cerrarPuertas)


    def iniciar_juego(self):
        # Lógica para iniciar el juego
        pass

    
    
    def crearLaberinto2HabFM(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)
        habitacion1.ponerElementoEnOrientacion(puerta, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta, Sur())
        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        return laberinto
    
    def crear_laberinto_2_hab_bomba(self, creator):
        laberinto = creator.crear_laberinto()
        hab1 = creator.crear_habitacion(1)
        hab2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(hab1, hab2)

        hab1.ponerElementoEnOrientacion(puerta, Norte())
        hab2.ponerElementoEnOrientacion(puerta, Sur())

        pared1 = creator.crear_pared()
        bomba1 = creator.crear_bomba(pared1)
        hab1.ponerElementoEnOrientacion(bomba1, Este())

        pared2 = creator.crear_pared()
        bomba2 = creator.crear_bomba(pared2)
        hab2.ponerElementoEnOrientacion(bomba2, Oeste())

        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        return laberinto

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)

    def crear_laberinto_4_hab(self, creator):
        laberinto = creator.crear_laberinto()

        hab1 = creator.crear_habitacion(1)
        hab2 = creator.crear_habitacion(2)
        hab3 = creator.crear_habitacion(3)
        hab4 = creator.crear_habitacion(4)

        puerta1 = creator.crear_puerta(hab1, hab2)
        puerta2 = creator.crear_puerta(hab1, hab3)
        puerta3 = creator.crear_puerta(hab2, hab4)
        puerta4 = creator.crear_puerta(hab3, hab4)


        hab1.ponerElementoEnOrientacion(puerta1, Sur())
        hab1.ponerElementoEnOrientacion(puerta2, Este())
        hab3.ponerElementoEnOrientacion(puerta2, Oeste())
        hab3.ponerElementoEnOrientacion(puerta4, Sur())
        hab2.ponerElementoEnOrientacion(puerta1, Norte())
        hab2.ponerElementoEnOrientacion(puerta3, Este())
        hab4.ponerElementoEnOrientacion(puerta4, Norte())
        hab4.ponerElementoEnOrientacion(puerta3, Oeste())

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


        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        laberinto.agregarHabitacion(hab3)
        laberinto.agregarHabitacion(hab4)

        return laberinto
    

    def terminarJuego(self):
        self.terminarBichos()
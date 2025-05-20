from Ente.ente import Ente
from Estado.muerto import Muerto
from Modo.agresivo import Agresivo
import random
import sys
sys.setrecursionlimit(150000)

class Bicho(Ente):

    def __init__(self):
        super().__init__()
        self.modo = None
        self.numero_identificador = None


    def set_posicion(self, pos):
        self.posicion = pos
        for observador in self.obsPosition:
            observador.visualBicho(self)

    def set_vidas(self, vidas):
        self.vidas = vidas
        print("Vidas de ", str(self), ":", str(self.vidas))
        for observador in self.obsVidas:
            observador.vidasBicho(self)

    def buscarEnemigo(self):
        return self.juego.visualBicho(self)

    def actuar(self):
        while self.estaVivo():
            self.estado.actua(self)

    def obtener_orientacion_aleatoria(self):
        return self.posicion.getRandOri()
    
    def puedeActuar(self):
        self.modo.actua(self)

    def ente_muere(self):
        self.muerto()

    def muerto(self):
        self.estado = Muerto()
        self.muere()
        self.juego.muere_bicho()

    def muere(self):
        print(str(self), " ha muerto.")
        self.corazones = 0
        self.estado = Muerto()

    def cambiar(self):
        entity = self.juego.buscar_bicho(self)
        if entity is not None:
            numero_aleatorio = random.randint(1, 10)

            if numero_aleatorio > 9:
                self.modo = Agresivo()
            
                for observador in self.obsPosition:
                    observador.visualBicho(self)

    def es_bicho(self):
        return True
    
    def __str__(self):
        return "Bicho" + " id: " + str(self.numero_identificador) + " " + str(self.modo)
    
    def __repr__(self):
        return "Bicho" + str(self.modo) + str(self.numero_identificador)

    def esAtacadoPor(self, unEnte):
        self.estado.enteEsAtacadoPor(self, unEnte)
        
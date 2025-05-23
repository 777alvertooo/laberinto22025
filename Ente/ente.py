from Orientaciones.oeste import Oeste
from Orientaciones.norte import Norte
from Orientaciones.este import Este
from Orientaciones.sur import Sur
from Orientaciones.noreste import Noreste
from Orientaciones.noroeste import Noroeste
from Orientaciones.sureste import Sureste
from Orientaciones.suroeste import Suroeste
from Estado.vivo import Vivo
import sys
sys.setrecursionlimit(150000)
from abc import ABC, abstractmethod

class Ente(ABC):
    def __init__(self):
        self.vidas = 100
        self.defensa = 20
        self.poder = 10
        self.estado = Vivo()
        self.posicion = None
        self.juego = None
        self.obsPosition = []
        self.obsVidas = []

    def subscribePosicion(self, obs):
        self.obsPosition.append(obs)

    def subscribeVida(self, obs):
        self.obsVidas.append(obs)

    def setPosicion(self, pos):
        self.posicion = pos
    
    def setVidas(self, vidas):
        self.vidas = vidas
        print(str(self), "|Vidas:", str(self.vidas) + "|")

    def atacar(self):
        unEnte = self.buscarEnemigo()
        if unEnte is not None:
            unEnte.esAtacadoPor(self)
    
    def esAtacadoPor(self, unEnte):
        self.estado.enteEsAtacadoPor(self, unEnte)

    def puedeSerAtacadoPor(self, unEnte):
        print("¿Puede ser atacado?")
        self.recalcularVidas(unEnte)
        if self.verificarEstado():
            self.muere()

    def recalcularVidas(self, ente):
        if ente.esPersonaje():
            arma = ente.obtenerBatePinchos()
        else:
            arma = None

        if self.esPersonaje() and self.defensa > 0:
            defensa_efectiva = min(self.defensa, ente.poder)
            dano_recibido = ente.poder + (arma.poder if arma else 0) - defensa_efectiva
            self.defensa -= defensa_efectiva
        else:
            dano_recibido = ente.poder + (arma.poder if arma else 0)

        calc = self.corazones - dano_recibido
        if calc > self.corazones:
            self.setCorazones(self.corazones)
        else:
            self.setCorazones(calc)
        if self.corazones < 0:
            self.setCorazones(0)
    
    def verificarEstado(self):
        if self.vidas == 0:
            return True
        else:
            return False
        
    @abstractmethod
    def buscarEnemigo(self):
        pass

    def estaVivo(self):
        return self.estado.estaVivo()
    
    def irA(self, unaOr):
        unaOr.moverA(self)

    def irAlNorte(self):
        self.irA(Norte.obtenerInstancia(self))

    def irAlEste(self):
        self.irA(Este.obtenerInstancia(self))

    def irAlOeste(self):
        self.irA(Oeste.obtenerInstancia(self))

    def irAlSur(self):
        self.irA(Sur.obtenerInstancia(self))

    def irAlNoreste(self):
        self.irA(Noreste.obtenerInstancia(self))

    def irAlNoroeste(self):
        self.irA(Noroeste.obtenerInstancia(self))

    def irAlSureste(self):
        self.irA(Sureste.obtenerInstancia(self))

    def irAlSuroeste(self):
        self.irA(Suroeste.obtenerInstancia(self))

    def esPersonaje(self):
        return False
    
    def esBicho(self):
        return False
    
    @abstractmethod
    def muere(self):
        pass


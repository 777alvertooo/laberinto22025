from Forma.Hexagono import Hexagono
from LaberintoBuilder.laberinto_builder import LaberintoBuilder
from ElementoMapa.Contenedor.habitacion import Habitacion
from Orientaciones.noreste import Noreste
from Orientaciones.noroeste import Noroeste
from Orientaciones.sureste import Sureste
from Orientaciones.suroeste import Suroeste
from Orientaciones.sur import Sur
from Orientaciones.norte import Norte
from Comandos.abrir import Abrir


class LaberintoBuilderHexagono(LaberintoBuilder):

    def fabricarForma(self):
        return Hexagono()
    
    def fabricarNoreste(self):
        return Noreste.obtenerInstancia(self)
    
    def fabricarNoroeste(self):
        return Noroeste.obtenerInstancia(self)
    
    def fabricarSureste(self):
        return Sureste.obtenerInstancia(self)
    
    def fabricarSuroeste(self):
        return Suroeste.obtenerInstancia(self)
    
    def fabricarNorte(self):
        return Norte.obtenerInstancia(self)
    
    def fabricarSur(self):
        return Sur.obtenerInstancia(self)
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)

        forma = self.fabricarForma()
        forma.ref= num
        hab.form = forma

        hab.putElementOn(self.fabricarNoreste(), self.fabricarPared())
        hab.putElementOn(self.fabricarNoroeste(), self.fabricarPared())
        hab.putElementOn(self.fabricarSureste(), self.fabricarPared())
        hab.putElementOn(self.fabricarSuroeste(), self.fabricarPared())
        hab.putElementOn(self.fabricarSur(), self.fabricarPared())
        hab.putElementOn(self.fabricarNorte(), self.fabricarPared())

        hab.addOr(self.fabricarNoreste())
        hab.addOr(self.fabricarNoroeste())
        hab.addOr(self.fabricarSureste())
        hab.addOr(self.fabricarSuroeste())
        hab.addOr(self.fabricarSur())
        hab.addOr(self.fabricarNorte())

        self.laberinto.agregarHabitacion(hab)

        return hab
    
    def fabricarBaulEn(self, obj, num):
        baul = self.fabricarBaul(num)

        p1 = self.fabricarPuerta()
        cmd = Abrir()
        cmd.receiver = p1
        p1.addCommand(cmd)

        p1.lado1 = baul
        p1.lado2 = obj

        baul.form = self.fabricarForma()
        baul.addOr(self.fabricarNorte())
        baul.addOr(self.fabricarSureste())
        baul.addOr(self.fabricarSuroeste())
        baul.addOr(self.fabricarSur())
        baul.addOr(self.fabricarNoroeste())
        baul.addOr(self.fabricarNoroeste())

        baul.putElementOn(self.fabricarSur(), self.fabricarPared())
        baul.putElementOn(self.fabricarSureste(), self.fabricarPared())
        baul.putElementOn(self.fabricarSuroeste(), self.fabricarPared())
        baul.putElementOn(self.fabricarNorte(), p1)
        baul.putElementOn(self.fabricarNoroeste(), self.fabricarPared())
        baul.putElementOn(self.fabricarNoreste(), self.fabricarPared())

        obj.addChild(baul)

        return baul
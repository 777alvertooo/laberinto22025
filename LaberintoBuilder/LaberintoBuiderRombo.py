from Forma.rombo import Rombo
from LaberintoBuilder.laberinto_builder import LaberintoBuilder
from ElementoMapa.Contenedor.habitacion import Habitacion
from Orientaciones.noreste import Noreste
from Orientaciones.noroeste import Noroeste
from Orientaciones.sureste import Sureste
from Orientaciones.suroeste import Suroeste
from Comandos.abrir import Abrir


class LaberintoBuilderRombo(LaberintoBuilder):

    def fabricarForma(self):
        return Rombo()
    
    def fabricarNoreste(self):
        return Noreste.obtenerInstancia(self)
    
    def fabricarNoroeste(self):
        return Noroeste.obtenerInstancia(self)
    
    def fabricarSureste(self):
        return Sureste.obtenerInstancia(self)
    
    def fabricarSuroeste(self):
        return Suroeste.obtenerInstancia(self)
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)

        forma = self.fabricarForma()
        forma.ref= num
        hab.form = forma

        hab.putElementOn(self.fabricarNoreste(), self.fabricarPared())
        hab.putElementOn(self.fabricarNoroeste(), self.fabricarPared())
        hab.putElementOn(self.fabricarSureste(), self.fabricarPared())
        hab.putElementOn(self.fabricarSuroeste(), self.fabricarPared())

        hab.addOr(self.fabricarNoreste())
        hab.addOr(self.fabricarNoroeste())
        hab.addOr(self.fabricarSureste())
        hab.addOr(self.fabricarSuroeste())

        self.laberinto.agregarHabitacion(hab)

        return hab
    
    def fabricarArmarioEn(self, padre, num):
        armario = self.fabricarArmario(num)
        
        p1= self.fabricarPuerta()
        cmd = Abrir()
        cmd.receiver=p1

        p1.addCommand(cmd)


        p1.lado1=self
        p1.lado2=padre

        armario.form= self.fabricarForma()
        p1.lado1= armario
        p1.lado2 = padre

        armario.addOr(self.fabricarNoreste())
        armario.addOr(self.fabricarNoroeste())
        armario.addOr(self.fabricarSureste())
        armario.addOr(self.fabricarSuroeste())

        armario.putElementOn(self.fabricarNoreste(),self.fabricarPared())
        armario.putElementOn(self.fabricarNoroeste(),self.fabricarPared())
        armario.putElementOn(self.fabricarSureste(),self.fabricarPared())
        armario.putElementOn(self.fabricarSuroeste(),p1)

        padre.addChild(armario)
        return armario
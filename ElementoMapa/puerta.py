from ElementoMapa.elemento_mapa import ElementoMapa
from Estado.EstadoPuerta.estado_puerta import Cerrada

class Puerta(ElementoMapa):
    def __init__(self):
        self.lado1 = None
        self.lado2 = None
        self.visitada = False
        self.estadoPuerta = Cerrada()

    def entrar(self,ente):
        if self.estaAbierta():
            if ente.posicion == self.lado1:
                self.lado2.entrar(ente)
            else:
                self.lado1.entrar(ente)
        else:
            print(str(ente)," se chocó con una puerta.")

    def puedeEntrar(self, alguien):
        print("Entrando en una puerta")
        if alguien.posicion == self.lado1:
            self.lado2.entrar(alguien)
        else:
            self.lado1.entrar(alguien)

    def abrir(self):
        print("Abriendo puerta")
        self.estadoPuerta.abrir(self)

    def cerrar(self):
        print("Cerrando puerta")
        self.estadoPuerta.cerrar(self)

    def esPuerta(self):
        return True
    
    def aceptar(self,visitor):
        print("Visitando una puerta")
        visitor.visitarPuerta(self)

    def calcularPosicionDesdeEn(self,forma, punto):
        print("punto: ", punto.x, punto.y)
        if self.visitada:
            return
        self.visitada = True
        if self.lado1.num == forma.num:
            self.lado2.forma.punto=punto
            self.lado2.calcularPosicion()
        else:
            self.lado1.forma.punto=punto
            self.lado1.calcularPosicion()
    
    def __str__(self):
        return "Soy una puerta"
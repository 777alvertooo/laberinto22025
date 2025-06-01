class ElementoMapa:

    def __init__(self):
        self.comandos = []

    def entrar(self):
        pass

    def entrar(self, alguien):
        pass

    def esArmario(self):
        pass

    def esBomba(self):
        pass

    def esFuego(self):
        pass

    def esHabitacion(self):
        pass

    def esLaberinto(self):
        pass

    def esPared(self):
        pass

    def esPuerta(self):
        pass

    def recorrer(self, unBloque):
        unBloque(self)

    def __str__(self):
        return "ElementoMapa"
    
    def aceptar(self, unVisitor):
        pass

    def agregarComando(self, unComando):
        self.comandos.append(unComando)

    def calcularPosicionDesdeEn(self, unaForma, unPunto):
        pass
    
    def eliminarComando(self, unComando):
        try:
            self.comandos.remove(unComando)
        except ValueError:
            print("No existe ese comando")

    def obtenerComandos(self):
        return self.comandos
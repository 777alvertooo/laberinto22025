from ElementoMapa.pared import Pared
from Comandos.apagar import Apagar

class ParedFuego(Pared):
    def __init__(self):
        super().__init__()
        self.commands.append(Apagar(self))

    def obtenerComandos(self, ente):
        return self.commands

    def aceptar(self, visitor):
        visitor.visitar(self)

    def __str__(self):
        return "Pared de Fuego"
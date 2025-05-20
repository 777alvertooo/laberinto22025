
from ElementoMapa.Contenedor.contenedor import Contenedor

class Armario(Contenedor):
    def __init__(self, ref):
        super().__init__(ref)
        self.observaciones = []

    def esArmario(self):
        return True

    def __str__(self):
        return "Armario " + str(self.ref)
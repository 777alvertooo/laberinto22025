from ElementoMapa.Contenedor.contenedor import Contenedor

class Baul(Contenedor):
    def __init__(self, ref):
        super().__init__(ref)
        self.observaciones = []

    def esBaul(self):
        return True

    def __str__(self):
        return "Baul " + str(self.ref)
from .Orientacion import Orientacion

class Sureste(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, unContenedor):
        unContenedor.sureste = elemento

    def recorrer(self, func, unContenedor):
        if unContenedor.sureste is not None:
            func(unContenedor.sureste)

    def __str__(self):
        return "Sureste"

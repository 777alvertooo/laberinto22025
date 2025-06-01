
from .Orientacion import Orientacion

class Suroeste(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, unContenedor):
        unContenedor.suroeste = elemento

    def recorrer(self, func, unContenedor):
        if unContenedor.suroeste is not None:
            func(unContenedor.suroeste)

    def __str__(self):
        return "Suroeste"

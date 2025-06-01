
from .Orientacion import Orientacion

class Oeste(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, unContenedor):
        unContenedor.oeste = elemento

    def recorrer(self, func, unContenedor):
        if unContenedor.oeste is not None:
            func(unContenedor.oeste)

    def __str__(self):
        return "Oeste"


from .Orientacion import Orientacion

class Norte(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, unContenedor):
        unContenedor.norte = elemento

    def recorrer(self, func, unContenedor):
        if unContenedor.norte is not None:
            func(unContenedor.norte)

    def __str__(self):
        return "Norte"

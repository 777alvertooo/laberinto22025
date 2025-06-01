
from .Orientacion import Orientacion

class Sur(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, unContenedor):
        unContenedor.sur = elemento

    def recorrer(self, func, unContenedor):
        if unContenedor.sur is not None:
            func(unContenedor.sur)

    def __str__(self):
        return "Sur"

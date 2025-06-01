from .Orientacion import Orientacion

class Noroeste(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, unContenedor):
        unContenedor.noroeste = elemento

    def recorrer(self, func, unContenedor):
        if unContenedor.noroeste is not None:
            func(unContenedor.noroeste)

    def __str__(self):
        return "Noroeste"

from .Orientacion import Orientacion

class Noreste(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, unContenedor):
        unContenedor.noreste = elemento

    def recorrer(self, func, unContenedor):
        if unContenedor.noreste is not None:
            func(unContenedor.noreste)

    def __str__(self):
        return "Noreste"
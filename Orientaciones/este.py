from .Orientacion import Orientacion

class Este(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, unContenedor):
        unContenedor.este = elemento

    def recorrer(self, func, unContenedor):
        if unContenedor.este is not None:
            func(unContenedor.este)

    def __str__(self):
        return "Este"
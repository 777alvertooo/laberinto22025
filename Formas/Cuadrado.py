from Formas.Forma import Forma

class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.orientaciones = []

    def __str__(self):
        return f"Cuadrado"

    
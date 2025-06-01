from Formas.Forma import Forma

class Hexagono(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None
        self.orientaciones = []

    def __str__(self):
        return f"Hexagono"
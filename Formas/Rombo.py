
from Formas.Forma import Forma

class Rombo(Forma):
    def __init__(self):
        super().__init__()
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None
        self.orientaciones = []

    def __str__(self):
        return f"Rombo"

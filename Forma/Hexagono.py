from Forma.forma import Forma

class Hexagono(Forma):
    def __init__(self):
        super().__init__()

        self.norte = None
        self.sur = None
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None

    def esHexagono(self):
        return True

    

    def __str__(self):
        return (
            "\n   -Norte: " + str(self.norte) +
            "\n   -Sur: " + str(self.sur) +
            "\n   -Noreste: " + str(self.noreste) +
            "\n   -Noroeste: " + str(self.noroeste) +
            "\n   -Sureste: " + str(self.sureste) +
            "\n   -Suroeste: " + str(self.suroeste))

from FM.Creator import Creator
from ElementoMapa.ParedBomba import ParedBomba
from ElementoMapa.ParedFuego import ParedFuego

class CreatorB(Creator):

    def fabricarParedBomba(self):
        return ParedBomba()
    
    def fabricarParedFuego(self):
        return ParedFuego()
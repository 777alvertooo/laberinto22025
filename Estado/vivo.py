from Estado.estado import Estado
import sys
sys.setrecursionlimit(150000)
class Vivo(Estado):
    
    def actua(self,unBicho):
        unBicho.puedeActuar()

    def enteEsAtacadoPor(self,victima,agresor):
        victima.puedeSerAtacadoPor(agresor)

    def estaVivo(self):
        return True
    
    def esVivo(self):
        return True
    
    def __str__(self):
        return "Vivo"
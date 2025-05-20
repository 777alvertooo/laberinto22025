import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ElementoMapa')))

from ElementoMapa.Contenedor.contenedor import Contenedor

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()        

    def entrar(self, ente):
        h = self.getHab(1)
        h.entrar(ente)

    def __str__(self):
        return "Soy un laberinto"

    def agregarHabitacion(self, hab):
        self.objChildren.append(hab)

    def getHab(self, index):
        return self.objChildren[index - 1]
    
    def recorrer(self, order):
        for ch in self.objChildren:
            ch.recorrer(order)
    
    def aceptar(self, visitor):
        print("Recorrer laberinto.")
        for ch in self.objChildren:
            ch.aceptar(visitor)
    
    def visitarContenedor(self, unVisitor):
        unVisitor.visitarLaberinto(self)

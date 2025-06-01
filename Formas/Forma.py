import random


class Forma:

    def __init__(self):
        self.orientaciones = []

    def ponerElementoEnOrientacion(self, elemento, unaOr):
        unaOr.poner(elemento, self)

    def eliminarOrientacion(self, unaOr):
        self.unaOr.remove(unaOr)

    def agregarOrientacion(self, unaOr):
        self.orientaciones.append(unaOr)

    def obtenerElementoEnOrientacion(self, unaOr):
        return unaOr.obtenerElemento(self)

    def recorrer(self, func):
        for unaOr in self.orientaciones:
            unaOr.recorrer(func, self)
    
    def caminarAleatorio(self, bicho):
        unaOr=self.obtenerOrientacionAleatoria()
        print(f"Orientacion aleatoria: {unaOr}")
        unaOr.caminarAleatorio(bicho, self)

    def obtenerOrientacionAleatoria(self):
        return random.choice(self.orientaciones)
    
    def __str__(self):
        return "Forma"
    
    

    
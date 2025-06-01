
from ElementoMapa.Hoja.Hoja import Hoja

class Tunel(Hoja):

    def __init__(self, laberinto):
        super().__init__()
        self.laberinto = None

    def esTunel(self):
        return True
    
    def entrar(self, alguien):
        if self.laberinto is None:
            alguien.clonarLaberinto(self)            
        else:
            self.laberinto.entrar(alguien)

    def crearNuevoLaberinto(self, alguien):
        self.laberinto = alguien.juegoClonaLaberinto()
        print(f"{alguien} crea un nuevo laberinto")

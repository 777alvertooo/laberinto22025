from ElementoMapa.Hoja.Decorator.Decorator import Decorator

class Fuego(Decorator):
    def __init__(self):
        super().__init__()

    def entrar(self, alguien):
        print(f"{alguien} entra en fuego y se quema")
        alguien.vidas -= 2
        self.em.entrar(alguien)
    
    
    def __str__(self):
        return "Fuego"

    def esFuego(self):
        return True

    

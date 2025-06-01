from ElementoMapa.Hoja.Decorator.Decorator import Decorator

class Bomba(Decorator):
    
    def __init__(self, em, daño: int = 10):
        super().__init__(em)
        self.daño = daño
        self.activa = False


    def esBomba(self):
        return True


    def __str__(self):
        return f"Bomba {self.activa}"
    

    def activar(self):
        self.activa = True
        print("Bomba activada")

    def esBombaNuclear(self):
        return False
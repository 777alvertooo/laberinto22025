from ElementoMapa.pared import Pared

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self,ente):
        if self.activa:
            print("¡BOOOOOOM! La bomba te ha explotado...")
            self.activa = False
        else:
            print("Te has chocado")

    def __str__(self):
        return "Soy una pared bomba"
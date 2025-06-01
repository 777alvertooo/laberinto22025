
from .Pared import Pared

class ParedFuego(Pared):

    def __init__(self):
        super().__init__()
        self.activa = True  # Puedes apagarla si lo deseas más adelante

    def entrar(self, alguien):
        if self.activa:
            print(f"{alguien} se quema al tocar la ParedFuego")
            alguien.vidas -= 2
            if alguien.vidas <= 0:
                alguien.heMuerto()
        else:
            print(f"{alguien} toca una ParedFuego desactivada")

    def activar(self):
        self.activa = True
        print("ParedFuego activada")

    def desactivar(self):
        self.activa = False
        print("ParedFuego desactivada")

    def esFuego(self):
        return True

    def __str__(self):
        return "ParedFuego"

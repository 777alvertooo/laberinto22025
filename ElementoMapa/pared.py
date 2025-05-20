from ElementoMapa.elemento_mapa import ElementoMapa

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self,alguien):
        print("chocando en una pared")

    def aceptar(self,visitor):
        print("Has visitado una pared.")
        visitor.visitaPared(self)

    def esPared(self):
        return True

    def __str__(self):
        return "Soy una pared"
    
    def __repr__(self):
        return "Pared"
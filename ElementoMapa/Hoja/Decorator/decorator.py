from ElementoMapa.Hoja.hoja import Hoja

class Decorator(Hoja):
    def __init__(self):
        super().__init__()
        self.em = None

    def recorrer(self, o):
            o(self)
            if self.componente is not None:
                self.componente.recorrer(o)

    def __str__(self):
        return "Soy un decorator"
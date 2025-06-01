from ElementoMapa.Hoja.Hoja import Hoja

class Decorator(Hoja):
        
        def __init__(self):
            super().__init__()
            self.em = None

        def __str__(self):
            return f"Decorator"
        
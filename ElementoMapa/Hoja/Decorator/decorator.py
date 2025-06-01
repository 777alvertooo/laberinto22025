from ElementoMapa.Hoja.Hoja import Hoja

class Decorator(Hoja):
        
        def __init__(self, em):
            super().__init__(getattr(em, 'nombre', str(em)))
            self.em = em

        def __str__(self):
            return f"Decorator"
        
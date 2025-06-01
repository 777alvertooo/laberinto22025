from ElementoMapa.Hoja.Decorator.Decorator import Decorator

class Fuego(Decorator):
    def __init__(self, em, daño: int = 5):
        # Llamamos a Decorator.__init__(em), que a su vez llama a Hoja.__init__(em.nombre)
        super().__init__(em)
        self.daño = daño

    def esFuego(self):
        return True

    def __str__(self):
        nombre_base = getattr(self.em, 'nombre', str(self.em))
        return f"Fuego '{nombre_base}' (Daño: {self.daño})"

    

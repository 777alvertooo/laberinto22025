from ElementoMapa.ElementoMapa import ElementoMapa

class Hoja(ElementoMapa):
    def __init__(self, nombre: str):
        super().__init__()
        self.nombre: str = nombre

    def __str__(self):
        return self.nombre

    def usar(self, personaje, **kwargs) -> bool:
        print(f"No se puede usar '{self.nombre}' de esta manera directamente.")
        return False
from ElementoMapa.elemento_mapa import ElementoMapa

class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Hoja"
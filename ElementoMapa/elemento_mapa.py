class ElementoMapa:
    def __init__(self):
        self.padre = None
        self.commands = []
    
    def recorrer(self, func):
        func(self)

    def entrar(self, alguien):
        pass

    def aceptar(self, unVisitor):
        pass

    def esPuerta(self):
        return False

    def esHabitacion(self):
        return False
    
    def esBomba(self):
        return False
    
    def esPared(self):
        return False
    
    def esArmario(self):
        return False
    
    def esTunel(self):
        return False

    def calcularPosicionDesde(self,forma):
        pass
    def calcularPosicion(self):
        pass
    def calcularPosicionDesdeEn(self,forma, punto):
        pass
    def __str__(self):
        return "Soy un ElementoMapa"
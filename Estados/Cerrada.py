from Estados.EstadoPuerta import EstadoPuerta


class Cerrada(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def cerrar(self, unaPuerta):
        print("Puerta ya cerrada")

    def abrir(self, unaPuerta):
        from Estados.Abierta import Abierta
        print("Abriendo puerta")
        unaPuerta.estadoPuerta = Abierta()

    def entrar(self, unaPuerta, alguien):
        pass

    def __str__(self):
        return "Cerrada"
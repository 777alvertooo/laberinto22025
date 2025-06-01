from Estados.EstadoPuerta import EstadoPuerta


class Abierta(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def cerrar(self, unaPuerta):
        from Estados.Cerrada import Cerrada
        print("Cerrando puerta")
        unaPuerta.estadoPuerta = Cerrada()

    def abrir(self, unaPuerta):
        print("Puerta ya abierta")

    def entrar(self, unaPuerta, alguien):
        unaPuerta.puedeEntrar(alguien)
    
    def __str__(self):
        return "Abierta"
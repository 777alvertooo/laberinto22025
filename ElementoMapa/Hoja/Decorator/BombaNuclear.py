from ElementoMapa.Hoja.Decorator.Bomba import Bomba

class BombaNuclear(Bomba):
    def __init__(self):
        super().__init__()

    def entrar(self, alguien):
        if self.activa:
            print(f"{alguien} ha activado la BOMBA NUCLEAR")
            self.explotar(alguien.posicion)
        else:
            print(f"{alguien} pisa la bomba nuclear inactiva")
            self.em.entrar(alguien)

    def activar(self):
        self.activa = True
        print("Bomba Nuclear ARMADA")

    def explotar(self, contenedor):
        print("¡BOOM! Todos los entes en la zona son eliminados")

        for hijo in contenedor.hijos:
            if hasattr(hijo, "vidas") and hijo.estaVivo():
                hijo.vidas = 0
                hijo.heMuerto()

        # Propagación opcional
        for or_ in contenedor.obtenerOrientaciones():
            vecino = contenedor.obtenerElementoOr(or_)
            if vecino and hasattr(vecino, "hijos"):
                print(f"La explosión alcanza {vecino}")
                self.explotar(vecino)

    def esBombaNuclear(self):
        return True

    def aceptar(self, unVisitor):
        if hasattr(unVisitor, "visitarBombaNuclear"):
            unVisitor.visitarBombaNuclear(self)

    def __str__(self):
        return "BombaNuclear"

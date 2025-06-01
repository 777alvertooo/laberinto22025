
from ElementoMapa.Contenedor.Contenedor import Contenedor

class Habitacion(Contenedor):

    def __init__(self, num, nombre="", descripcion=""):
        super().__init__()
        self.num = num
        self.nombre = nombre
        self.descripcion = descripcion
        # Hacemos que items_en_habitacion sea un alias de self.hijos:
        self.items_en_habitacion = self.hijos

    def entrar(self, alguien):
        print(f"Entrando en la habitación {self.num}")
        alguien.posicion = self

    def __str__(self):
        return f"Habitación {self.num} ({getattr(self, 'nombre', 'Sin Nombre')})"
    

    def mostrarObjetos(self):
        """
        Lista TODO lo que hay en self.hijos. El juego debe llamar a este método
        cuando quiera imprimir “Ves aquí: …”
        """
        if not self.hijos:
            print("No ves ningún objeto de interés inmediato.")
            return

        print("Ves aquí:")
        for obj in self.hijos:
            print(f"  - {getattr(obj, 'nombre', str(obj))}")

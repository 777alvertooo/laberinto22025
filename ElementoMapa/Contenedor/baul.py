from ElementoMapa.Contenedor.Contenedor import Contenedor


class Baul(Contenedor):
    def __init__(self, nombre: str):
        super().__init__()
        self.nombre = nombre       # ahora lo recibimos dinámicamente
        self.abierto = False

    def abrir(self, personaje):
        if self.abierto:
            print(f"El baul '{self.nombre}' ya está abierto.")
            return
        self.abierto = True
        print(f"Has abierto el baul '{self.nombre}'.")
        self.verificar_daño(personaje)

        # Mover todos los hijos a la habitación padre
        padre = getattr(self, 'padre', None)
        if padre:
            for item in list(self.hijos):
                self.hijos.remove(item)
                padre.agregar_hijo(item)
                print(f"  - Del interior del baul aparece: '{item.nombre}'")

    def verificar_daño(self, personaje):
        for item in self.hijos:
            clase = type(item).__name__
            if clase in ['Bomba', 'Fuego', 'BombaNuclear']:
                daño = getattr(item, 'daño', 10)
                print(f"¡Al abrir el baul '{self.nombre}', '{getattr(item, 'nombre', str(item))}' te hace daño!")
                personaje.recibir_daño(daño)

    def esBaul(self):
        return True

    def __str__(self):
        return f"Armario '{self.nombre}'"

from ElementoMapa.ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):

    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones = []

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminar_hijo(self, hijo):
        self.hijos.remove(hijo)

    def agregar_orientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def eliminar_orientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.poner(elemento, self)

    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)
        for orientacion in self.orientaciones:
            orientacion.recorrer(func, self)
    
    def listar_contenido(self):
        if not self.hijos:
            return f"El {self.__str__()} está vacío."
        return f"{self.__str__()} contiene:\n" + "\n".join(f"  - {h.nombre}" for h in self.hijos)

    def coger_todo(self):
        contenido = self.hijos[:]
        self.hijos.clear()
        return contenido

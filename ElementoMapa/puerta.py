
from Estados.Cerrada import Cerrada
from ElementoMapa.ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2): 
        super().__init__() 
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def entrar(self, alguien): 
        # print(f"Puerta.entrar: {alguien.nombre} intenta entrar. Puerta abierta: {self.abierta}")
        if self.abierta:
            if alguien.posicion == self.lado1:
                print(f"Puerta '{getattr(self, 'nombre', 'Puerta')}' abierta, {alguien.nombre} va de {self.lado1} a {self.lado2}")
                self.lado2.entrar(alguien) 
                return True 
            elif alguien.posicion == self.lado2:
                print(f"Puerta '{getattr(self, 'nombre', 'Puerta')}' abierta, {alguien.nombre} va de {self.lado2} a {self.lado1}")
                self.lado1.entrar(alguien) 
                return True 
            else:
                print(f"Error: {alguien.nombre} no está en un lado válido ({self.lado1} o {self.lado2}) de la puerta '{getattr(self, 'nombre', 'Puerta')}'. Posición actual: {alguien.posicion}")
                return False
        else:
            print(f"La puerta '{getattr(self, 'nombre', 'Puerta')}' está cerrada.")
            return False 

    def abrir(self):
        if not self.abierta:
            print(f"Abriendo puerta '{getattr(self, 'nombre', 'Puerta')}'")
            self.abierta = True
        else:
            print(f"La puerta '{getattr(self, 'nombre', 'Puerta')}' ya estaba abierta.")
        return self.abierta


    def cerrar(self):
        if self.abierta:
            print(f"Cerrando puerta '{getattr(self, 'nombre', 'Puerta')}'")
            self.abierta = False
        else:
            print(f"La puerta '{getattr(self, 'nombre', 'Puerta')}' ya estaba cerrada.")
        return not self.abierta


    def esPuerta(self): 
        return True

    def __str__(self): 
        estado = "Abierta" if self.abierta else "Cerrada"
        return f"{getattr(self, 'nombre', 'puerta')} ({estado})"



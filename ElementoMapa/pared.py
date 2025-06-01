from ElementoMapa.ElementoMapa import ElementoMapa
class Pared(ElementoMapa):
    
    def entrar(self,alguien):
         print(f"{alguien} se ha chocado con una pared")

    def esPared(self):
        return True

    def __str__(self):
        return "Pared"
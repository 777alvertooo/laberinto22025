from Comandos.Comandos import Comandos


class Usar(Comandos):
    
    def ejecutar(self, obj):
        self.receiver.usar(obj)
    
    def esUsar(self):
        return True
    
    def __str__(self):
        return "Usar"
    def equals(self,comando):
        if comando.esUsar():
            return True
        return False
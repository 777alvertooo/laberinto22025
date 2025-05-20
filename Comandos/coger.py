from Comandos.Comandos import Comandos

class Coger(Comandos):
    
    def ejecutar(self, obj):
        self.receiver.entrar(obj)

    def esCoger(self):
        return True
    
    def __str__(self):
        return "Coger"
    def equals(self,comando):
        if comando.esCoger():
            return True
        return False
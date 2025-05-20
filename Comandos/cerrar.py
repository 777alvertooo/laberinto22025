from Comandos.Comandos import Comandos


class Cerrar(Comandos):

    def ejecutar(self, obj):
        self.receiver.close(obj)
    
    def esCerrar(self): 
        return True
    
    def __str__(self):
        return "Puerta cerrada"
    
    
    def equals(self,comando):
        if comando.esCerrar():
            return True
        return False
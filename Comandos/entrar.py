from Comandos.Comandos import Comandos


class Entrar(Comandos):
    def ejecutar(self, obj):
        self.receiver.entrar(obj)
    
    def esEntrar(self):
        return True
    
    def __str__(self):
        return "¡Entrando!"
    
    
    def equals(self,comando):
        if comando.esEntrar():
            return True
        return False
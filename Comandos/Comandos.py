from abc import ABC, abstractmethod
class Comandos(ABC):
    
    def __init__(self):
        self.receiver = None
        
    @abstractmethod
    def ejecutar(self, ente):
        pass

    def esAbrir(self):
        return False
    
    def esCerrar(self):
        return False
    
    def esEntrar(self):
        return False
    
    
    
    @abstractmethod
    def equals(self,command):
        pass
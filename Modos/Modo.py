
class Modo:

    def __init__(self):
        pass

    def actuar(self, bicho):
        self.dormir(bicho)
        self.caminar(bicho)
        self.atacar(bicho)


    def dormir(self, unBicho):
        pass

    def caminar(self, unBicho):
        pass

    def atacar(self, unBicho):
        pass

    def buscarTunelBicho(self, unBicho):
        pass

    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False
    
    def __str__(self):
        return "Modo"

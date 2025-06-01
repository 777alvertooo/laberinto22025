from Estados.EstadoEnte import EstadoEnte

class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()
        
    def morir(self, unEnte): 
        from Estados.Muerto import Muerto  
        nombre_ente = getattr(unEnte, 'nombre', 'El ente') 
        print(f"{nombre_ente} muere.")
        unEnte.estadoEnte = Muerto() 

    def vivir(self, unEnte):
        nombre_ente = getattr(unEnte, 'nombre', 'El ente')
        print(f"{nombre_ente} está vivo.")

    def __str__(self):
        return "Vivo"

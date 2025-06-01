
import time
from Modos.Modo import Modo
from Estados.Vivo import Vivo

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def buscarTunelBicho(self, unBicho):
        pos = unBicho.posicion
        tunel = next((each for each in pos.hijos if each.esTunel()), None)
        if tunel is not None:
            tunel.entrar(unBicho)

    def dormir(self, unBicho):
        nombre_bicho = getattr(unBicho, 'nombre', 'Perezoso')
        print(f"{nombre_bicho}: Durmiendo profundamente...")
        time.sleep(1) 

    def caminar(self, unBicho):
        nombre_bicho = getattr(unBicho, 'nombre', 'Perezoso')
        # print(f"{nombre_bicho}: Deambulando sin prisa...")
        pass 
    

    
    def atacar(self, unBicho, unPersonajeObj):

        nombre_bicho = getattr(unBicho, 'nombre', 'Perezoso')
        nombre_personaje = getattr(unPersonajeObj, 'nombre', 'el objetivo')

        if getattr(unBicho, 'invisible', False):
            print(f"{nombre_bicho} es invisible y no puede atacar todavía.")
            return

        if unPersonajeObj and hasattr(unPersonajeObj, 'recibir_daño') and \
           hasattr(unPersonajeObj, 'estadoEnte') and isinstance(unPersonajeObj.estadoEnte, Vivo):
            print(f"El {nombre_bicho} ataca a {nombre_personaje} con desgana.")
            if hasattr(unBicho, 'poder'):
                unPersonajeObj.recibir_daño(unBicho.poder)
            else:
                print(f"WARN: {nombre_bicho} no tiene atributo 'poder'.")
        else:
            print(f"El {nombre_bicho} ni se molesta en atacar (objetivo no válido o no vivo).")


    def esPerezoso(self):
        return True
    
    def __str__(self):
        return "Perezoso"

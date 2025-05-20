from Fase.fase import Fase

class Final(Fase):
    
    def addCharacter(self, ch, game):
        print("[¡!] El juego ya ha terminado. No puedes introducir más personajes [¡!]")

    def lanzarBichos(self,juego):
        print("[¡!] El juego ya ha terminado. No puedes introducir más bichos [¡!]")
        
    def esFinal(self):
        return True
    
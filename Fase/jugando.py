from Fase.fase import Fase

class Jugando(Fase):

    def addCharacter(self, ch, game):
        print("[¡!] El juego está en curso, no puedes meter más personajes [¡!]")

    def lanzarBichos(self, ch, game):
        print("[¡!] El juego está en curso, no puedes meter más bichos [¡!]")
    
    def esJugando(self):
        return True
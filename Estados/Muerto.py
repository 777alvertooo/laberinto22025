from Estados.EstadoEnte import EstadoEnte


class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()

    def morir(self,unEnte): 
        nombre_ente = getattr(unEnte, 'nombre', 'El ente')
        
        if hasattr(unEnte, 'juego') and unEnte.juego:
            from Ente.Personaje import Personaje
            if isinstance(unEnte, Personaje): 
                print(f"{nombre_ente} (el personaje principal) está completamente derrotado.")
                unEnte.juego.perder_juego() 
            else: 
                print(f"{nombre_ente} ya estaba/ha sido derrotado (no es el jugador).")
        else:
            print(f"{nombre_ente} está muerto, pero no se pudo finalizar el juego (sin referencia a 'juego').")

    def vivir(self, unEnte):
        from Estados.Vivo import Vivo  # 🔁 Importación local aquí
        nombre_ente = getattr(unEnte, 'nombre', 'El ente')
        print(f"{nombre_ente} revive milagrosamente.") 
        unEnte.estadoEnte = Vivo()

    def __str__(self):
        return "Muerto"

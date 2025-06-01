from Comandos.Comando import Comando
from typing import  Optional, List
from ElementoMapa.Puerta import Puerta

class Cerrar(Comando):
    
    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje or not juego.personaje.posicion:
            return "Error: Personaje no inicializado o sin posición."
        
        if not args:
            return "Debes especificar qué puerta quieres abrir (ej: 'abrir norte')."
            
        direccion = args[0].lower()
        habitacion_actual = juego.personaje.posicion


        if hasattr(habitacion_actual, direccion):
            elemento = getattr(habitacion_actual, direccion)
            if isinstance(elemento, Puerta):
                if elemento.abierta:
                    elemento.cerrar()
                    return f"Has cerrado la '{getattr(elemento, 'nombre', 'puerta')}' en dirección {direccion}."
                else:
                    return f"La puerta ya está cerrada."
            else:
                return f"No hay una puerta en la dirección '{direccion}'."
        else:
            return f"La dirección '{direccion}' no es válida desde aquí."
        

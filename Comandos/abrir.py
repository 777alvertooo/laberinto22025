from Comandos.Comando import Comando
from typing import  Optional, List
from ElementoMapa.Puerta import Puerta

class Abrir(Comando):
    
    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje or not juego.personaje.posicion:
            return "Error: Personaje no inicializado o sin posición."
        
        if not args:
            return "Debes especificar qué puerta quieres abrir (ej: 'abrir norte')."
            
        direccion = " ".join(args).lower()
        habitacion_actual = juego.personaje.posicion
        # Primero intentamos abrir una puerta en esa dirección
        if hasattr(habitacion_actual, direccion):
            elemento_en_direccion = getattr(habitacion_actual, direccion)
            if isinstance(elemento_en_direccion, Puerta):
                puerta_a_abrir = elemento_en_direccion
                if puerta_a_abrir.abrir():
                    return f"Has abierto la '{getattr(puerta_a_abrir, 'nombre', 'puerta')}' en dirección {direccion}."
                else:
                    return None
            else:
                return f"No hay una puerta en la dirección '{direccion}' para abrir."
        
        # Buscar en hijos un contenedor (armario o baul) con nombre EXACTO igual a entrada
        for hijo in getattr(habitacion_actual, 'hijos', []):
            nombre_hijo = getattr(hijo, 'nombre', '').lower()
            if (hasattr(hijo, 'esArmario') and hijo.esArmario() or
                hasattr(hijo, 'esBaul') and hijo.esBaul()) and nombre_hijo == direccion:
                hijo.abrir(juego.personaje)
                return f"Has abierto el {nombre_hijo}."

        return f"No hay nada que puedas abrir llamado '{direccion}'."
        

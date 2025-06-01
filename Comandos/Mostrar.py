from Comandos.Comando import Comando
from typing import  Optional, List

class Mostrar(Comando):
    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje:
            return "Error: No hay un personaje en el juego."

        salud_str = f"Salud de {juego.personaje.nombre}: {juego.personaje.vidas}"
        if hasattr(juego.personaje, 'vidas_maximas') and juego.personaje.vidas_maximas is not None:
            salud_str += f" / {juego.personaje.vidas_maximas}"
        print(salud_str)

        # Mostrar inventario
        print("--- Inventario ---")
        inventario = getattr(juego.personaje, 'inventario', None)
        if inventario and hasattr(inventario, 'listar_items'):
            print(inventario.listar_items())
        else:
            print("  (Inventario no disponible)")

        print("--- Ubicación Actual ---")
        juego.mostrar_descripcion_habitacion_actual() 
        
        return None
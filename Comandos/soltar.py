from Comandos.Comando import Comando
from typing import  Optional, List

class Soltar(Comando):
    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje or not juego.personaje.posicion:
            return "Error: Personaje no inicializado o sin posición."
        if not hasattr(juego.personaje, 'inventario'):
            return "Error: El personaje no tiene inventario."

        if not args:
            return "Debes especificar qué objeto quieres soltar (ej: 'soltar palo de madera')."
        
        nombre_item_a_soltar = " ".join(args).lower()
        
        item_soltado = juego.personaje.inventario.quitar_item_por_nombre(nombre_item_a_soltar)
        
        if item_soltado:
            habitacion_actual = juego.personaje.posicion
            if hasattr(habitacion_actual, 'agregar_hijo'):
                habitacion_actual.agregar_hijo(item_soltado)
                if hasattr(item_soltado, 'equipada') and item_soltado.equipada:
                    if hasattr(item_soltado, 'usar'):
                         item_soltado.usar(juego.personaje) 
                return f"Has soltado: {item_soltado.nombre}."
            else:
                juego.personaje.inventario.agregar_item(item_soltado) 
                return f"Error: No puedes dejar objetos en este lugar."
        else:
            return f"No tienes un objeto llamado '{nombre_item_a_soltar}' en tu inventario."

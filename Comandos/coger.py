from Comandos.Comando import Comando
from ElementoMapa.Hoja.Hoja import Hoja
from typing import  Optional, List


class Coger(Comando):
    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje or not juego.personaje.posicion:
            return "Error: Personaje no inicializado o sin posición."

        if not args:
            return "Debes especificar qué objeto quieres coger (ej: 'coger palo de madera')."
        
        nombre_objeto_a_coger = " ".join(args).lower()
        habitacion_actual = juego.personaje.posicion
        item_encontrado: Optional[Hoja] = None
        
        if hasattr(habitacion_actual, 'hijos'):
            for posible_item in list(habitacion_actual.hijos): 
                if isinstance(posible_item, Hoja) and hasattr(posible_item, 'nombre'):
                    if posible_item.nombre.lower() == nombre_objeto_a_coger:
                        item_encontrado = posible_item
                        break 
        
        if item_encontrado:
            if juego.personaje.inventario.agregar_item(item_encontrado):
                if hasattr(habitacion_actual, 'eliminar_hijo'):
                    habitacion_actual.eliminar_hijo(item_encontrado)
                    return f"Has recogido: {item_encontrado.nombre}."
                else:
                    juego.personaje.inventario.quitar_item_por_nombre(item_encontrado.nombre) 
                    return f"Error interno: No se pudo quitar {item_encontrado.nombre} de la habitación."
            else:
                return f"No puedes coger {item_encontrado.nombre} (quizás el inventario está lleno)."
        else:
            return f"No ves ningún objeto llamado '{nombre_objeto_a_coger}' aquí."
        
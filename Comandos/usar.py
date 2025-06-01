from typing import  Optional, List
from Comandos.Comando import Comando
from ElementoMapa.Hoja.Arma import Arma




class Usar(Comando):
    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje or not juego.personaje.posicion:
            return "Error: Personaje no inicializado o sin posición."

        if not args:
            return "Debes especificar qué arma quieres usar (ej: 'usar espada mágica')."

        nombre_item_str = " ".join(args).lower()
        item_a_usar = juego.personaje.inventario.buscar_item_por_nombre(nombre_item_str)

        if not item_a_usar:
            return f"No tienes un objeto llamado '{nombre_item_str}' en tu inventario."

        if not Arma or not isinstance(item_a_usar, Arma):
            return f"'{getattr(item_a_usar, 'nombre', nombre_item_str)}' no es un arma válida o no se puede usar como tal."

        if not hasattr(item_a_usar, 'usar'):
            return f"El objeto '{item_a_usar.nombre}' no se puede usar de esta forma."

        print(f"Intentando usar (equipar) el arma '{item_a_usar.nombre}'...")
        fue_exitoso = item_a_usar.usar(juego.personaje)

        if fue_exitoso:
            return f"Has equipado el arma '{item_a_usar.nombre}'."
        else:
            return f"No se pudo usar el arma '{item_a_usar.nombre}'."

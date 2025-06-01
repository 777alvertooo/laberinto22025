from Comandos.Comando import Comando
from typing import  Optional, List
from Ente.Bicho import Bicho
from ElementoMapa.Hoja.Arma import Arma
from Estados.Vivo import Vivo

class Atacar(Comando):
    def _encontrar_bicho_en_sala(self, juego, nombre_bicho_str: str) -> Optional[Bicho]:
        hab_actual = juego.personaje.posicion
        nombre_bicho_lower = nombre_bicho_str.lower()
        if hasattr(juego, 'bichos'): 
            for bicho_obj in juego.bichos:
                if hasattr(bicho_obj, 'estaVivo') and bicho_obj.estaVivo() and \
                   hasattr(bicho_obj, 'posicion') and bicho_obj.posicion == hab_actual and \
                   hasattr(bicho_obj, 'nombre') and bicho_obj.nombre.lower() == nombre_bicho_lower:
                    return bicho_obj
        return None

    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje or not juego.personaje.posicion or \
           not hasattr(juego.personaje, 'estadoEnte') or not isinstance(juego.personaje.estadoEnte, Vivo): 
            return "No puedes atacar ahora (personaje no disponible, sin posición o no está vivo)."

        if not args:
            return "Debes especificar a qué bicho atacar (ej: 'atacar guardián')."

        nombre_bicho_a_atacar_args = []
        nombre_arma_a_usar_args = []
        usando_arma_especifica = False

        if "con" in args:
            try:
                idx_con = args.index("con")
                nombre_bicho_a_atacar_args = args[:idx_con]
                nombre_arma_a_usar_args = args[idx_con+1:]
                if not nombre_bicho_a_atacar_args or not nombre_arma_a_usar_args:
                    return "Formato incorrecto. Prueba: 'atacar <bicho> con <arma>' o 'atacar <bicho>'."
                usando_arma_especifica = True
            except ValueError: 
                nombre_bicho_a_atacar_args = args 
        else:
            nombre_bicho_a_atacar_args = args

        nombre_bicho_str = " ".join(nombre_bicho_a_atacar_args).lower()
        bicho_objetivo = self._encontrar_bicho_en_sala(juego, nombre_bicho_str)

        if not bicho_objetivo:
            return f"No hay ningún bicho llamado '{nombre_bicho_str}' aquí o ya está derrotado."

        poder_ataque_jugador = juego.personaje.poder 
        arma_especifica_usada_msg = ""

        if usando_arma_especifica:
            if not Arma: 
                return "Error: La funcionalidad de armas no está disponible en este momento."

            nombre_arma_str = " ".join(nombre_arma_a_usar_args).lower()
            arma_obj = juego.personaje.inventario.buscar_item_por_nombre(nombre_arma_str)

            if not arma_obj:
                return f"No tienes un arma llamada '{nombre_arma_str}' en tu inventario."
            if not isinstance(arma_obj, Arma):
                return f"'{getattr(arma_obj, 'nombre', nombre_arma_str)}' no es un arma."
            
            if hasattr(arma_obj, 'usar'):
                print(f"Intentando equipar '{arma_obj.nombre}' para el ataque...")
                arma_obj.usar(juego.personaje) 
                poder_ataque_jugador = juego.personaje.poder 
                arma_especifica_usada_msg = f" (con {arma_obj.nombre})"
            else:
                return f"No se puede equipar/usar el arma '{arma_obj.nombre}' de esta forma."
        
       
        print(f"Atacas al {bicho_objetivo.nombre}{arma_especifica_usada_msg}...")
        bicho_objetivo.recibir_daño(poder_ataque_jugador) 

        juego.verificar_condicion_victoria()

        if not bicho_objetivo.estaVivo():
            return None 
        
        # print(f"DEBUG: {bicho_objetivo.nombre} sigue vivo, intentando contraataque.")
        if hasattr(bicho_objetivo, 'intentar_contraataque'):
             bicho_objetivo.intentar_contraataque(juego.personaje) 
             
        if juego.esta_terminado():
            return None 
        
        if bicho_objetivo.estaVivo(): 
            return "El combate continúa..."
        else:
            return None 
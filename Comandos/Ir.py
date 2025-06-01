from Comandos.Comando import Comando
from ElementoMapa.Puerta import Puerta
from Estados.Vivo import Vivo
from Modos.Agresivo import Agresivo
from typing import  Optional, List

class Ir(Comando):
    
    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje or not juego.personaje.posicion:
            return "Error: Personaje no inicializado o sin posición."

        if not args:
            return "Debes especificar una dirección (ej: 'ir norte')."
        
        direccion = args[0].lower()
        habitacion_actual_antes_de_mover = juego.personaje.posicion 
        puerta_a_usar = None

        if hasattr(habitacion_actual_antes_de_mover, direccion): 
            elemento_en_direccion = getattr(habitacion_actual_antes_de_mover, direccion)
            if isinstance(elemento_en_direccion, (Puerta)):
                puerta_a_usar = elemento_en_direccion
        
        if puerta_a_usar:
            print(f"Intentando ir {direccion} a través de '{getattr(puerta_a_usar, 'nombre', 'una puerta')}'...")
            if puerta_a_usar.entrar(juego.personaje): 
                juego.mostrar_descripcion_habitacion_actual() 
                
                if Agresivo: 
                    habitacion_nueva = juego.personaje.posicion 
                    bichos_agresivos_en_sala = []
                    if hasattr(juego, 'bichos'):
                        for bicho_en_juego in juego.bichos:
                            if bicho_en_juego.estaVivo() and \
                               bicho_en_juego.posicion == habitacion_nueva and \
                               isinstance(bicho_en_juego.modo, Agresivo):
                                bichos_agresivos_en_sala.append(bicho_en_juego)
                    
                    if bichos_agresivos_en_sala:
                        for bicho_agresivo in bichos_agresivos_en_sala:
                            if not isinstance(juego.personaje.estadoEnte, Vivo): break 
                            print(f"¡Un {bicho_agresivo.nombre} te ve y se lanza al ataque!")
                            if hasattr(bicho_agresivo, 'intentar_contraataque'):
                                bicho_agresivo.intentar_contraataque(juego.personaje)
                                if not isinstance(juego.personaje.estadoEnte, Vivo):
                                    return "Has sido emboscado y derrotado al entrar..." 
                return None 
            else:
                return f"No pudiste ir hacia {direccion}." 
        else:
            return f"No hay una puerta en la dirección '{direccion}' desde aquí."

class ComandoInventario(Comando):

    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje:
            return "Error: El personaje no existe."
        if not hasattr(juego.personaje, 'inventario'):
            return "Error: El personaje no tiene inventario."
        return juego.personaje.inventario.listar_items()

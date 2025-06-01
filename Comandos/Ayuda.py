from Comandos.Comando import Comando
from typing import Optional, List
class Ayuda(Comando):
    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not hasattr(juego, 'procesador_comandos') or \
           not hasattr(juego.procesador_comandos, 'comandos_disponibles'):
            return "Error: El sistema de ayuda no está disponible."

       
        comandos_agrupados = {}
        
        temp_comandos = {} 
        
        for cmd_key, cmd_obj in juego.procesador_comandos.comandos_disponibles.items():
            obj_id = id(cmd_obj)
            
            if hasattr(cmd_obj, '_alias_direccion_original') and cmd_key in cmd_obj._alias_direccion_original:
                continue

            if obj_id not in temp_comandos:
                temp_comandos[obj_id] = {'principal': cmd_key, 'alias': set()}
            else:
                
                if len(cmd_key) < len(temp_comandos[obj_id]['principal']):
                    temp_comandos[obj_id]['alias'].add(temp_comandos[obj_id]['principal'])
                    temp_comandos[obj_id]['principal'] = cmd_key
                elif cmd_key != temp_comandos[obj_id]['principal']: 
                    temp_comandos[obj_id]['alias'].add(cmd_key)

        ayuda_texto = "Comandos disponibles:\n"
        
        comandos_ordenados = sorted(temp_comandos.values(), key=lambda x: x['principal'])
        
        for grupo in comandos_ordenados:
            ayuda_texto += f"  - {grupo['principal']}"
            if grupo['alias']:
                alias_ordenados = sorted(list(grupo['alias']))
                ayuda_texto += f" (alias: {', '.join(alias_ordenados)})"
            ayuda_texto += "\n"
            
        ayuda_texto += "\nTambién puedes usar direcciones como comandos directos (ej: 'norte', 'sur', 'este', 'oeste'...).\n"
        ayuda_texto += "Para la mayoría de los comandos: <comando> [argumentos...]\n"
        ayuda_texto += "Ejemplos:\n"
        ayuda_texto += "  ir norte\n"
        ayuda_texto += "  coger palo de madera\n"
        ayuda_texto += "  inventario (o inv)\n"
        ayuda_texto += "  mostrar (o estado, info, ver)\n"
        ayuda_texto += "  atacar <nombre del bicho>\n" 
        ayuda_texto += "  atacar <nombre del bicho> con <nombre del arma>\n" 
        ayuda_texto += "  abrir norte\n"
        ayuda_texto += "  soltar palo de madera\n"
        ayuda_texto += "  ayuda (o ?)\n"
        ayuda_texto += "  salir (para terminar el juego)\n"
        
        return ayuda_texto.strip()
try:
    from ElementoMapa.Hoja.Arma import Arma
except ImportError:
    Arma = None
    print("ADVERTENCIA (comandos_concretos): No se pudo importar 'Arma' desde 'arma.py' para ComandoAtacar.")

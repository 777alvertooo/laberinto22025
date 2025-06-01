from typing import TYPE_CHECKING, Optional, Dict
from Comandos.Comando import Comando
from Comandos.Ir import Ir
from Comandos.Coger import Coger
from Comandos.Abrir import Abrir
from Comandos.Cerrar import Cerrar
from Comandos.Mostrar import Mostrar
from Comandos.Soltar import Soltar
from Comandos.Atacar import Atacar
from Comandos.Ayuda import Ayuda
from Comandos.Revisar import Revisar



class ProcesadorComandos:
    def __init__(self, juego):
        self.juego = juego
        self.comandos_disponibles: Dict[str, Comando] = {}
        self._registrar_comandos_iniciales()

    def _registrar_comandos_iniciales(self):
        self.registrar_comando("ir", Ir())
        self.registrar_comando("i", Ir()) 
        self.registrar_comando("norte", Ir(), es_alias_direccion=True, direccion_alias="norte")
        self.registrar_comando("sur", Ir(), es_alias_direccion=True, direccion_alias="sur")
        self.registrar_comando("este", Ir(), es_alias_direccion=True, direccion_alias="este")
        self.registrar_comando("oeste", Ir(), es_alias_direccion=True, direccion_alias="oeste")
        

        self.registrar_comando("coger", Coger())
        self.registrar_comando("tomar", Coger())
        self.registrar_comando("recoger", Coger())
        self.registrar_comando("usar", Coger())

        self.registrar_comando("abrir", Abrir())
        self.registrar_comando("ab", Abrir()) 

        self.registrar_comando("cerrar", Cerrar())
        
        self.registrar_comando("mostrar", Mostrar())
        self.registrar_comando("estado", Mostrar()) 
        self.registrar_comando("info", Mostrar())   
        self.registrar_comando("ver", Mostrar())    


        self.registrar_comando("soltar", Soltar())
        self.registrar_comando("dejar", Soltar()) 

        self.registrar_comando("ayuda", Ayuda())
        self.registrar_comando("help", Ayuda()) 
        self.registrar_comando("?", Ayuda()) 
   

        self.registrar_comando("atacar", Atacar())
        self.registrar_comando("luchar", Atacar()) 

        self.registrar_comando('revisar', Revisar())

        
        print(f"DEBUG: Comandos registrados: {list(self.comandos_disponibles.keys())}") 

    def registrar_comando(self, palabra_clave: str, comando_obj: Comando, es_alias_direccion: bool = False, direccion_alias: str = ""):
        palabra_clave = palabra_clave.lower()
        if es_alias_direccion:
            self.comandos_disponibles[palabra_clave] = comando_obj 
            if not hasattr(comando_obj, '_alias_direccion_original'):
                 comando_obj._alias_direccion_original = {} 
            comando_obj._alias_direccion_original[palabra_clave] = direccion_alias
        else:
            self.comandos_disponibles[palabra_clave.lower()] = comando_obj


    def procesar(self, entrada_str: str) -> Optional[str]:
        partes = entrada_str.strip().lower().split()
        if not partes:
            return "No has introducido ningún comando."

        palabra_clave_cmd = partes[0]
        argumentos = partes[1:]

        comando_obj = self.comandos_disponibles.get(palabra_clave_cmd)

        if comando_obj:
            argumentos_para_comando = argumentos 
            if hasattr(comando_obj, '_alias_direccion_original') and palabra_clave_cmd in comando_obj._alias_direccion_original:
                direccion_fija = comando_obj._alias_direccion_original[palabra_clave_cmd]
                argumentos_para_comando = [direccion_fija] 
            
            try:
                return comando_obj.ejecutar(self.juego, argumentos_para_comando)
            except Exception as e:
                print(f"DEBUG: Error ejecutando el comando '{palabra_clave_cmd}' con args '{argumentos_para_comando}': {e}")
                import traceback
                traceback.print_exc() 
                return f"Hubo un error inesperado al procesar tu comando. ({type(e).__name__})"
        else:
            if palabra_clave_cmd == "ayuda":
                comandos_ayuda = "Comandos disponibles: " + ", ".join(sorted(self.comandos_disponibles.keys()))
                return comandos_ayuda
            return f"Comando desconocido: '{palabra_clave_cmd}'. Escribe 'ayuda' para ver los comandos."
  
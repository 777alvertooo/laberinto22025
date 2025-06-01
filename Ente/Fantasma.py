from Modos.Perezoso import Perezoso 
from Modos.Agresivo import Agresivo 
from Ente.Ente import Ente
from Ente.Personaje import Personaje
from Estados.Vivo import Vivo 
from typing import List, Optional
from ElementoMapa.Hoja.Hoja import Hoja

class Fantasma(Ente):
    def __init__(self, vidas: int, poder: int, posicion, modo, 
                 nombre: str = "fantasma Anónimo", 
                 drop_items: Optional[List['Hoja']] = None): 
        super().__init__() 
        self.nombre: str = nombre
        self.vidas_maximas: int = vidas 
        self.vidas: int = vidas
        self.poder: int = poder
        self.invisible: bool = True
        self.posicion = posicion 
        self.modo = modo
        self.juego = None 
        

        if not self.estadoEnte: 
            self.estadoEnte = Vivo()

        self.drop_items_objs: List['Hoja'] = drop_items if drop_items is not None else []

        print(f"FANTASMA CREADO: {self.nombre} (V:{self.vidas}, P:{self.poder}, Modo:{self.modo}) en Hab: {getattr(self.posicion, 'num', '?')}")

    def estaVivo(self) -> bool:
        return self.vidas > 0

    def recibir_daño(self, cantidad: int):
        if not self.estaVivo():
            return
        
        if getattr(self, "invisible", False):
            print(f"{self.nombre} era invisible, pero ha sido revelado por el ataque.")
            self.invisible = False

        self.vidas -= cantidad
        vidas_mostradas = max(0, self.vidas)
        print(f"¡El {self.nombre} recibe {cantidad} puntos de daño! Vidas restantes: {vidas_mostradas}.")
        
        if self.vidas <= 0:
            self.morir()

    def morir(self):
        if isinstance(self.estadoEnte, Vivo): 
            print(f"¡El {self.nombre} ha sido derrotado!")
            self.estadoEnte.morir(self) 
            self._soltar_drops()
            self._eliminar_del_juego()

    def _soltar_drops(self):
        if self.posicion and self.drop_items_objs:
            if hasattr(self.posicion, 'agregar_hijo'):
                print(f"El {self.nombre} ha soltado algo:")
                for item_obj in self.drop_items_objs:
                    self.posicion.agregar_hijo(item_obj)
                    print(f"  - {item_obj.nombre} aparece en el suelo.")
            else:
                print(f"FANTASMA WARN: La habitación {getattr(self.posicion, 'num', '?')} no puede recibir drops (no tiene 'agregar_hijo').")

    def _eliminar_del_juego(self):
        if self.juego and hasattr(self.juego, 'fantasmas') and self in self.juego.fantasmas:
            self.juego.fantasmas.remove(self)
            #print(f"FANTASMA INFO: {self.nombre} eliminado de la lista de fantasmas del juego.")
        
    def actua(self):
        if self.estaVivo() and self.modo and hasattr(self.modo, 'actuar'):
            if self.invisible:
                print(f"{self.nombre} flota invisiblemente por el laberinto...")
                self.invisible = False  # se vuelve visible tras actuar
            else:
                print(f"{self.nombre} actúa visiblemente.")
            self.modo.actuar(self)

          

    def intentar_contraataque(self, personaje_objetivo: 'Personaje'):
        if self.estaVivo() and self.modo and hasattr(self.modo, 'atacar'):
            #print(f"DEBUG FANTASMA: {self.nombre} intentando contraataque...")
            self.modo.atacar(self, personaje_objetivo)
        elif not self.estaVivo():
            pass 
                


    def __str__(self):
        estado_vida = "Vivo" if self.estaVivo() else "Derrotado"
        visibilidad = "Invisible" if self.invisible else "Visible"
        return f"{self.nombre} [{self.modo}] (Vidas: {self.vidas}/{self.vidas_maximas}, Estado: {estado_vida}, {visibilidad})"

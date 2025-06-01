from Ente.Inventario import Inventario
from .Ente import Ente
from Estados.Vivo import Vivo
import random

class Personaje(Ente):
    def __init__(self, nombre: str, vidas: int, poder: int, juego, capacidad_inventario: int = 5):
        super().__init__()
        self.nombre = nombre
        self.vidas_maximas = vidas  
        self.vidas = vidas         
        self.poder = poder
        self.juego = juego          
        self.inventario = Inventario(capacidad_inventario)
        self.estadoEnte = Vivo()    

    def __str__(self) -> str:
        salud_actual_str = f"{self.vidas}"
        if self.vidas_maximas is not None:
            salud_actual_str += f"/{self.vidas_maximas}"
        
        estado_str = ""
        if self.estadoEnte and hasattr(self.estadoEnte, '__class__'): 
            estado_str = f"(Estado: {self.estadoEnte.__class__.__name__})"

        return (f"--- {self.nombre} {estado_str} ---\n"
                f"  Salud: {salud_actual_str}\n"
                f"  Poder: {self.poder}\n"
                f"  {self.inventario.listar_items()}") 

    def recibir_daño(self, cantidad: int):
        if not self.estaVivo():
            # print(f"{self.nombre} ya está derrotado, no puede recibir más daño.") 
            return

        self.vidas -= cantidad
        
        vidas_mostradas = max(0, self.vidas) 
        
        print(f"¡{self.nombre} recibe {cantidad} puntos de daño! Vidas restantes: {vidas_mostradas}.")
        
        if self.vidas <= 0:
            self.vidas = 0 
            super().morir() 


    def recoger_hoja(self, hoja, habitacion_actual):
        if not hasattr(habitacion_actual, 'hijos'):
            print(f"Error: {getattr(habitacion_actual, 'nombre', 'Esta habitación')} no parece contener objetos (sin 'hijos').")
            return False

        item_encontrado_en_hijos = False
        for hijo in habitacion_actual.hijos: 
            if hijo == hoja: 
                item_encontrado_en_hijos = True
                break
        
        if item_encontrado_en_hijos: 
            if self.inventario.agregar_item(hoja):
                if hasattr(habitacion_actual, 'eliminar_hijo'):
                    habitacion_actual.eliminar_hijo(hoja) 
                    print(f"{self.nombre} recogió: {hoja.nombre}.")
                    return True
                else:
                    self.inventario.quitar_item_por_nombre(hoja.nombre)
                    print(f"Error interno: No se pudo quitar {hoja.nombre} de la habitación.")
                    return False
            else:
                return False
        else:
            print(f"'{hoja.nombre}' no se encuentra en {getattr(habitacion_actual, 'nombre', 'esta habitación')}.")
            return False

    def mostrar_inventario(self):
        print(self.inventario.listar_items())
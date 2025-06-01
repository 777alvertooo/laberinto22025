from Comandos.Comando import Comando
from typing import List, Optional
from ElementoMapa.Contenedor.Baul import Baul
from ElementoMapa.Contenedor.Armario import Armario

class Saquear(Comando):
    def ejecutar(self, juego, args: List[str]) -> Optional[str]:
        if not juego.personaje or not juego.personaje.posicion:
            return "No estás en una habitación válida."

        hab = juego.personaje.posicion
        inventario = juego.personaje.inventario
        nombre_objetivo = " ".join(args).lower()

        for hijo in getattr(hab, "hijos", []):
            if isinstance(hijo, (Baul, Armario)) and hijo.__str__().lower() == nombre_objetivo:
                objetos = hijo.coger_todo()
                recogidos = []
                rechazados = []

                for obj in objetos:
                    if inventario.agregar_item(obj):
                        recogidos.append(obj.nombre)
                    else:
                        rechazados.append(obj.nombre)

                respuesta = ""
                if recogidos:
                    respuesta += "Has saqueado:\n" + "\n".join(f"  - {n}" for n in recogidos)
                if rechazados:
                    respuesta += "\nNo había espacio para:\n" + "\n".join(f"  - {n}" for n in rechazados)
                if not respuesta:
                    respuesta = "No había nada que saquear."
                return respuesta

        return f"No ves ningún '{nombre_objetivo}' que puedas saquear aquí."

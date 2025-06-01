from Comandos.Comando import Comando
from Juego import Juego

class Revisar(Comando):
    def ejecutar(self, juego: Juego, args: list[str]) -> str:
        if not args:
            return "¿Qué contenedor deseas revisar?"

        # En tu proyecto, el personaje guarda su habitación actual en el atributo `posicion`
        habitacion_actual = juego.personaje.posicion
        nombre_objetivo = " ".join(args).lower()

        # Busca solo armarios/baúles en habitacion_actual.hijos
        for hijo in getattr(habitacion_actual, 'hijos', []):
            nombre_hijo = getattr(hijo, 'nombre', '').lower()
            es_armario = hasattr(hijo, 'esArmario') and hijo.esArmario()
            es_baul    = hasattr(hijo, 'esBaul')   and hijo.esBaul()
            if (es_armario or es_baul) and nombre_hijo == nombre_objetivo:
                hijo.abrir(juego.personaje)
                return f"Has revisado el {nombre_hijo}."

        return f"No hay ningún armario o baúl llamado '{nombre_objetivo}' en esta habitación."


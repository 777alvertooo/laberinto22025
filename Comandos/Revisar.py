from Comandos.Comando import Comando
from Juego import Juego

class Revisar(Comando):
    def ejecutar(self, juego: Juego, args: list[str]) -> str:
        if not args:
            return "¿Qué contenedor deseas revisar?"

        habitacion_actual = juego.personaje.posicion
        nombre_objetivo = " ".join(args).lower()

        for hijo in getattr(habitacion_actual, 'hijos', []):
            nombre_hijo = getattr(hijo, 'nombre', '').lower()
            es_armario = hasattr(hijo, 'esArmario') and hijo.esArmario()
            es_baul    = hasattr(hijo, 'esBaul')   and hijo.esBaul()

            if (es_armario or es_baul) and nombre_objetivo in nombre_hijo:
                # 1) Capturamos la lista de nombres que había antes de abrir
                contenidos_antes = getattr(hijo, 'hijos', [])
                if contenidos_antes:
                    nombres_antes = [getattr(obj, 'nombre', str(obj)) for obj in contenidos_antes]
                    lista_antes = ", ".join(nombres_antes)
                    mensaje_contenido = f"'{hijo.nombre}' contenía: {lista_antes}."
                else:
                    mensaje_contenido = f"'{hijo.nombre}' estaba vacío."

                # 2) Ahora abrimos el contenedor (para mover los hijos a la sala y causar daños)
                if not getattr(hijo, 'abierto', False):
                    hijo.abrir(juego.personaje)

                # 3) Devolvemos primero la lista antigua y luego confirmamos que ya no queda nada dentro
                return f"Has abierto '{hijo.nombre}'. {mensaje_contenido}"

        return f"No hay ningún armario o baúl que coincida con '{nombre_objetivo}' en esta habitación."

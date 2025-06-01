import unittest
from Juego.Juego import Juego
from Ente.Personaje import Personaje
from ElementoMapa.Contenedor.Habitacion import Habitacion
from ElementoMapa.Contenedor.Armario import Armario
from ElementoMapa.Hoja.Decorator.Bomba import Bomba
from ElementoMapa.Hoja.Hoja import Hoja
from Comandos.Revisar import Revisar

class TestComandoRevisar(unittest.TestCase):
    def setUp(self):
        self.j = Juego()
        self.p = Personaje("Tester", vidas=20, poder=5, juego=self.j, capacidad_inventario=5)
        self.j.personaje = self.p
        self.hab = Habitacion(1, "Sala", "Desc")
        self.p.posicion = self.hab

        self.arm = Armario("ArmTest")
        self.hab.agregar_hijo(self.arm)

        base = Hoja("Bomba Pequeña")
        self.bomba = Bomba(base, daño=5)
        self.arm.agregar_hijo(self.bomba)

    def test_revisar_armario_devuelve_texto_y_daño(self):
        cmd = Revisar()
        resultado = cmd.ejecutar(self.j, ["ArmTest"])
        self.assertIn("ArmTest contenía: Bomba Pequeña", resultado)
        self.assertEqual(self.p.vidas, 15)
        self.assertNotIn(self.bomba, self.arm.hijos)
        self.assertIn(self.bomba, self.hab.hijos)

    def test_revisar_sin_argumentos(self):
        cmd = Revisar()
        respuesta = cmd.ejecutar(self.j, [])
        self.assertEqual(respuesta, "¿Qué contenedor deseas revisar?")

    def test_revisar_nombre_inexistente(self):
        cmd = Revisar()
        respuesta = cmd.ejecutar(self.j, ["NoExiste"])
        self.assertIn("No hay ningún armario o baúl", respuesta)

if __name__ == "__main__":
    unittest.main()

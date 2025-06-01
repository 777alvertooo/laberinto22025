import unittest
from Ente.Personaje import Personaje

class TestPersonaje(unittest.TestCase):
    def test_recibir_daño_resta_vidas(self):
        p = Personaje("A", vidas=20, poder=5, juego=None, capacidad_inventario=5)
        p.recibir_daño(5)
        self.assertEqual(p.vidas, 15)

    def test_recibir_daño_hasta_muerte(self):
        p = Personaje("B", vidas=10, poder=5, juego=None, capacidad_inventario=5)
        p.recibir_daño(10)
        self.assertEqual(p.vidas, 0)
        self.assertFalse(p.estaVivo())

    def test_no_recibe_daño_si_ya_muerto(self):
        p = Personaje("C", vidas=5, poder=5, juego=None, capacidad_inventario=5)
        p.recibir_daño(5)
        self.assertFalse(p.estaVivo())
        p.recibir_daño(3)
        self.assertEqual(p.vidas, 0)

if __name__ == "__main__":
    unittest.main()

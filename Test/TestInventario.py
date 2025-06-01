import unittest
from Ente.Personaje import Personaje
from ElementoMapa.Hoja.Hoja import Hoja
from ElementoMapa.Contenedor.Habitacion import Habitacion

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.p = Personaje("Tester", vidas=20, poder=5, juego=None, capacidad_inventario=2)
        self.hab = Habitacion(1, "Sala", "")
        self.p.posicion = self.hab

    def test_recoger_hoja_exitosamente(self):
        hoja = Hoja("Llave")
        self.hab.agregar_hijo(hoja)

        ok = self.p.recoger_hoja(hoja, self.hab)
        self.assertTrue(ok)
        self.assertIn(hoja, self.p.inventario.items)
        self.assertNotIn(hoja, self.hab.hijos)

    def test_recoger_hoja_no_existente(self):
        hoja = Hoja("NoExiste")
        ok = self.p.recoger_hoja(hoja, self.hab)
        self.assertFalse(ok)

    def test_inventario_limitado(self):
        h1 = Hoja("A")
        h2 = Hoja("B")
        h3 = Hoja("C")
        self.hab.agregar_hijo(h1)
        self.hab.agregar_hijo(h2)
        self.hab.agregar_hijo(h3)

        self.assertTrue(self.p.recoger_hoja(h1, self.hab))
        self.assertTrue(self.p.recoger_hoja(h2, self.hab))
        ok = self.p.recoger_hoja(h3, self.hab)
        self.assertFalse(ok)
        self.assertIn(h3, self.hab.hijos)

if __name__ == "__main__":
    unittest.main()

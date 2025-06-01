import unittest
from ElementoMapa.Hoja.Decorator.Bomba import Bomba
from ElementoMapa.Hoja.Decorator.Fuego import Fuego
from ElementoMapa.Hoja.Hoja import Hoja

class TestDecoradores(unittest.TestCase):
    def test_bomba_guarda_daño_y_str(self):
        base = Hoja("Base")
        b = Bomba(base, daño=7)
        # Comprobamos que se guardó el daño correctamente
        self.assertEqual(b.daño, 7)
        # __str__ debe contener al menos la palabra "Bomba"
        self.assertIn("Bomba", str(b))

    def test_fuego_guarda_daño_y_str(self):
        base = Hoja("Base")
        f = Fuego(base, daño=3)
        # Comprobamos que se guardó el daño correctamente
        self.assertEqual(f.daño, 3)
        # __str__ debe retornar exactamente "Fuego"
        self.assertEqual(str(f), "Fuego")

if __name__ == "__main__":
    unittest.main()

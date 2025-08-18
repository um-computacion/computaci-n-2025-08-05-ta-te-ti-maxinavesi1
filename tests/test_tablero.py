import unittest
from tateti.tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()

    def test_poner_ficha_valida(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")

    def test_poner_ficha_en_posicion_ocupada(self):
        self.tablero.poner_la_ficha(0, 0, "O")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(0, 0, "X")

if __name__ == "__main__":
    unittest.main()

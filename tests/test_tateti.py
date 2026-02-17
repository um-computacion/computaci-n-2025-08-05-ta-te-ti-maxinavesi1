import unittest
from tateti.tateti import Tateti

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.juego = Tateti("Alice", "Bob")

    def test_tablero_inicial(self):
        for fila in self.juego.tablero:
            self.assertEqual(fila, ["", "", ""])

    def test_turno_inicial(self):
        self.assertEqual(self.juego.jugador_actual().nombre, "Alice")

    def test_ocupar_casilla_valida(self):
        exito = self.juego.ocupar_casilla(0, 0)
        self.assertTrue(exito)
        self.assertEqual(self.juego.tablero[0][0], "X")

    def test_ocupar_casilla_ocupada(self):
        self.juego.ocupar_casilla(0, 0)
        exito = self.juego.ocupar_casilla(0, 0)
        self.assertFalse(exito)

    def test_cambio_turno(self):
        self.juego.ocupar_casilla(0, 0)
        self.assertEqual(self.juego.jugador_actual().nombre, "Bob")

    def test_ganador_fila(self):
        self.juego.tablero = [
            ["X", "X", "X"],
            ["", "", ""],
            ["", "", ""]
        ]
        self.assertTrue(self.juego.hay_ganador())

    def test_ganador_columna(self):
        self.juego.tablero = [
            ["O", "", ""],
            ["O", "", ""],
            ["O", "", ""]
        ]
        self.assertTrue(self.juego.hay_ganador())

    def test_ganador_diagonal(self):
        self.juego.tablero = [
            ["X", "", ""],
            ["", "X", ""],
            ["", "", "X"]
        ]
        self.assertTrue(self.juego.hay_ganador())

    def test_empate_tablero_lleno(self):
        self.juego.tablero = [
            ["X", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertTrue(self.juego.tablero_lleno())
        self.assertFalse(self.juego.hay_ganador())

if __name__ == "__main__":
    unittest.main()


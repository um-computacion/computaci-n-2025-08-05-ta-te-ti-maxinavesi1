import unittest
from tateti.jugador import Jugador

class TestJugador(unittest.TestCase):
    def test_creacion_jugador(self):
        jugador = Jugador("Maxi", "X")
        self.assertEqual(jugador.nombre, "Maxi")
        self.assertEqual(jugador.ficha, "X")

if __name__ == "__main__":
    unittest.main()

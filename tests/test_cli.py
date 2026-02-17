import builtins
from unittest import mock, TestCase
from tateti.cli import main

def run_main_with_inputs(inputs):
    with mock.patch('builtins.input', side_effect=inputs), \
         mock.patch('builtins.print') as mock_print:
        main()
        return [call.args[0] for call in mock_print.call_args_list]

class TestCLI(TestCase):
    def test_empate(self):
        # Secuencia que llena el tablero sin ganador (empate)
        inputs = [
            "Ana", "Beto",
            "0", "0",  # X
            "0", "1",  # O
            "0", "2",  # X
            "1", "1",  # O
            "1", "0",  # X
            "1", "2",  # O
            "2", "1",  # X
            "2", "0",  # O
            "2", "2",  # X
        ]
        output = run_main_with_inputs(inputs)
        self.assertTrue(any("Bienvenidos al Tateti" in line for line in output))
        self.assertTrue(any("Ingrese el nombre del jugador X" in line for line in output))
        self.assertTrue(any("Ingrese el nombre del jugador O" in line for line in output))
        self.assertTrue(any("¡Empate! El tablero está lleno." in line for line in output))

    def test_victoria_x(self):
        inputs = [
            "Ana", "Beto",
            "0", "0", "1", "0",
            "0", "1", "1", "1",
            "0", "2"
        ]
        output = run_main_with_inputs(inputs)
        self.assertTrue(any("¡Hay un ganador!" in line for line in output))

    def test_input_invalido(self):
        inputs = [
            "Ana", "Beto",
            "a", "0",  # fila inválida
            "0", "b",  # columna inválida
            "0", "0",  # válido
            "1", "0",  # válido
            "0", "1",  # válido
            "1", "1",  # válido
            "0", "2",  # válido
            "1", "2",  # válido
            "2", "1",  # válido
            "2", "0",  # válido
            "2", "2",  # válido
        ]
        output = run_main_with_inputs(inputs)
        self.assertTrue(any("Error:" in line for line in output))

if __name__ == "__main__":
    import unittest
    unittest.main()
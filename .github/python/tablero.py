class PosOcupadaException(Exception):
    pass

class Tablero:
    def init(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def poner_la_ficha(self, fil, col, ficha):
        if self.contenedor[fil][col] != "":
            raise PosOcupadaException("La posición ya está ocupada")
        self.contenedor[fil][col] = ficha
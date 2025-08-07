from jugador import Jugador

class Tateti:
    def init(self, nombre_x, nombre_o):
        self.jugador_x = Jugador(nombre_x, "X")
        self.jugador_o = Jugador(nombre_o, "O")
        self.turno = self.jugador_x
        self.tablero = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def ocupar_casilla(self, fil, col):
        if self.tablero[fil][col] == "":
            self.tablero[fil][col] = self.turno.ficha
            self.cambiar_turno()
            return True
        return False

    def cambiar_turno(self):
        self.turno = self.jugador_o if self.turno == self.jugador_x else self.jugador_x

    def jugador_actual(self):
        return self.turno

    def hay_ganador(self):
        t = self.tablero
        for i in range(3):
            if t[i][0] == t[i][1] == t[i][2] != "":
                return True
            if t[0][i] == t[1][i] == t[2][i] != "":
                return True
        if t[0][0] == t[1][1] == t[2][2] != "":
            return True
        if t[0][2] == t[1][1] == t[2][0] != "":
            return True
        return False

    def tablero_lleno(self):
        for fila in self.tablero:
            for casilla in fila:
                if casilla == "":
                    return False
        return
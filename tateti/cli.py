from tateti.tateti import Tateti


def main():
    print("Bienvenidos al Tateti")

    print("Ingrese el nombre del jugador X")
    nombre_x = input()

    print("Ingrese el nombre del jugador O")
    nombre_o = input()

    juego = Tateti(nombre_x, nombre_o)
    ...

    while True:
        print("Tablero:")
        for fila in juego.tablero:
            print(fila)
        print("Turno de:", juego.jugador_actual().nombre)

        try:
            fil = int(input("Ingrese la fila (0, 1 o 2): "))
            col = int(input("Ingrese la columna (0, 1 o 2): "))

            if not juego.ocupar_casilla(fil, col):
                print("Esa casilla ya está ocupada. Intente de nuevo.")
                continue

            if juego.hay_ganador():
                print("¡Hay un ganador!")
                for fila in juego.tablero:
                    print(fila)
                break

            if juego.tablero_lleno():
                print("¡Empate! El tablero está lleno.")
                for fila in juego.tablero:
                    print(fila)
                break

        except Exception as e:
            print("Error:", e)


if __name__ == '__main__':
    main()

from tateti import Tateti

def main():
    print("Bienvenidos al Tateti")
    nombre_x = input("Ingrese el nombre del jugador X: ")
    nombre_o = input("Ingrese el nombre del jugador O: ")
    juego = Tateti(nombre_x, nombre_o)
    while True:
        print("Tablero:")
        for fila in juego.tablero:
            print(fila)
        print("Turno de:", juego.jugador_actual().nombre)
        try:
            fil = int(input("Ingrese fila (0, 1 o 2): "))
            col = int(input("Ingrese col (0, 1 o 2): "))
            if not juego.ocupar_casilla(fil, col):
                print("Esa casilla ya está ocupada. Intenta de nuevo.")
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
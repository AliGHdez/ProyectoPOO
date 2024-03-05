class Gato:
    def __init__(self):
        # Inicializa el tablero del juego con una lista de listas.
        # Cada sublista representa una fila del tablero, inicializada con espacios en blanco.
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        # Inicializa el turno del jugador como 'X'.
        self.turno = 'X'

    def __repr__(self):
        # Representa el tablero como una cadena.
        # Las filas están separadas por saltos de línea y las columnas están separadas por barras verticales.
        return '\n'.join([' | '.join(row) for row in self.tablero])

    def hacer_movimiento(self, fila, columna):
        # Verifica si la casilla seleccionada está vacía.
        # Si es así, coloca el símbolo del jugador en esa posición y cambia el turno al otro jugador.
        # Si no, imprime un mensaje de error.
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = self.turno
            self.turno = 'O' if self.turno == 'X' else 'X'
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")

    def hay_ganador(self):
        # Verifica todas las posibles líneas ganadoras en el tablero.
        # Retorna el símbolo del jugador que gana si alguna línea contiene solo 'X' o 'O', indicando que hay un ganador.
        lineas = (
            self.tablero[0], self.tablero[1], self.tablero[2],
            [self.tablero[i][0] for i in range(3)],
            [self.tablero[i][1] for i in range(3)],
            [self.tablero[i][2] for i in range(3)],
            [self.tablero[i][i] for i in range(3)],
            [self.tablero[i][2 - i] for i in range(3)]
        )
        for linea in lineas:
            if linea == ['X', 'X', 'X']:
                return 'X'
            elif linea == ['O', 'O', 'O']:
                return 'O'
        return None

    def tablero_lleno(self):
        # Verifica si el tablero está lleno, es decir, si no hay espacios en blanco en ninguna casilla.
        return all(' ' not in row for row in self.tablero)

    def juego_terminado(self):
        # Verifica si el juego ha terminado, ya sea porque hay un ganador o porque el tablero está lleno.
        return self.hay_ganador() or self.tablero_lleno()

class JugadorHumano:
    def __init__(self, simbolo):
        # Inicializa el jugador humano con su símbolo ('X' o 'O').
        self.simbolo = simbolo

    def hacer_movimiento(self):
        # Solicita al usuario que ingrese la fila y columna donde quiere colocar su símbolo.
        # Repite el proceso hasta que el usuario ingrese un movimiento válido.
        while True:
            try:
                fila = int(input("Ingrese la fila (0-2): "))
                columna = int(input("Ingrese la columna (0-2): "))
                if fila not in range(3) or columna not in range(3):
                    raise ValueError
                return fila, columna
            except ValueError:
                print("Sintaxis inválida. Por favor, inténta con los numeros 0,1,2.")

class JugadorComputadora:
    def __init__(self, simbolo):
        # Inicializa el jugador de la computadora con su símbolo ('X' o 'O').
        self.simbolo = simbolo

    def hacer_movimiento(self, tablero):
        # Genera una lista de movimientos disponibles en el tablero (casillas vacías).
        # Retorna el primer movimiento disponible (es decir, la primera casilla vacía).
        movimientos_disponibles = [(fila, columna) for fila in range(3) for columna in range(3) if tablero[fila][columna] == ' ']
        return movimientos_disponibles[0] if movimientos_disponibles else None

def jugar():
    # Inicializa una instancia del juego del Gato.
    gato = Gato()
    # Crea una lista de jugadores, un humano y una computadora.
    jugadores = [JugadorHumano('X'), JugadorComputadora('O')]
    # Inicializa el turno actual como el primer jugador en la lista.
    turno_actual = 0

    # Loop principal del juego, que continúa hasta que el juego termina.
    while not gato.juego_terminado():
        print(gato)
        # Determina el jugador actual según el turno.
        jugador_actual = jugadores[turno_actual % 2]

        if isinstance(jugador_actual, JugadorHumano):
            # Si el jugador es humano, solicita su movimiento.
            fila, columna = jugador_actual.hacer_movimiento()
        else:
            # Si el jugador es la computadora, obtiene su movimiento automáticamente.
            fila, columna = jugador_actual.hacer_movimiento(gato.tablero)

        # Realiza el movimiento en el tablero.
        gato.hacer_movimiento(fila, columna)
        # Cambia al siguiente turno.
        turno_actual += 1

    print(gato)

    # Determina el ganador y muestra el mensaje correspondiente.
    ganador = gato.hay_ganador()
    if ganador:
        print(f"¡El jugador {ganador} ha ganado!")
    else:
        print("¡Empate!")

if __name__ == "__main__":
    # Inicia el juego cuando se ejecuta el script.
    jugar()


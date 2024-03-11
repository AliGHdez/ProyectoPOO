class Gato:
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.turno = 'X'

    def __repr__(self):
        return '\n'.join([' | '.join(row) for row in self.tablero])

    def hacer_movimiento(self, fila, columna):
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = self.turno
            self.turno = 'O' if self.turno == 'X' else 'X'
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")

    def hay_ganador(self, tablero):
        lineas = (
            tablero[0], tablero[1], tablero[2],
            [tablero[i][0] for i in range(3)],
            [tablero[i][1] for i in range(3)],
            [tablero[i][2] for i in range(3)],
            [tablero[i][i] for i in range(3)],
            [tablero[i][2 - i] for i in range(3)]
        )
        for linea in lineas:
            if linea == ['X', 'X', 'X']:
                return 'X'
            elif linea == ['O', 'O', 'O']:
                return 'O'
        return None

    def tablero_lleno(self, tablero):
        return all(casilla != ' ' for fila in tablero for casilla in fila)

    def juego_terminado(self):
        return self.hay_ganador(self.tablero) or self.tablero_lleno(self.tablero)

class JugadorHumano:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def hacer_movimiento(self):
        while True:
            try:
                fila = int(input("Ingrese la fila (0-2): "))
                columna = int(input("Ingrese la columna (0-2): "))
                if fila not in range(3) or columna not in range(3):
                    raise ValueError
                return fila, columna
            except ValueError:
                print("Sintaxis inválida. Por favor, inténta con los numeros 0, 1, 2.")

def solicitar_repeticion():
    while True:
        respuesta = input("¿Quieres jugar otra vez? (Sí/No): ").lower()
        if respuesta in ['si', 'sí']:
            return True
        elif respuesta in ['no']:
            return False
        else:
            print("Respuesta no válida. Inténtalo de nuevo.")

class JugadorComputadora:
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.simbolo_oponente = 'O' if simbolo == 'X' else 'X'

    def hacer_movimiento(self, tablero):
        _, mejor_movimiento = self.minimax(tablero, self.simbolo)
        return mejor_movimiento

    def minimax(self, tablero, jugador_actual):
        if gato.hay_ganador(tablero):
            return (1 if jugador_actual == self.simbolo_oponente else -1), None
        elif gato.tablero_lleno(tablero):
            return 0, None

        mejor_puntuacion = float('-inf') if jugador_actual == self.simbolo else float('inf')
        mejor_movimiento = None
        for fila in range(3):
            for columna in range(3):
                if tablero[fila][columna] == ' ':
                    tablero[fila][columna] = jugador_actual
                    puntuacion, _ = self.minimax(tablero, self.simbolo_oponente if jugador_actual == self.simbolo else self.simbolo)
                    tablero[fila][columna] = ' '
                    if jugador_actual == self.simbolo:
                        if puntuacion > mejor_puntuacion:
                            mejor_puntuacion = puntuacion
                            mejor_movimiento = (fila, columna)
                    else:
                        if puntuacion < mejor_puntuacion:
                            mejor_puntuacion = puntuacion
                            mejor_movimiento = (fila, columna)

        return mejor_puntuacion, mejor_movimiento

def jugar():
    while True:
        global gato
        gato = Gato()
        jugadores = [JugadorHumano('X'), JugadorComputadora('O')]
        turno_actual = 0

        while not gato.juego_terminado():
            print(gato)
            jugador_actual = jugadores[turno_actual % 2]

            if isinstance(jugador_actual, JugadorHumano):
                fila, columna = jugador_actual.hacer_movimiento()
            else:
                fila, columna = jugador_actual.hacer_movimiento(gato.tablero)

            gato.hacer_movimiento(fila, columna)

            if gato.hay_ganador(gato.tablero):
                print(f"¡El jugador {jugador_actual.simbolo} ha ganado!")
                break
            elif gato.tablero_lleno(gato.tablero):
                print("¡Empate!")
                break

            turno_actual += 1

        print(gato)

        if not solicitar_repeticion():
            break

jugar()
import random
from openai import OpenAI

# Define tu clave de API de OpenAI
client = OpenAI(api_key='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')

class Gato:
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.turno = 'X'

    def __repr__(self):
        tablero_str = '\n'.join([' | '.join(row) for row in self.tablero])
        separador = "\n--+---+--\n"
        return separador.join(tablero_str.split("\n"))

    def hacer_movimiento(self, fila, columna):
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = self.turno
            self.turno = 'O' if self.turno == 'X' else 'X'
            return True
        else:
            return False

    def hay_ganador(self):
        lineas = (
            self.tablero[0], self.tablero[1], self.tablero[2],
            [self.tablero[i][0] for i in range(3)],
            [self.tablero[i][1] for i in range(3)],
            [self.tablero[i][2] for i in range(3)],
            [self.tablero[i][i] for i in range(3)],
            [self.tablero[i][2 - i] for i in range(3)]
        )
        for linea in lineas:
            if linea == ['X', 'X', 'X'] or linea == ['O', 'O', 'O']:
                return True
        return False

    def tablero_lleno(self):
        return all(casilla != ' ' for fila in self.tablero for casilla in fila)

    def juego_terminado(self):
        return self.hay_ganador() or self.tablero_lleno()

class JugadorHumano:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def hacer_movimiento(self, tablero):
        while True:
            try:
                fila = int(input("Ingrese la fila (0-2): "))
                columna = int(input("Ingrese la columna (0-2): "))
                if fila in range(3) and columna in range(3) and tablero[fila][columna] == ' ':
                    return fila, columna
                else:
                    print("Movimiento inválido. Por favor, inténtalo de nuevo.")
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar números.")

def obtener_mensaje_de_motivacion(ganador):
    if ganador == 'jugador':
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": "¿Podrías darme una frase de felicitaciiones para luego de haber ganado una partida en un juego? Solo incluye la frase en tu respuesta"}
        ],
        max_tokens=30
        )
        #print(completion.choices[0].message.content)
    else:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": "¿Podrías darme una frase de felicitaciiones para luego de haber ganado una partida en un juego? Solo incluye la frase en tu respuesta"}
        ],
        max_tokens=30
        )
        #print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def jugar():
    print("Bienvenido al juego del Gato (Tic-Tac-Toe)!\n")
    jugador_simbolo = input("Elige tu símbolo (X/O): ").upper()
    computadora_simbolo = 'O' if jugador_simbolo == 'X' else 'X'
    print(f"Tú serás '{jugador_simbolo}' y tu oponente será '{computadora_simbolo}'.\n")

    while True:
        gato = Gato()
        jugador_humano = JugadorHumano(jugador_simbolo)
        turno_actual = 'X'

        while not gato.juego_terminado():
            print(gato)
            if turno_actual == jugador_simbolo:
                print("Tu turno.")
                fila, columna = jugador_humano.hacer_movimiento(gato.tablero)
            else:
                print("Turno de la computadora...")
                fila, columna = random.choice([(i, j) for i in range(3) for j in range(3) if gato.tablero[i][j] == ' '])

            if not gato.hacer_movimiento(fila, columna):
                print("Casilla ocupada, elige otra.")
                continue

            if gato.juego_terminado():
                print(gato)
                if gato.hay_ganador():
                    ganador = "jugador" if turno_actual == jugador_simbolo else "computadora"
                    print(obtener_mensaje_de_motivacion(ganador))
                else:
                    print("¡Empate!")
                break

            turno_actual = 'O' if turno_actual == 'X' else 'X'

        respuesta = input("¿Quieres jugar otra vez? (Sí/No): ").lower()
        if respuesta not in ['si', 'sí']:
            break

jugar()
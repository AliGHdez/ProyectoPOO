class Calculadora:
    def sumar(a, b):
        return a + b

# Usando el desempaquetamiento de funciones
numeros = (3, 5)
resultado = Calculadora.sumar(*numeros)

print("La suma es:", resultado)
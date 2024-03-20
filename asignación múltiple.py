class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

# Asignación múltiple al crear una instancia de la clase Rectangulo
base, altura = 5, 3
mi_rectangulo = Rectangulo(base, altura)

# Accediendo a los atributos del objeto
print("Base:", mi_rectangulo.base)
print("Altura:", mi_rectangulo.altura)

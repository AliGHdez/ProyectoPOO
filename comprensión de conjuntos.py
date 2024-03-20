class Estudiante:
    def __init__(self, nombre, materias):
        self.nombre = nombre
        self.materias = materias

# Creamos instancias de la clase Estudiante
estudiantes = [
    Estudiante("Juan", {"Matemáticas", "Física"}),
    Estudiante("María", {"Historia", "Literatura"}),
    Estudiante("Pedro", {"Matemáticas", "Química"})
]

# Creamos un conjunto de todas las materias usando comprensión de conjuntos
todas_las_materias = {materia for estudiante in estudiantes for materia in estudiante.materias}

# Imprimimos el conjunto de todas las materias
print(todas_las_materias)

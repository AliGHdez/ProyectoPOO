class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creamos instancias de la clase Persona
personas = [Persona("Juan", 30), Persona("María", 25), Persona("Pedro", 35)]

# Creamos un diccionario usando comprensión de diccionarios
diccionario_edades = {persona.nombre: persona.edad for persona in personas}

# Imprimimos el diccionario de edades
print(diccionario_edades)
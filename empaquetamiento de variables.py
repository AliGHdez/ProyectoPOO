class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

# Empaquetamiento de variables al crear una instancia de la clase Persona
datos_persona = ("Juan", 30, "Ingeniero")
juan = Persona(*datos_persona)

# Accediendo a los atributos del objeto
print("Nombre:", juan.nombre)
print("Edad:", juan.edad)
print("Ocupación:", juan.ocupacion)

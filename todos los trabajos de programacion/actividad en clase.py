class keiner:
    def __init__(self, nombre, edad, ocupacion, pasion, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        self.pasion = pasion
        self.nacionalidad = nacionalidad

    def realizar_accion(self):
        if self.ocupacion == "estudiante de Ingeniería Informática":
            return f"{self.nombre} está realizando un problema de phyton."
        else:
            return f"{self.nombre} está trabajando en actividades relacionadas con su ocupación."

mi_persona = keiner(
    nombre="keiner quevedo",
    edad=17,
    ocupacion="estudiante de Ingeniería Informática",
    pasion="jugar futbol",
    nacionalidad="colombiano"
)

print(f"Nombre: {mi_persona.nombre}")
print(f"Edad: {mi_persona.edad}")
print(f"Ocupación: {mi_persona.ocupacion}")
print(f"Pasión: {mi_persona.pasion}")
print(f"Nacionalidad: {mi_persona.nacionalidad}")
print(mi_persona.realizar_accion())
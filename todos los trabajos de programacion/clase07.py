class Empleado:
    def __init__(self, id_empleado, nombre, rol):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.rol = rol

    def mostrar_info(self):
        print(f"ID: {self.id_empleado}")
        print(f"Nombre: {self.nombre}")
        print(f"Rol: {self.rol}")


class Gerente(Empleado):
    def __init__(self, id_empleado, nombre):
        super().__init__(id_empleado, nombre, rol="Gerente")
        self.salario = 3 * 1400000  

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Salario: ${self.salario:,}")


class EmpleadoOrdinario(Empleado):
    def __init__(self, id_empleado, nombre, horas_trabajo):
        super().__init__(id_empleado, nombre, rol="Empleado Ordinario")
        self.salario_base = 2 * 1400000   
        self.horas_trabajo = horas_trabajo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Horas de trabajo: {self.horas_trabajo}")
        print(f"Salario base: ${self.salario_base:,}")


gerente = Gerente(1, "GERMAN")
empleado1 = EmpleadoOrdinario(2, "ROBERTA", 40)


print("=== Información del Gerente ===")
gerente.mostrar_info()

print("\n=== Información del Empleado Ordinario ===")
empleado1.mostrar_info()

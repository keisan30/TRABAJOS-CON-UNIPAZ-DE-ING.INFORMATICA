class Vehiculo:
    def __init__(self, marca, modelo, color, placa, tipo, puertas, puestos,
                 combustible, transmision, año, pais_origen, precio, velocidad_maxima):

        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.placa = placa
        self.tipo = tipo                
        self.puertas = puertas
        self.puestos = puestos
        self.combustible = combustible  
        self.transmision = transmision  
        self.año = año
        self.pais_origen = pais_origen
        self.precio = precio
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False
        self.kilometraje = 0.0
        self.nivel_combustible = 100.0  

    def encender(self):
        if not self.encendido:
            if self.nivel_combustible <= 0:
                return f"No se puede encender el vehículo {self.placa}: tanque vacío."
            self.encendido = True
            return f"El {self.marca} {self.modelo} ({self.placa}) ha sido encendido."
        else:
            return f"El vehículo {self.placa} ya está encendido."

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad_actual = 0
            return f"El {self.marca} {self.modelo} ({self.placa}) ha sido apagado correctamente."
        else:
            return f"El vehículo {self.placa} ya estaba apagado."

    def acelerar(self, velocidad):
        if not self.encendido:
            return f"No puedes acelerar, el vehículo {self.placa} está apagado."
        elif velocidad > self.velocidad_maxima:
            return f"No puedes superar los {self.velocidad_maxima} km/h."
        else:
            self.velocidad_actual = velocidad
            self.nivel_combustible -= 0.5
            if self.nivel_combustible < 0:
                self.nivel_combustible = 0
            return f"El vehículo {self.placa} acelera a {self.velocidad_actual} km/h. Combustible: {self.nivel_combustible:.1f}%."

    def frenar(self):
        if self.velocidad_actual > 0:
            self.velocidad_actual -= 15
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
            return f"El vehículo {self.placa} frenó. Velocidad actual: {self.velocidad_actual} km/h."
        else:
            return f"El vehículo {self.placa} ya está detenido."

    def tocar_bocina(self):
        return f"¡Piiiiip! Bocina del vehículo {self.placa} activada."

    def abrir_puertas(self):
        return f"Se han abierto las {self.puertas} puertas del vehículo {self.placa}."

    def mostrar_informacion(self):
        return (f"------ INFORMACIÓN DEL VEHÍCULO ------\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Año: {self.año}\n"
                f"Tipo: {self.tipo}\n"
                f"Color: {self.color}\n"
                f"Placa: {self.placa}\n"
                f"Puertas: {self.puertas}\n"
                f"Puestos: {self.puestos}\n"
                f"Combustible: {self.combustible}\n"
                f"Transmisión: {self.transmision}\n"
                f"País de origen: {self.pais_origen}\n"
                f"Precio: ${self.precio:,}\n"
                f"Velocidad máxima: {self.velocidad_maxima} km/h\n"
                f"Kilometraje: {self.kilometraje:.1f} km\n"
                f"Nivel de combustible: {self.nivel_combustible:.1f}%\n")


mi_auto = Vehiculo(
    marca="tesla",
    modelo="model x",
    color="negro",
    placa="ABC-321",
    tipo="Automóvil",
    puertas=2,
    puestos=2,
    combustible="electrico",
    transmision="Automático",
    año=2026,
    pais_origen="california",
    precio=115970,
    velocidad_maxima=200
)

print(mi_auto.mostrar_informacion())
print(mi_auto.encender())
print(mi_auto.acelerar(120))
print(mi_auto.tocar_bocina())
print(mi_auto.frenar())
print(mi_auto.abrir_puertas())
print(mi_auto.apagar())

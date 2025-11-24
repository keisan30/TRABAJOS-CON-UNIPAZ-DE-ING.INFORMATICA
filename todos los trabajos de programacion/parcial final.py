class Vehiculo:
    def __init__(self, marca, modelo, año, velocidad_actual=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_actual = velocidad_actual
    
    def arrancar(self, incremento):
        self.velocidad_actual += incremento
        print(f"{self.modelo} arrancó a {self.velocidad_actual} km/h")
    
    def frenar(self):
        self.velocidad_actual = 0
        print(f"{self.modelo} frenó.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Velocidad actual: {self.velocidad_actual} km/h")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas, velocidad_actual=0):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        print(f"Carro -> Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, "
              f"Puertas: {self.num_puertas}, Velocidad actual: {self.velocidad_actual} km/h")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, velocidad_actual=0):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.cilindraje = cilindraje

    def mostrar_info(self):
        print(f"Moto -> Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, "
              f"Cilindraje: {self.cilindraje} cc, Velocidad actual: {self.velocidad_actual} km/h")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo, velocidad_actual=0):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Bicicleta -> Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, "
              f"Tipo: {self.tipo}, Velocidad actual: {self.velocidad_actual} km/h")

carro1 = Carro("Toyota", "Corolla", 2020, 4)
carro2 = Carro("Mazda", "CX-30", 2022, 5)

moto1 = Moto("Yamaha", "MT-09", 2021, 900)
moto2 = Moto("Pulsar", "RS-250", 2021, 250)

bicicleta1 = Bicicleta("Trek", "FX 3", 2019, "Montaña")
bicicleta2 = Bicicleta("Specialized", "Sirrus X", 2024, "Híbrida")  

vehiculos = [carro1, carro2, moto1, moto2, bicicleta1, bicicleta2]

for v in vehiculos:
    v.mostrar_info()
    v.arrancar(30)
    v.frenar()
    print("-" * 50)
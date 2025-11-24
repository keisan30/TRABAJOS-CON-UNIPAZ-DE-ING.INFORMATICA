class Jugador:
    def __init__(self, nombre, dorsal, rol):
        self.nombre = nombre
        self.dorsal = dorsal
        self.rol = rol
        self.goles = 0

        self.goles_tapados = 0
        self.bloqueos = 0
        self.jugadas = 0
        self.tiros_arco = 0

    def poner_goles(self, cantidad):
        self.goles += cantidad  

    def poner_estadisticas(self):
        if self.rol == "Arquero":
            self.goles_tapados = int(input(f"¿Cuántos goles tapó {self.nombre}? "))
        elif self.rol == "Lateral":
            self.bloqueos = int(input(f"¿Cuántos jugadores bloqueó {self.nombre}? "))
        elif self.rol == "Armador":
            self.jugadas = int(input(f"¿Cuántas jugadas/parés realizó {self.nombre}? "))
        elif self.rol == "Delantero":
            self.tiros_arco = int(input(f"¿Cuántos tiros al arco hizo {self.nombre}? "))

    def mostrar_info(self):
        print(f"{self.nombre} #{self.dorsal} - Rol: {self.rol}, Goles: {self.goles}")

        if self.rol == "Arquero":
            print(f"   Goles tapados: {self.goles_tapados}")
        elif self.rol == "Lateral":
            print(f"   Bloqueos: {self.bloqueos}")
        elif self.rol == "Armador":
            print(f"   Jugadas realizadas: {self.jugadas}")
        elif self.rol == "Delantero":
            print(f"   Tiros al arco: {self.tiros_arco}")


colombia = [
    Jugador("René Higuita", 1, "Arquero"),
    Jugador("Mauricio Serna", 8, "Lateral"),
    Jugador("Iván Ramiro Córdoba", 2, "Lateral"),
    Jugador("Carlos 'El Pibe' Valderrama", 10, "Armador"),
    Jugador("Radamel Falcao García", 9, "Delantero")
]

españa = [
    Jugador("Iker Casillas", 1, "Arquero"),
    Jugador("Sergio Ramos", 4, "Lateral"),
    Jugador("Carles Puyol", 5, "Lateral"),
    Jugador("Xavi Hernández", 8, "Armador"),
    Jugador("Fernando Torres", 9, "Delantero")
]

print(" PARTIDO: COLOMBIA vs ESPAÑA\n")

tiempo = 1

while tiempo <= 2:
    print(f"\n TIEMPO {tiempo} \n")

    print(" GOLES DEL EQUIPO COLOMBIA:\n")
    for j in colombia:
        while True:
            try:
                goles = int(input(f"¿Cuántos goles hizo {j.nombre} en este tiempo? "))
                if goles < 0:
                    print("No puede ser negativo.")
                else:
                    j.poner_goles(goles)
                    break
            except:
                print("Ingrese un número válido.")

    print("\n ESTADÍSTICAS ADICIONALES COLOMBIA:")
    for j in colombia:
        j.poner_estadisticas()

    print("\n GOLES DEL EQUIPO ESPAÑA:\n")
    for j in españa:
        while True:
            try:
                goles = int(input(f"¿Cuántos goles hizo {j.nombre} en este tiempo? "))
                if goles < 0:
                    print("No puede ser negativo.")
                else:
                    j.poner_goles(goles)
                    break
            except:
                print("Ingrese un número válido.")

    print("\n ESTADÍSTICAS ADICIONALES ESPAÑA:")
    for j in españa:
        j.poner_estadisticas()

    seguir = input("\n¿El partido continúa? (0 = NO, 1 = SÍ): ")

    if seguir == "0":
        break
    else:
        tiempo += 1

goles_colombia = sum(j.goles for j in colombia)
goles_espana = sum(j.goles for j in españa)

print("\n MARCADOR FINAL ")
print(f"Colombia {goles_colombia}  -  {goles_espana} España")

print("\n COLOMBIA ")
for j in colombia:
    j.mostrar_info()

print("\n ESPAÑA ")
for j in españa:
    j.mostrar_info()

print("\nFin del partido.\n")
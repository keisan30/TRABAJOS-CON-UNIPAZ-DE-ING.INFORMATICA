class Personaje:
    def __init__(
        self, nombre, edad, altura, cabello, personalidad, habilidad, frase, objetivo,
        tipo_personaje, nombre_equipo, especial, vidas, resistencia,
        habilidades, oficio, poder_equipo, tipo_arma, daño
    ):
        
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.cabello = cabello
        self.personalidad = personalidad
        self.habilidad = habilidad
        self.frase = frase
        self.objetivo = objetivo

        
        self.tipo_personaje = tipo_personaje
        self.nombre_equipo = nombre_equipo
        self.especial = especial
        self.vidas = vidas
        self.resistencia = resistencia
        self.habilidades = habilidades  
        self.oficio = oficio
        self.poder_equipo = poder_equipo
        self.tipo_arma = tipo_arma
        self.daño = daño

    def describir(self):
        descripcion = f"""
         Descripción de {self.nombre} 
        Edad: {self.edad} años
        Altura: {self.altura} m
        Cabello: {self.cabello}
        Personalidad: {self.personalidad}
        Habilidad principal: {self.habilidad}
        Frase típica: "{self.frase}"
        Objetivo: {self.objetivo}

        Tipo de personaje: {self.tipo_personaje}
        Equipo: {self.nombre_equipo}
        Especial: {self.especial}
        Vidas: {self.vidas}
        Resistencia: {self.resistencia}
        Oficio: {self.oficio}
        Poder de equipo: {self.poder_equipo}
        Arma: {self.tipo_arma}
        Daño del arma: {self.daño}

        Habilidades adicionales:
        - {chr(10).join(self.habilidades)}
        """
        return descripcion


class Companion:
    def __init__(self, nombre, edad, especie, color, habilidad, personalidad, frase, gusto):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.color = color
        self.habilidad = habilidad
        self.personalidad = personalidad
        self.frase = frase
        self.gusto = gusto

    def describir(self):
        descripcion = f"""
         Descripción de {self.nombre} 
        Edad: {self.edad} años
        Especie: {self.especie}
        Color: {self.color}
        Personalidad: {self.personalidad}
        Habilidad principal: {self.habilidad}
        Frase típica: "{self.frase}"
        Lo que más disfruta: {self.gusto}
        """
        return descripcion


if __name__ == "__main__":
    
    finn = Personaje(
        nombre="Finn el Humano",
        edad=17,
        altura=1.65,
        cabello="Rubio (bajo su gorro blanco)",
        personalidad="Valiente, optimista, impulsivo",
        habilidad="Espadachín experto",
        frase="¡Matemático!",
        objetivo="Ayudar a los demás y vivir aventuras",

        tipo_personaje="Héroe",
        nombre_equipo="Equipo Aventura",
        especial="Coraje infinito",
        vidas=5,
        resistencia=80,
        habilidades=["Golpe giratorio", "Salto acrobático", "Determinación pura"],
        oficio="Aventurero",
        poder_equipo="Inspirar a sus aliados",
        tipo_arma="Espada de Demonio",
        daño=45
    )

    jake = Companion(
        nombre="Jake el Perro",
        edad=28,
        especie="Perro mágico",
        color="Amarillo dorado",
        habilidad="Puede estirarse y cambiar de forma",
        personalidad="Relajado, divertido, sabio",
        frase="¡Tranquilo, viejo!",
        gusto="Comer panqueques, dormir y la música"
    )

    print(finn.describir())
    print(jake.describir())

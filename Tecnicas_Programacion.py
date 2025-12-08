## Clase base
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"Nombre: {self.nombre}")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha sido derrotado.")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = max(0, self.daño(enemigo))  # Evitar daño negativo
        enemigo.vida -= daño
        print(f"{self.nombre} ha causado {daño} de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print("Vida restante de", enemigo.nombre, ":", enemigo.vida)
        else:
            enemigo.morir()

# Clase Carla (tipo guerrera)
class Carla(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma

    def cambiar_arma(self):
        print("Selecciona arma:")
        print("1. Arma de fuego (daño x9)")
        print("2. Hacha pesada (daño x7)")
        opcion = int(input("Opción: "))
        if opcion == 1:
            self.arma = 9
        elif opcion == 2:
            self.arma = 7
        else:
            print("Arma no válida")

    def atributos(self):
        super().atributos()
        print("· Arma (potencia):", self.arma)

    def daño(self, enemigo):
        return (self.fuerza * self.arma) - enemigo.defensa

# Clase Calo (tipo mago)
class Calo(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, hechizo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.hechizo = hechizo

    def atributos(self):
        super().atributos()
        print("· Hechizo (poder):", self.hechizo)

    def daño(self, enemigo):
        return (self.inteligencia * self.hechizo) - enemigo.defensa

# Función de combate
def combate(jugador1, jugador2):
    turno = 1
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        jugador1.atacar(jugador2)
        if jugador2.esta_vivo():
            jugador2.atacar(jugador1)
        turno += 1

    print("\n=== Fin del combate ===")
    if jugador1.esta_vivo():
        print("Ganador:", jugador1.nombre)
    elif jugador2.esta_vivo():
        print("Ganador:", jugador2.nombre)
    else:
        print("¡Empate!")

# Crear personajes y probar
carla = Carla("Carla", 12, 5, 4, 100, 3)
calo = Calo("Calo", 4, 15, 3, 100, 4)

carla.atributos()
calo.atributos()

combate(carla, calo)


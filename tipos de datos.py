import math

# ----------------------------
# Clase Círculo
# ----------------------------
# Esta clase representa un círculo.
# Tiene el atributo 'radio' y métodos
# para calcular el área y el perímetro.
class Circulo:
    def __init__(self, radio):
        self.radio = radio  # Guardamos el valor del radio

    # Esta función calcula el área del círculo
    def calcular_area(self):
        return math.pi * self.radio * self.radio

    # Esta función calcula el perímetro del círculo (circunferencia)
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


# ----------------------------
# Clase Rectángulo
# ----------------------------
# Esta clase representa un rectángulo.
# Tiene dos atributos: base y altura.
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base      # Guardamos la base
        self.altura = altura  # Guardamos la altura

    # Calcula el área del rectángulo
    def calcular_area(self):
        return self.base * self.altura

    # Calcula el perímetro del rectángulo
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


# ------------------------------------
# Ejemplo de uso para las dos clases
# ------------------------------------

# Crear un círculo de radio 5
cir = Circulo(5)
print("Círculo:")
print("Área:", cir.calcular_area())
print("Perímetro:", cir.calcular_perimetro())

# Crear un rectángulo de base 4 y altura 6
rect = Rectangulo(4, 6)
print("\nRectángulo:")
print("Área:", rect.calcular_area())
print("Perímetro:", rect.calcular_perimetro())

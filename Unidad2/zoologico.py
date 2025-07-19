## Clase base con mayúscula y encapsulación consistente
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre   # atributo encapsulado
        self.edad = edad

    def obtener_nombre(self):
        return self._nombre

    def hacer_sonido(self):
        return "Este animal hace un sonido."

    def descripcion(self):
        return f"{self._nombre} tiene {self.edad} años."

# Clase derivada 1
class Foca(Animal):
    def __init__(self, nombre, edad, habitat):
        super().__init__(nombre, edad)
        self.habitat = habitat  # atributo específico de Foca

    # Polimorfismo: sobrescribir método
    def hacer_sonido(self):
        return "¡Ow ow!"

# Clase derivada 2
class Gato(Animal):
    def __init__(self, nombre, edad, color_pelaje):
        super().__init__(nombre, edad)
        self.color_pelaje = color_pelaje

    # Polimorfismo: sobrescribir método
    def hacer_sonido(self):
        return "¡Miau!"

# Programa principal para probar las clases
def main():
    foca1 = Foca("Lupe", 10, "océano antártico")
    gato1 = Gato("Cloe", 3, "Blanco")

    animales = [foca1, gato1]

    for animal in animales:
        print(animal.descripcion())
        print(f"Sonido: {animal.hacer_sonido()}")
        print("-----")

if __name__ == "__main__":
    main()

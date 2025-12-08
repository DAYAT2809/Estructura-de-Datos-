# Promedio Semanal del Clima - Programación Orientada a Objetos (POO)

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Solicitar al usuario ingresar las temperaturas de los 7 días de la semana
        y guardar en la lista de "temperaturas"
        """
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio de las temperaturas ingresadas
        """
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio

def main():
    print("Promedio Semanal del clima (Programación Orientada a Objetos)")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"Promedio Semanal del clima: {promedio:.2f}°C")

if __name__ == "__main__":
    main()


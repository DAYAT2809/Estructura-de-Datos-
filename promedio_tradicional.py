# Promedio Semanal del Clima - rogramación Orientada a Objetos (Tradicional)

def ingresar_temperaturas():
    """
    Solicitar al usuario ingresar las temperaturas de la semana.
    Al finalizar, entrega todas las temperaturas en forma de lista.
    """
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcular el promedio de una lista de temperaturas.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

def main():
    print("Promedio Semanal del Clima (Programación Tradicional)")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio de la temperatura es: {promedio:.2f}°C")

# Ejecución del programa
if __name__ == "__main__":
    main()
    









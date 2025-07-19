# Programa para gestionar información básica de un registro de persona
# Permite ingresar nombre, edad, altura, carrera, país y si es estudiante,
# luego muestra la información y determina si la persona es mayor de edad.

def solicitar_datos_personales():
    """
    Solicita al usuario ingresar datos personales y los almacena en un diccionario.
    Retorna: diccionario con los datos.
    """

    # Pedimos al usuario ingresar su nombre completo
    nombre = input("Ingrese el nombre completo: ")

    # Ciclo para validar la edad ingresada
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad < 0:
                # La edad no puede ser negativa
                print("La edad no puede ser negativa. Intente nuevamente.")
                continue
            break  # Edad válida, salimos del ciclo
        except ValueError:
            # Si no es un número entero válido, mostramos error
            print("Por favor ingrese un número entero válido para la edad.")

    # Ciclo para validar la altura
    while True:
        try:
            altura = float(input("Ingrese la altura en metros (ej. 1.70): "))
            if altura <= 0:
                print("La altura debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número válido para la altura.")

    # Pedimos la carrera que estudia la persona
    carrera = input("Ingrese la carrera: ")

    # Pedimos el país de residencia
    pais = input("Ingrese el país: ")

    # Preguntamos si la persona es estudiante y convertimos a booleano
    es_estudiante_str = input("¿Es estudiante? (si/no): ").strip().lower()
    es_estudiante = es_estudiante_str == "si"

    # Creamos un diccionario con los datos personales
    persona = {
        "nombre": nombre,
        "edad": edad,
        "altura": altura,
        "carrera": carrera,
        "pais": pais,
        "es_estudiante": es_estudiante
    }

    return persona


def mostrar_informacion_persona(persona: dict):
    """
    Muestra la información almacenada de la persona y evalúa si es mayor de edad.
    """

    print("\n--- Información del registro ---")

    # Mostramos cada dato y su tipo
    print(f"Nombre: {persona['nombre']} (tipo: {type(persona['nombre'])})")
    print(f"Edad: {persona['edad']} años (tipo: {type(persona['edad'])})")
    print(f"Altura: {persona['altura']} m (tipo: {type(persona['altura'])})")
    print(f"Carrera: {persona['carrera']} (tipo: {type(persona['carrera'])})")
    print(f"País: {persona['pais']} (tipo: {type(persona['pais'])})")
    print(f"Es estudiante: {'Sí' if persona['es_estudiante'] else 'No'} (tipo: {type(persona['es_estudiante'])})")

    # Evaluamos si la persona es mayor de edad (18 o más)
    es_mayor_de_edad = persona["edad"] >= 18

    # Mostramos si es mayor de edad (valor booleano)
    print(f"¿Es mayor de edad?: {'Sí' if es_mayor_de_edad else 'No'} (booleano)")


def main():
    """
    Función principal que controla el flujo del programa.
    Primero solicita los datos y luego muestra la información.
    """
    print("\n--- Gestión del registro ---")
    persona = solicitar_datos_personales()
    mostrar_informacion_persona(persona)


# Punto de entrada del programa: este bloque garantiza que main() solo se ejecute
# si el archivo se ejecuta directamente, no si es importado como módulo
if __name__ == "__main__":
    main()

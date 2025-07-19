import os
import subprocess

def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no existe.")
        return None
    except Exception as error:
        print(f"Ha ocurrido un error al leer el archivo: {error}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix/Linux/Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': {
            'nombre': 'Unidad 1',
            'carpeta': 'Unidad1',
            'proyectos': {
                '1': 'zoologico.py',
                '2': 'reserva_hotel.py'
            }
        },
        '2': {
            'nombre': 'Unidad 2',
            'carpeta': 'Unidad2',
            'proyectos': {
                '1': 'datos_personales.py',
                '2': 'Banco.py'
            }
        }
    }

    while True:
        print("\n=== MENÚ PRINCIPAL - DASHBOARD ===")
        for key, unidad in unidades.items():
            print(f"{key} - {unidad['nombre']}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            unidad = unidades[eleccion_unidad]
            carpeta = unidad['carpeta']
            proyectos = unidad['proyectos']
            mostrar_sub_menu(proyectos, os.path.join(ruta_base, carpeta))
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_sub_menu(proyectos, ruta_unidad):
    while True:
        print("\n--- SUBMENÚ: Selecciona un proyecto ---")
        for key, script in proyectos.items():
            print(f"{key} - {script}")
        print("0 - Regresar al menú principal")

        eleccion_script = input("Elige un proyecto o '0' para regresar: ")

        if eleccion_script == '0':
            break
        elif eleccion_script in proyectos:
            ruta_script = os.path.join(ruta_unidad, proyectos[eleccion_script])
            codigo = mostrar_codigo(ruta_script)
            if codigo:
                ejecutar = input("¿Deseas ejecutar el script? (1: Sí, 0: No): ")
                if ejecutar == '1':
                    ejecutar_codigo(ruta_script)
                elif ejecutar == '0':
                    print("No se ejecutó el script.")
                else:
                    print("Opción inválida.")
                input("\nPresiona Enter para continuar...")
        else:
            print("Opción no válida. Intenta otra vez.")

# Ejecutar el menú si es el archivo principal
if __name__ == "__main__":
    mostrar_menu()


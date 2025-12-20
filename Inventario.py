
import json
from producto import Producto

# Clase Inventario - Maneja un conjunto de productos
class Inventario:
    def __init__(self):
        """Inicializa el inventario vacío"""
        self.productos = {}

    def agregar_producto(self, producto: Producto):
        """Agrega un producto al inventario"""
        self.productos[producto.id] = producto

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID"""
        if id_producto in self.productos:
            del self.productos[id_producto]

    def modificar_producto(self, id_producto, nuevo_producto: Producto):
        """Modifica los datos de un producto existente"""
        if id_producto in self.productos:
            self.productos[id_producto] = nuevo_producto

    def mostrar_productos(self):
        """Devuelve todos los productos como lista"""
        return list(self.productos.values())

    def guardar_archivo(self, archivo="inventario.json"):
        """Guarda el inventario en un archivo JSON"""
        with open(archivo, "w") as f:
            json.dump({id: p.to_dict() for id, p in self.productos.items()}, f, indent=4)

    def cargar_archivo(self, archivo="inventario.json"):
        """Carga el inventario desde un archivo JSON"""
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                self.productos = {id: Producto(**info) for id, info in data.items()}
        except FileNotFoundError:
            self.productos = {}


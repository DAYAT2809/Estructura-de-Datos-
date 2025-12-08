# Clase Producto - Representa un producto del inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto
        :param id_producto: ID único del producto
        :param nombre: Nombre del producto
        :param cantidad: Cantidad disponible en inventario
        :param precio: Precio unitario del producto
        """
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """Representación en texto del producto"""
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_dict(self):
        """Convierte el objeto en un diccionario para guardarlo en JSON"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

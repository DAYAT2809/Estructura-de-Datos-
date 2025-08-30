# =========================
# Sistema de Gestión de Inventarios Mejorado
# Manejo de Archivos y Excepciones
# =========================

class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_cantidad(self):
        return self.cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    # Para mostrar bonito en consola
    def mostrar(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad}"

    # Para guardar/leer del archivo (formato CSV simple)
    def a_linea_archivo(self):
        return f"{self.id_producto},{self.nombre},{self.precio},{self.cantidad}"

    @staticmethod
    def desde_linea_archivo(linea):
        id_producto, nombre, precio, cantidad = linea.strip().split(",")
        return Producto(id_producto, nombre, float(precio), int(cantidad))


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()  # cargar automáticamente al iniciar

    # =========================
    # Guardar inventario en archivo
    # =========================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(p.a_linea_archivo() + "\n")
            print("✅ Inventario guardado correctamente en archivo.")
        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al guardar: {e}")

    # =========================
    # Cargar inventario desde archivo
    # =========================
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for num_linea, linea in enumerate(f, start=1):
                    linea = linea.strip()
                    if not linea:
                        continue
                    try:
                        producto = Producto.desde_linea_archivo(linea)
                        self.productos.append(producto)
                    except ValueError:
                        print(f"⚠️ Advertencia: línea {num_linea} corrupta en archivo, se omitió.")
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("❌ Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al cargar: {e}")

    # =========================
    # Métodos del Inventario
    # =========================
    def add_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto añadido correctamente.")

    def actualizar_precio(self, id_producto, nuevo_precio):
        for p in self.productos:
            if p.get_id() == id_producto:
                p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("✅ Precio actualizado correctamente.")
                return
        print("❌ Error: Producto no encontrado.")

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        for p in self.productos:
            if p.get_id() == id_producto:
                p.set_cantidad(nueva_cantidad)
                self.guardar_en_archivo()
                print("✅ Cantidad actualizada correctamente.")
                return
        print("❌ Error: Producto no encontrado.")

    def eliminar_producto(self, id_producto):
        for p in list(self.productos):
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("✅ Producto eliminado correctamente.")
                return
        print("❌ Error: Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📂 Inventario vacío.")
        else:
            print("📦 Inventario actual:")
            for p in self.productos:
                print(p.mostrar())


# =========================
# PROGRAMA PRINCIPAL
# =========================
if __name__ == "__main__":
    inventario = Inventario()

    # Cargar productos iniciales si el inventario está vacío
    if not inventario.productos:
        inventario.add_producto(Producto("P001", "CHOCOLATE", 1.30, 20))
        inventario.add_producto(Producto("P002", "HUEVOS", 4.00, 52))
        inventario.add_producto(Producto("P003", "TE", 1.05, 2))
        inventario.add_producto(Producto("P004", "PAN", 1.00, 20))
        inventario.add_producto(Producto("P005", "LECHE", 0.99, 5))

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1 - Añadir producto")
        print("2 - Mostrar inventario")
        print("3 - Actualizar precio de un producto")
        print("4 - Actualizar cantidad de un producto")
        print("5 - Eliminar producto")
        print("6 - Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            id_p = input("ID del producto: ").strip()
            nombre = input("Nombre: ").strip()
            try:
                precio = float(input("Precio: ").strip())
                cantidad = int(input("Cantidad: ").strip())
                nuevo = Producto(id_p, nombre, precio, cantidad)
                inventario.add_producto(nuevo)
            except ValueError:
                print("Error: Precio o cantidad inválidos.")

        elif opcion == "2":
            inventario.mostrar_inventario()

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ").strip()
            try:
                nuevo_precio = float(input("Nuevo precio: ").strip())
                inventario.actualizar_precio(id_p, nuevo_precio)
            except ValueError:
                print("Error: Precio inválido.")

        elif opcion == "4":
            id_p = input("ID del producto a actualizar: ").strip()
            try:
                nueva_cantidad = int(input("Nueva cantidad: ").strip())
                inventario.actualizar_cantidad(id_p, nueva_cantidad)
            except ValueError:
                print("Error: Cantidad inválida.")

        elif opcion == "5":
            id_producto = input("ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_producto)

        elif opcion == "6":
            print("Guardando cambios y saliendo del sistema...")
            inventario.guardar_en_archivo()
            break

        else:
            print("Opción no válida, intenta de nuevo.")

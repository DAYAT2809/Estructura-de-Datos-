import tkinter as tk
from tkinter import ttk, messagebox
from inventario import Inventario
from producto import Producto

# Clase principal de la aplicación con Tkinter
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventario")

        # Información del estudiante
        info = tk.Label(root, text="Estudiante: Tu Nombre | Carrera: X | Paralelo: Y", font=("Arial", 12))
        info.pack(pady=10)

        # Menú principal
        menubar = tk.Menu(root)
        root.config(menu=menubar)
        menu_principal = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opciones", menu=menu_principal)
        menu_principal.add_command(label="Productos", command=self.abrir_ventana_productos)
        menu_principal.add_separator()
        menu_principal.add_command(label="Salir", command=root.quit)
        # Inicializar inventario
        self.inventario = Inventario()
        self.inventario.cargar_archivo()

        # Atajo de teclado para salir con Escape
        root.bind("<Escape>", lambda e: root.quit())

    def abrir_ventana_productos(self):
        """Abre la ventana secundaria para gestionar productos"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestión de Productos")

        # Campos de entrada
        tk.Label(ventana, text="ID").grid(row=0, column=0)
        tk.Label(ventana, text="Nombre").grid(row=1, column=0)
        tk.Label(ventana, text="Cantidad").grid(row=2, column=0)
        tk.Label(ventana, text="Precio").grid(row=3, column=0)

        id_entry = tk.Entry(ventana)
        nombre_entry = tk.Entry(ventana)
        cantidad_entry = tk.Entry(ventana)
        precio_entry = tk.Entry(ventana)

        id_entry.grid(row=0, column=1)
        nombre_entry.grid(row=1, column=1)
        cantidad_entry.grid(row=2, column=1)
        precio_entry.grid(row=3, column=1)

        # Tabla para mostrar productos
        tree = ttk.Treeview(ventana, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings")
        for col in ("ID", "Nombre", "Cantidad", "Precio"):
            tree.heading(col, text=col)
        tree.grid(row=5, column=0, columnspan=4)

        # Función para actualizar tabla
        def actualizar_tabla():
            for row in tree.get_children():
                tree.delete(row)
            for p in self.inventario.mostrar_productos():
                tree.insert("", "end", values=(p.id, p.nombre, p.cantidad, p.precio))

        # Función para agregar producto
        def agregar():
            try:
                p = Producto(id_entry.get(), nombre_entry.get(), int(cantidad_entry.get()), float(precio_entry.get()))
                self.inventario.agregar_producto(p)
                self.inventario.guardar_archivo()
                actualizar_tabla()
            except ValueError:
                messagebox.showerror("Error", "Cantidad debe ser entero y Precio debe ser número decimal.")

        # Función para eliminar producto
        def eliminar():
            seleccionado = tree.selection()
            if seleccionado:
                valores = tree.item(seleccionado[0], "values")
                self.inventario.eliminar_producto(valores[0])
                self.inventario.guardar_archivo()
                actualizar_tabla()

        # Función para modificar producto
        def modificar():
            seleccionado = tree.selection()
            if seleccionado:
                valores = tree.item(seleccionado[0], "values")
                try:
                    nuevo = Producto(id_entry.get(), nombre_entry.get(), int(cantidad_entry.get()),
                                     float(precio_entry.get()))
                    self.inventario.modificar_producto(valores[0], nuevo)
                    self.inventario.guardar_archivo()
                    actualizar_tabla()
                except ValueError:
                    messagebox.showerror("Error", "Cantidad debe ser entero y Precio debe ser número decimal.")

        # Botones de acciones
        tk.Button(ventana, text="Agregar", command=agregar).grid(row=4, column=0)
        tk.Button(ventana, text="Modificar", command=modificar).grid(row=4, column=1)
        tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=4, column=2)
        tk.Button(ventana, text="Listar", command=actualizar_tabla).grid(row=4, column=3)

        # Atajos de teclado para eliminar
        ventana.bind("<Delete>", lambda e: eliminar())
        ventana.bind("<d>", lambda e: eliminar())

        actualizar_tabla()

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
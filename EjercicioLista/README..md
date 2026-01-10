# Sistema de Gestión de Inventario

Este proyecto implementa un sistema de gestión de inventarios aplicando **POO, colecciones, archivos JSON y una interfaz gráfica con Tkinter**.

## Características
- Clase `Producto` y `Inventario` en archivos separados.
- Operaciones CRUD: Agregar, Modificar, Eliminar y Listar productos.
- Persistencia con archivos JSON.
- Interfaz gráfica en Tkinter con `TreeView`.
- Atajos de teclado:
  - `Delete` o `D`: Eliminar producto seleccionado.
  - `Escape`: Cerrar aplicación.

## Estructura del proyecto
inventario_proyecto/
├── producto.py # Clase Producto
├── inventario.py # Clase Inventario
├── main.py # Interfaz gráfica (Tkinter)
└── inventario.json # Archivo para guardar los productos
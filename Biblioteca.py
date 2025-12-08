# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # El título y el autor se almacenan como tupla porque son inmutables
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        # Lista de libros actualmente prestados
        self.libros_prestados = []

    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return "No tiene libros prestados."
        return "\n".join([str(libro) for libro in self.libros_prestados])

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario: key=ISBN, value=Libro
        self.usuarios_ids = set()  # Conjunto de IDs
        self.usuarios = {}  # Diccionario: key=ID, value=Usuario

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' añadido correctamente.")

    def registrar_usuario(self, usuario):
        if usuario.user_id in self.usuarios_ids:
            print(f"El usuario con ID {usuario.user_id} ya está registrado.")
        else:
            self.usuarios_ids.add(usuario.user_id)
            self.usuarios[usuario.user_id] = usuario
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios_ids:
            del self.usuarios[user_id]
            self.usuarios_ids.remove(user_id)
            print(f"Usuario con ID {user_id} eliminado.")
        else:
            print(f"Usuario con ID {user_id} no está registrado.")

    def prestar_libro(self, isbn, user_id):
        if isbn not in self.libros:
            print(f"Libro con ISBN {isbn} no disponible.")
            return
        if user_id not in self.usuarios:
            print(f"Usuario con ID {user_id} no registrado.")
            return
        libro = self.libros.pop(isbn)
        self.usuarios[user_id].libros_prestados.append(libro)
        print(f"Libro '{libro.info[0]}' prestado a {self.usuarios[user_id].nombre}.")

    def devolver_libro(self, isbn, user_id):
        if user_id not in self.usuarios:
            print(f"Usuario con ID {user_id} no registrado.")
            return
        usuario = self.usuarios[user_id]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                return
        print(f"El usuario no tiene el libro con ISBN {isbn} prestado.")

    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros.values():
            if "titulo" in kwargs and kwargs["titulo"].lower() in libro.info[0].lower():
                resultados.append(libro)
            elif "autor" in kwargs and kwargs["autor"].lower() in libro.info[1].lower():
                resultados.append(libro)
            elif "categoria" in kwargs and kwargs["categoria"].lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados if resultados else "No se encontraron libros."


# -------------------------
# Pruebas del sistema
# -------------------------
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "123")
libro2 = Libro("Python para Todos", "Raúl González", "Programación", "456")
libro3 = Libro("La Odisea", "Homero", "Épica", "789")

# Añadir libros
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Registrar usuarios
usuario1 = Usuario("Dayo", "U001")
usuario2 = Usuario("Ana", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("123", "U001")
biblioteca.prestar_libro("456", "U002")

# Mostrar libros prestados
print("\nLibros prestados a Dayo:")
print(usuario1.listar_libros_prestados())

# Devolver libro
biblioteca.devolver_libro("123", "U001")

# Buscar libro
print("\nBuscar libros de categoría Programación:")
for libro in biblioteca.buscar_libro(categoria="Programación"):
    print(libro)
PythonProject9
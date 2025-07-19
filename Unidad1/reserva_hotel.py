# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def mostrar_info(self):
        print(f"Habitación {self.numero} | Tipo: {self.tipo} | Precio: ${self.precio} | Disponible: {self.disponible}")

    def ocupar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True


# Clase que representa a un cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_info(self):
        print(f"Cliente: {self.nombre} | Cédula: {self.cedula}")


# Clase que representa una reserva
class Reserva:
    def __init__(self, habitacion, cliente):
        self.habitacion = habitacion
        self.cliente = cliente

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.ocupar()
            print(f"Reserva confirmada para {self.cliente.nombre} en la habitación {self.habitacion.numero}")
        else:
            print("La habitación está ocupada.")

    def cancelar_reserva(self):
        self.habitacion.liberar()
        print(f"Reserva cancelada para la habitación {self.habitacion.numero}")

# Crear una habitación y un cliente
habitacion1 = Habitacion(901, "Compartida", 80)
cliente1 = Cliente("Scarleth Tenecota", "1723456789")

# Mostrar información
habitacion1.mostrar_info()
cliente1.mostrar_info()

# Crear y confirmar una reserva
reserva1 = Reserva(habitacion1, cliente1)
reserva1.confirmar_reserva()

# Mostrar estado actualizado
habitacion1.mostrar_info()

# Cancelar reserva
reserva1.cancelar_reserva()
habitacion1.mostrar_info()

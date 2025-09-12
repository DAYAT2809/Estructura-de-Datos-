import tkinter as tk
from tkinter import messagebox

# ----------------------------
# Aplicación de Tickets de Avión
# ----------------------------

def agregar_ticket():
    nombre = entrada_nombre.get().strip()
    destino = entrada_destino.get().strip()

    if nombre and destino:  # Ambos campos deben tener datos
        ticket = f"Pasajero: {nombre} | Destino: {destino}"
        lista_tickets.insert(tk.END, ticket)
        entrada_nombre.delete(0, tk.END)
        entrada_destino.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Complete todos los campos antes de agregar el ticket.")

def limpiar():
    seleccion = lista_tickets.curselection()
    if seleccion:  # Si hay tickets seleccionados
        for i in seleccion[::-1]:
            lista_tickets.delete(i)
    else:  # Si no hay selección, limpiar solo los campos
        entrada_nombre.delete(0, tk.END)
        entrada_destino.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Tickets de Avión")
ventana.geometry("500x350")

# Etiquetas y campos de texto
label_nombre = tk.Label(ventana, text="Nombre del Pasajero:")
label_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=40)
entrada_nombre.pack(pady=5)

label_destino = tk.Label(ventana, text="Destino del Vuelo:")
label_destino.pack(pady=5)
entrada_destino = tk.Entry(ventana, width=40)
entrada_destino.pack(pady=5)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar Ticket", command=agregar_ticket, bg="lightblue")
btn_agregar.pack(pady=5)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, bg="lightcoral")
btn_limpiar.pack(pady=5)

# Lista de tickets
lista_tickets = tk.Listbox(ventana, width=60, height=10)
lista_tickets.pack(pady=10)

# Agregar ticket inicial de ejemplo
lista_tickets.insert(tk.END, "Pasajero: Scarleth | Destino: Miami")

# Iniciar aplicación
ventana.mainloop()

# ============================================
# Aplicación GUI: Lista de Tareas
# Autor: [Tu Nombre]
# Descripción:
#   Aplicación simple con Tkinter para gestionar
#   una lista de tareas. Permite añadir, marcar
#   como completadas y eliminar tareas.
# ============================================

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # -----------------------------
        # Entrada de texto y botones
        # -----------------------------
        self.entry_task = tk.Entry(root, width=30)
        self.entry_task.pack(pady=10)
        self.entry_task.bind("<Return>", self.add_task)  # Evento: Enter añade tarea

        self.btn_add = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.btn_add.pack(pady=5)

        self.btn_complete = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.btn_complete.pack(pady=5)

        self.btn_delete = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.btn_delete.pack(pady=5)

        # -----------------------------
        # Lista de tareas
        # -----------------------------
        self.listbox_tasks = tk.Listbox(root, width=40, height=10)
        self.listbox_tasks.pack(pady=10)

        # Tareas iniciales (ejemplo)
        tareas_iniciales = ["Martes: Inglés a las 3", "Miércoles: Inglés a las 3", "Jueves: Inglés a las 3"]
        for tarea in tareas_iniciales:
            self.listbox_tasks.insert(tk.END, tarea)

        # Permitir doble clic para marcar como completada
        self.listbox_tasks.bind("<Double-Button-1>", self.complete_task)

    # -----------------------------
    # Funciones principales
    # -----------------------------
    def add_task(self, event=None):
        """Añade una nueva tarea a la lista."""
        task = self.entry_task.get().strip()
        if task != "":
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self, event=None):
        """Marca la tarea seleccionada como completada."""
        try:
            index = self.listbox_tasks.curselection()[0]
            task = self.listbox_tasks.get(index)

            # Verificamos si ya está completada
            if not task.startswith("✔ "):
                self.listbox_tasks.delete(index)
                self.listbox_tasks.insert(index, f"✔ {task}")
            else:
                messagebox.showinfo("Info", "Esta tarea ya está completada.")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.delete(index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


# -----------------------------
# Punto de entrada principal
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()



# Agenda Personal

import tkinter as tk
from tkinter import ttk, messagebox

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("650x400")
        self.root.resizable(False, False)

        # Frames
        self.frame_list = ttk.Frame(self.root, padding=(10, 10))
        self.frame_actions = ttk.Frame(self.root, padding=(10, 10))
        self.frame_list.pack(fill=tk.BOTH, expand=True)
        self.frame_actions.pack(fill=tk.X)

        # Configurar lista y acciones
        self._setup_treeview()
        self._setup_actions()

        # Lista de actividades semanales (predefinido)
        eventos_iniciales = [
            ("Lunes", "15:00", "Clases de inglés"),
            ("Martes", "____", "Descanso"),
            ("Miércoles", "15:00", "Clases de inglés"),
            ("Jueves", "15:00", "Clases de inglés"),
            ("Viernes", "____", "Descanso"),
            ("Sábado", "07:30", "Clases de la UEA"),
            ("Domingo", "____", "Descanso")
        ]

        # Insertar eventos iniciales en la tabla
        for i, (dia, hora, desc) in enumerate(eventos_iniciales):
            item_id = f"evento_{i}"
            self.tree.insert("", tk.END, iid=item_id, values=(dia, hora, desc))

    def _setup_treeview(self):
        lbl = ttk.Label(self.frame_list, text="Agenda Semanal", font=("Segoe UI", 12, "bold"))
        lbl.pack(anchor=tk.W, pady=(0, 6))

        columnas = ("dia", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_list, columns=columnas, show="headings", selectmode="browse")
        self.tree.heading("dia", text="Día")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")

        self.tree.column("dia", width=120, anchor=tk.CENTER)
        self.tree.column("hora", width=80, anchor=tk.CENTER)
        self.tree.column("descripcion", width=400, anchor=tk.W)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def _setup_actions(self):
        btn_delete = ttk.Button(self.frame_actions, text="Eliminar Evento Seleccionado",
                                command=self.delete_selected_event)
        btn_exit = ttk.Button(self.frame_actions, text="Salir", command=self.root.quit)

        btn_delete.pack(side=tk.LEFT, padx=6, pady=8)
        btn_exit.pack(side=tk.RIGHT, padx=10, pady=8)

    def delete_selected_event(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Eliminar evento", "Seleccione primero un evento de la lista.")
            return

        item_id = seleccionado[0]
        valores = self.tree.item(item_id, "values")
        dia, hora, descripcion = valores

        confirmar = messagebox.askyesno("Confirmar eliminación",
                                        f"¿Eliminar el evento?\n\nDía: {dia}\nHora: {hora}\nDescripción: {descripcion}")
        if confirmar:
            self.tree.delete(item_id)


def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
i



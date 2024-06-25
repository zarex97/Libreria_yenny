import tkinter as tk
from tkinter import messagebox
from src.ui.styles import apply_styles
from src.models.user import *

class ModificarUsuarioFrame(tk.Frame):
    def __init__(self, parent, show_frame, abm_usuarios_frame, usuario_email):
        super().__init__(parent)
        self.parent = parent
        self.show_frame = show_frame
        self.abm_usuarios_frame = abm_usuarios_frame
        self.usuario_email = usuario_email
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Modificar Usuario", font=("Helvetica", 24, "bold")).pack(pady=20)

        usuario = get_user(self.usuario_email)
        if usuario:
            self.name_entry = self.create_entry("Nombre:", usuario.name)
            self.email_entry = self.create_entry("Email:", usuario.email)

            current_role = self.get_role_name(usuario.role_id)
            roles = ['Admin', 'Empleado', 'Cliente']

            self.role_var = tk.StringVar()
            self.role_var.set(current_role)
            tk.Label(self, text="Rol:", font=("Helvetica", 12)).pack()
            self.role_optionmenu = tk.OptionMenu(self, self.role_var, *roles)
            self.role_optionmenu.pack(pady=5)

            self.premium_var = tk.BooleanVar(value=usuario.is_premium)
            self.premium_checkbox = tk.Checkbutton(self, text="Premium", variable=self.premium_var)
            self.premium_checkbox.pack(pady=10)

            save_button = tk.Button(self, text="Guardar Cambios", font=("Helvetica", 12), command=self.save_changes)
            save_button.pack(pady=10)
        else:
            messagebox.showerror("Error", f"No se encontró ningún usuario con el email {self.usuario_email}")
            self.show_frame(self.abm_usuarios_frame)

        cancel_button = tk.Button(self, text="Cancelar", font=("Helvetica", 12), command=self.cancel)
        cancel_button.pack(pady=10)

    def create_entry(self, label_text, initial_value):
        frame = tk.Frame(self)
        frame.pack(pady=5)
        label = tk.Label(frame, text=label_text, font=("Helvetica", 12))
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
        entry.pack(side=tk.LEFT)
        entry.insert(0, str(initial_value))
        return entry

    def save_changes(self):
        new_name = self.name_entry.get()
        new_email = self.email_entry.get()
        new_role = self.role_var.get()
        new_premium = self.premium_var.get()

        if new_role == 'Admin':
            new_role_id = 1
        elif new_role == 'Empleado':
            new_role_id = 2
        else:
            new_role_id = 3

        if new_name and new_email and new_role in ['Admin', 'Empleado', 'Cliente']:
            update_user(self.usuario_email, new_name, new_email, new_role_id, new_premium)
            self.show_frame(self.abm_usuarios_frame)
            self.abm_usuarios_frame.load_usuarios()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son requeridos")

    def get_role_name(self, role_id):
        if role_id == 1:
            return 'Admin'
        elif role_id == 2:
            return 'Empleado'
        elif role_id == 3:
            return 'Cliente'

    def cancel(self):
        self.show_frame(self.abm_usuarios_frame)

import tkinter as tk
from tkinter import messagebox

from src.auth.auth import hash_password
from src.ui.styles import apply_styles
from src.models.user import *


class AgregarUsuarioFrame(tk.Frame):
    def __init__(self, parent, show_frame, abm_usuarios_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.abm_usuarios_frame = abm_usuarios_frame
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Agregar Usuario", font=("Helvetica", 24, "bold")).pack(pady=20)

        self.name_entry = self.create_entry("Nombre:")
        self.password_entry = self.create_entry("Contraseña:")
        self.email_entry = self.create_entry("Email:")

        self.role_var = tk.StringVar()
        self.role_var.set('Cliente')
        roles = ['Admin', 'Empleado', 'Cliente']
        tk.Label(self, text="Rol:", font=("Helvetica", 12)).pack()
        self.role_optionmenu = tk.OptionMenu(self, self.role_var, *roles)
        self.role_optionmenu.pack(pady=5)

        self.premium_var = tk.BooleanVar(value=False)
        self.premium_checkbox = tk.Checkbutton(self, text="Premium", variable=self.premium_var)
        self.premium_checkbox.pack(pady=10)

        self.accept_button = tk.Button(self, text="Aceptar", font=("Helvetica", 12), command=self.add_user)
        self.accept_button.pack(pady=5)

        self.cancel_button = tk.Button(self, text="Cancelar", font=("Helvetica", 12), command=self.cancel)
        self.cancel_button.pack(pady=5)

    def create_entry(self, label_text):
        frame = tk.Frame(self)
        frame.pack(pady=5)
        tk.Label(frame, text=label_text, font=("Helvetica", 12)).pack(side=tk.LEFT)
        entry = tk.Entry(frame, font=("Helvetica", 12))
        entry.pack(side=tk.LEFT)
        return entry

    def add_user(self):
        name = self.name_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        role = self.role_var.get()
        premium = self.premium_var.get()

        if name and password and email and role in ['Admin', 'Empleado', 'Cliente']:
            if not verify_email(email):
                if role == 'Admin':
                    role_id = 1
                elif role == 'Empleado':
                    role_id = 2
                else:
                    role_id = 3

                hashed_password = hash_password(password)
                set_user(name, hashed_password, email, role_id, premium)
                self.abm_usuarios_frame.load_usuarios()
                self.show_frame(self.abm_usuarios_frame)
            else:
                messagebox.showwarning("Advertencia", "El usuario ya existe")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son requeridos")

    def cancel(self):
        self.show_frame(self.abm_usuarios_frame)

import tkinter as tk
from tkinter import messagebox

from src.ui.styles import apply_styles, RoundedButton
from src.logic.register_logic import register


class RegistroFrame(tk.Frame):
    def __init__(self, parent, show_frame, on_login_success):
        super().__init__(parent)
        self.show_frame = show_frame
        self.on_login_success = on_login_success
        self.create_widgets()
        apply_styles(self)  # Apply styles here

    def create_widgets(self):
        tk.Label(self, text="Registro", font=("Helvetica", 24, "bold")).pack(pady=20)
        tk.Label(self, text="Nombre").pack(pady=5)
        self.registro_nombre = tk.Entry(self)
        self.registro_nombre.pack(pady=5)
        tk.Label(self, text="Mail").pack(pady=5)
        self.registro_email = tk.Entry(self)
        self.registro_email.pack(pady=5)
        tk.Label(self, text="Contraseña").pack(pady=5)
        self.registro_password = tk.Entry(self, show='*')
        self.registro_password.pack(pady=5)
        
        RoundedButton(self, text="Registrar", command=self.register, width=180, height=60, bg='white', fg='#013220').pack(pady=20)
        RoundedButton(self, text="Iniciar Sesion", command=lambda: self.show_frame(self.master.children["!loginframe"]), width=180, height=60, bg='white', fg='#013220').pack(pady=10)

    def register(self):
        name = self.registro_nombre.get()
        email = self.registro_email.get()
        password = self.registro_password.get()

        if '@' not in email:
            messagebox.showinfo("Error al registrarse", "Ingrese un email valido")
            return

        if len(password) < 8:
            messagebox.showinfo("Error al registrarse", "La contraseña debe tener al menos 8 caracteres")
            return

        user = register(name, password, email)

        if user:
            self.on_login_success(user)
            messagebox.showinfo("Registro exitoso", "Te has registrado correctamente")
        else:
            messagebox.showinfo("Error de registro", "El email ya ha sido usado")

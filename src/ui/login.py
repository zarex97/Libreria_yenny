import tkinter as tk
from tkinter import messagebox

from src.ui.styles import apply_styles
from src.logic.login_logic import *


class LoginFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Login", font=("Helvetica", 24, "bold")).pack(pady=20)
        tk.Label(self, text="Mail").pack(pady=5)
        self.login_email = tk.Entry(self)
        self.login_email.pack(pady=5)
        tk.Label(self, text="Contraseña").pack(pady=5)
        self.login_password = tk.Entry(self, show='*')
        self.login_password.pack(pady=5)
        tk.Button(self, text="Login", command=self.handle_login).pack(pady=20)


    def handle_login(self):
        email = self.login_email.get()
        password = self.login_password.get()

        user = login(email, password)

        if user:
            if user.role_id == 3:
                self.show_frame(self.master.children["!productosframe"])
            else:
                self.show_frame(self.master.children["!adminframe"])
        else:
            messagebox.showinfo("Error de login", "Credenciales incorrectas")

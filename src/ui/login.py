import tkinter as tk
from tkinter import messagebox

from src.ui.adminpanel import AdminFrame
from src.ui.pedidos import PedidosFrame
from src.ui.styles import apply_styles
from src.logic.login_logic import *


class LoginFrame(tk.Frame):
    def __init__(self, parent, show_frame, on_login_success):
        super().__init__(parent)
        self.show_frame = show_frame
        self.on_login_success = on_login_success
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
        tk.Button(self, text="Registrarse",
                  command=lambda: self.show_frame(self.master.children["!registroframe"])).pack(pady=10)

    def handle_login(self):
        email = self.login_email.get()
        password = self.login_password.get()

        user = login(email, password)

        if user:
            self.master.user = user
            self.master.pedidos_frame = PedidosFrame(self.master, self.show_frame, user.id, user.role_id)
            self.master.pedidos_frame.grid(row=0, column=0, sticky='nsew', in_=self.master)
            self.master.admin_frame = AdminFrame(self.master, self.show_frame, user.role_id)
            self.master.admin_frame.grid(row=0, column=0, sticky='nsew', in_=self.master)
            self.show_frame(self.master.admin_frame)
        else:
            messagebox.showinfo("Error de login", "Credenciales incorrectas")

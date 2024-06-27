import tkinter as tk
from tkinter import messagebox

from src.ui.adminpanel import AdminFrame
from src.ui.pedidos import PedidosFrame
from src.ui.productos import ProductosFrame
from src.ui.styles import apply_styles, RoundedButton
from src.logic.login_logic import *


class LoginFrame(tk.Frame):
    def __init__(self, parent, show_frame, on_login_success):
        super().__init__(parent)
        self.show_frame = show_frame
        self.on_login_success = on_login_success
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        container = tk.Frame(self, bg='#013220', bd=10, relief='flat')  
        container.pack(pady=20, padx=20)

        tk.Label(container, text="Nombre de usuario", font=("Helvetica", 12, "bold"), bg='#013220', fg='#ffffff').grid(row=0, column=0, pady=5, padx=10)  
        self.login_email = tk.Entry(container, font=("Helvetica", 12), relief='flat', highlightthickness=0)
        self.login_email.grid(row=1, column=0, pady=5, padx=10)

        tk.Label(container, text="Contraseña", font=("Helvetica", 12, "bold"), bg='#013220', fg='#ffffff').grid(row=2, column=0, pady=5, padx=10) 
        self.login_password = tk.Entry(container, show='*', font=("Helvetica", 12), relief='flat', highlightthickness=0)
        self.login_password.grid(row=3, column=0, pady=5, padx=10)

        RoundedButton(container, text="Iniciar Sesion", command=self.handle_login, width=180, height=60, radius=30, bg='white', fg='#013220').grid(row=4, column=0, pady=20, padx=10)  
        RoundedButton(container, text="Registrarse", command=lambda: self.show_frame(self.master.children["!registroframe"]), width=180, height=60, radius=30, bg='white', fg='#013220').grid(row=5, column=0, pady=10, padx=10)  # Botón blanco cremoso

    def handle_login(self):
        email = self.login_email.get()
        password = self.login_password.get()

        user = login(email, password)

        if user:
            self.master.user = user
            self.master.pedidos_frame = PedidosFrame(self.master, self.show_frame, user.id, user.role_id)
            self.master.pedidos_frame.grid(row=0, column=0, sticky='nsew', in_=self.master)
            self.master.productos_frame = ProductosFrame(self.master, self.show_frame, user.id)
            self.master.productos_frame.grid(row=0, column=0, sticky='nsew', in_=self.master)
            self.master.admin_frame = AdminFrame(self.master, self.show_frame, user.role_id)
            self.master.admin_frame.grid(row=0, column=0, sticky='nsew', in_=self.master)
            self.show_frame(self.master.admin_frame)
        else:
            messagebox.showinfo("Error de login", "Credenciales incorrectas")

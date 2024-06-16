import tkinter as tk
from ui.styles import apply_styles

class RegistroFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.create_widgets()
        apply_styles(self)  # Apply styles here

    def create_widgets(self):
        tk.Label(self, text="Registro", font=("Helvetica", 24, "bold")).pack(pady=20)
        tk.Label(self, text="Mail").pack(pady=5)
        self.registro_email = tk.Entry(self)
        self.registro_email.pack(pady=5)
        tk.Label(self, text="Nombre").pack(pady=5)
        self.registro_nombre = tk.Entry(self)
        self.registro_nombre.pack(pady=5)
        tk.Label(self, text="Dirección").pack(pady=5)
        self.registro_direccion = tk.Entry(self)
        self.registro_direccion.pack(pady=5)
        tk.Label(self, text="Contraseña").pack(pady=5)
        self.registro_password = tk.Entry(self, show='*')
        self.registro_password.pack(pady=5)
        tk.Button(self, text="Registrar").pack(pady=20)

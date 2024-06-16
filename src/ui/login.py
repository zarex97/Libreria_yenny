import tkinter as tk
from ui.styles import apply_styles

class LoginFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.create_widgets()
        apply_styles(self)  # Apply styles here

    def create_widgets(self):
        tk.Label(self, text="Login", font=("Helvetica", 24, "bold")).pack(pady=20)
        tk.Label(self, text="Mail").pack(pady=5)
        self.login_email = tk.Entry(self)
        self.login_email.pack(pady=5)
        tk.Label(self, text="Contraseña").pack(pady=5)
        self.login_password = tk.Entry(self, show='*')
        self.login_password.pack(pady=5)
        tk.Button(self, text="Login", command=lambda: self.show_frame(self.master.children["!adminframe"])).pack(pady=20)

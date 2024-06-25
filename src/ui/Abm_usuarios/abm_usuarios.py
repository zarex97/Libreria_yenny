import tkinter as tk
from tkinter import simpledialog, messagebox
from src.ui.Abm_usuarios.agregar_usuario import AgregarUsuarioFrame
from src.ui.Abm_usuarios.modificar_usuario import ModificarUsuarioFrame
from src.ui.styles import apply_styles
from src.models.user import *

class ABMUsuariosFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Administrar Usuarios", font=("Helvetica", 24, "bold")).pack(pady=20)

        self.usuarios_listbox = tk.Listbox(self, font=("Helvetica", 12), height=10)
        self.usuarios_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.load_usuarios()

        self.modify_button = tk.Button(self, text="Modificar", font=("Helvetica", 12), command=self.show_modificar_usuario_frame)
        self.modify_button.pack(pady=5)

        self.delete_button = tk.Button(self, text="Eliminar", font=("Helvetica", 12), command=self.delete_usuario)
        self.delete_button.pack(pady=5)

        self.add_button = tk.Button(self, text="Agregar Usuario", font=("Helvetica", 12), command=self.show_agregar_usuario_frame)
        self.add_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Volver atrás", font=("Helvetica", 12), command=self.back)
        self.back_button.pack(pady=10)

    def load_usuarios(self):
        self.usuarios_listbox.delete(0, tk.END)
        usuarios = get_all_users()
        role_map = {
            1: "Admin",
            2: "Empleado",
            3: "Cliente"
        }

        is_premium_map = {
            0: "No es usuario premium",
            1: "Es usuario premium"
        }
        for usuario in usuarios:
            role_name = role_map.get(usuario.role_id)
            premium_user = is_premium_map.get(usuario.is_premium)
            usuario_text = f"{usuario.id} - {usuario.name} - {usuario.email} - Rol: {role_name} - Premium: {premium_user}"
            self.usuarios_listbox.insert(tk.END, usuario_text)

    def show_modificar_usuario_frame(self):
        selected_usuario_index = self.usuarios_listbox.curselection()
        if selected_usuario_index:
            selected_usuario = self.usuarios_listbox.get(selected_usuario_index)
            usuario_email = selected_usuario.split(" - ")[2]
            modificar_usuario_frame = ModificarUsuarioFrame(self.master, self.show_frame, self, usuario_email)
            modificar_usuario_frame.grid(row=0, column=0, sticky='nsew', in_=self.master)
            self.show_frame(modificar_usuario_frame)
        else:
            messagebox.showinfo("Selección", "Por favor, selecciona un usuario para modificar")

    def delete_usuario(self):
        selected_usuario_index = self.usuarios_listbox.curselection()
        if selected_usuario_index:
            selected_usuario = self.usuarios_listbox.get(selected_usuario_index)
            usuario_id = int(selected_usuario.split(" - ")[0])
            delete_user(usuario_id)
            self.load_usuarios()
        else:
            messagebox.showinfo("Selección", "Por favor, selecciona un usuario para eliminar")

    def show_agregar_usuario_frame(self):
        agregar_usuario_frame = AgregarUsuarioFrame(self.master, self.show_frame, self)
        agregar_usuario_frame.grid(row=0, column=0, sticky='nsew', in_=self.master)
        self.show_frame(agregar_usuario_frame)

    def back(self):
        self.show_frame(self.master.children["!adminframe"])

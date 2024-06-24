import tkinter as tk
from src.ui.styles import apply_styles


class AdminFrame(tk.Frame):
    def __init__(self, parent, show_frame, role_id):
        super().__init__(parent)
        self.show_frame = show_frame
        self.role_id = role_id
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Panel de Administrador", font=("Helvetica", 24, "bold")).pack(pady=20)

        # Only show certain buttons if role_id is not 3 (admin or empleado)
        if self.role_id != 3:
            tk.Button(self, text="Agregar Producto", command=self.show_agregar_frame).pack(pady=10)
            tk.Button(self, text="Eliminar Producto").pack(pady=10)

        tk.Button(self, text="Ver Tienda", command=self.show_productos_frame).pack(pady=10)
        tk.Button(self, text="Ver Pedidos", command=self.show_pedidos_frame).pack(pady=10)

    def show_agregar_frame(self):
        agregar_frame = self.master.children.get("!agregarframe")
        if agregar_frame:
            agregar_frame.tkraise()
        else:
            print("¡Error! El frame '!agregarframe' no está disponible.")

    def show_productos_frame(self):
        productos_frame = self.master.children.get("!productosframe")
        if productos_frame:
            productos_frame.tkraise()
        else:
            print("¡Error! El frame '!productosframe' no está disponible.")

    def show_pedidos_frame(self):
        pedidos_frame = self.master.children.get("!pedidosframe")
        if pedidos_frame:
            pedidos_frame.tkraise()
        else:
            print("¡Error! El frame '!pedidosframe' no está disponible.")

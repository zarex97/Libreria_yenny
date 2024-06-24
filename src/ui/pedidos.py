import tkinter as tk
from src.models.bookOrder import *
from src.ui.styles import apply_styles


class PedidosFrame(tk.Frame):
    def __init__(self, parent, show_frame, user_id, role_id):
        super().__init__(parent)
        self.show_frame = show_frame
        self.user_id = user_id
        self.role_id = role_id
        self.create_widgets()
        apply_styles(self)  # Apply styles here

    def create_widgets(self):
        tk.Label(self, text="Pedidos", font=("Helvetica", 24, "bold")).pack(pady=20)

        self.pedido_listbox = tk.Listbox(self, font=("Helvetica", 12), height=10)
        self.pedido_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        orders = get_order(self.user_id, self.role_id)

        for order in orders:
            order_text = f"Pedido #{order[0]} - Usuario: {order[1]}, Fecha: {order[2]}, Valor: {order[3]}"
            self.pedido_listbox.insert(tk.END, order_text)

        self.back_button = tk.Button(self, text="Volver atrás", font=("Helvetica", 12), command=self.back)
        self.back_button.pack(pady=10)

    def back(self):
        self.show_frame(self.master.children["!adminframe"])

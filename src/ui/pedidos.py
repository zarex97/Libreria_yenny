import tkinter as tk
from src.models.bookOrder import *
from src.ui.styles import apply_styles


class PedidosFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.create_widgets()
        apply_styles(self)  # Apply styles here

    def create_widgets(self):
        tk.Label(self, text="Pedidos", font=("Helvetica", 24, "bold")).pack(pady=20)
        
        # Create a Listbox to display the orders
        self.pedido_listbox = tk.Listbox(self, font=("Helvetica", 12), height=10)
        self.pedido_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        orders = get_order()

        for order in orders:
            order_text = f"Pedido #{order[0]} - Usuario: {order[1]}, Fecha: {order[2]}, Valor: {order[3]}"
            self.pedido_listbox.insert(tk.END, order_text)

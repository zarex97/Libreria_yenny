import tkinter as tk
from tkinter import ttk
from ui.styles import apply_styles

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
        
        # Adding sample data to the Listbox
        pedidos = [
            "Pedido 1 - Nombre: Juan Perez, Dirección: Calle Falsa 123, Mail: juan@example.com",
            "Pedido 2 - Nombre: Ana Gomez, Dirección: Av. Siempre Viva 456, Mail: ana@example.com",
            "Pedido 3 - Nombre: Luis Martinez, Dirección: P. Sherman, 42 Wallaby Way, Mail: luis@example.com"
        ]
        
        for pedido in pedidos:
            self.pedido_listbox.insert(tk.END, pedido)

import tkinter as tk
from tkinter import ttk
from ui.styles import apply_styles

class ProductosFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.create_widgets()
        apply_styles(self)  # Apply styles here

    def create_widgets(self):
        tk.Label(self, text="Productos", font=("Helvetica", 24, "bold")).pack(pady=20)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for i in range(12):
            ttk.Label(scrollable_frame, text="Producto " + str(i)).grid(row=i//3, column=i%3, padx=10, pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        cart_frame = tk.Frame(self)
        cart_frame.pack(side="right", fill="y", padx=10)

        tk.Label(cart_frame, text="Carrito").pack()
        for _ in range(6):
            tk.Entry(cart_frame).pack(pady=2)
        tk.Button(cart_frame, text="Comprar").pack(pady=20)
        tk.Button(cart_frame, text="Ver Pedidos", command=lambda: self.show_frame(self.master.children["!pedidosframe"])).pack(pady=10)

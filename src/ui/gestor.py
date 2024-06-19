import tkinter as tk
from tkinter import messagebox

class GestorFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.products = []
        self.create_widgets()

    def create_widgets(self):
        self.product_frame = tk.Frame(self)
        self.product_frame.pack(fill='both', expand=True)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill='x', pady=10)

        self.add_button = tk.Button(self.button_frame, text="Agregar Producto", command=self.add_product)
        self.add_button.pack(side='left', padx=10)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Producto", command=self.delete_product)
        self.delete_button.pack(side='left', padx=10)

        self.list_label = tk.Label(self.product_frame, text="Lista de Productos", font=("Helvetica", 16, "bold"))
        self.list_label.pack(pady=10)

        self.product_listbox = tk.Listbox(self.product_frame, height=10, width=60)
        self.product_listbox.pack(pady=10)

        self.refresh_product_list()

    def add_product(self):
        self.new_window = tk.Toplevel(self)
        self.new_window.title("Nuevo Producto")

        tk.Label(self.new_window, text="Nombre:").grid(row=0, column=0)
        tk.Label(self.new_window, text="Stock:").grid(row=1, column=0)
        tk.Label(self.new_window, text="Precio:").grid(row=2, column=0)

        self.name_entry = tk.Entry(self.new_window)
        self.stock_entry = tk.Entry(self.new_window)
        self.price_entry = tk.Entry(self.new_window)

        self.name_entry.grid(row=0, column=1)
        self.stock_entry.grid(row=1, column=1)
        self.price_entry.grid(row=2, column=1)

        self.save_button = tk.Button(self.new_window, text="Guardar", command=self.save_product)
        self.save_button.grid(row=3, column=0, columnspan=2)

    def save_product(self):
        name = self.name_entry.get()
        stock = self.stock_entry.get()
        price = self.price_entry.get()

        if not name or not stock or not price:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        try:
            stock = int(stock)
            price = float(price)
        except ValueError:
            messagebox.showwarning("Advertencia", "Stock debe ser un entero y Precio debe ser un número.")
            return

        product = {'name': name, 'stock': stock, 'price': price}
        self.products.append(product)
        self.refresh_product_list()
        self.new_window.destroy()

    def refresh_product_list(self):
        self.product_listbox.delete(0, tk.END)
        for idx, product in enumerate(self.products):
            self.product_listbox.insert(tk.END,
                                        f"{product['name']} - Stock: {product['stock']} - Precio: ${product['price']}")

    def delete_product(self):
        selected_index = self.product_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un producto para eliminar.")
            return

        index = selected_index[0]
        del self.products[index]
        self.refresh_product_list()

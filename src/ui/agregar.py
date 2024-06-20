import tkinter as tk
from tkinter import filedialog
from src.ui.styles import apply_styles

class AgregarFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.create_widgets()
        apply_styles(self)  # Aplicar estilos aquí

    def create_widgets(self):
        tk.Label(self, text="Agregar Producto", font=("Helvetica", 24, "bold")).pack(pady=20)

        tk.Label(self, text="Nombre").pack(pady=5)
        self.product_name_entry = tk.Entry(self)
        self.product_name_entry.pack(pady=5)

        tk.Label(self, text="Foto").pack(pady=5)
        self.product_photo_button = tk.Button(self, text="Cargar Foto", command=self.load_photo)
        self.product_photo_button.pack(pady=5)
        self.product_photo_label = tk.Label(self)
        self.product_photo_label.pack(pady=5)

        tk.Label(self, text="Stock").pack(pady=5)
        self.product_stock_entry = tk.Entry(self)
        self.product_stock_entry.pack(pady=5)

        tk.Button(self, text="Agregar", command=self.add_product).pack(pady=20)

    def load_photo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.product_photo_label.config(text=file_path)

    def add_product(self):
        name = self.product_name_entry.get()
        photo = self.product_photo_label.cget("text")
        stock = self.product_stock_entry.get()

        # Aquí puedes agregar la lógica para guardar el producto en una base de datos o lista

        print(f"Producto agregado: {name}, {photo}, {stock}")

# Ejemplo de cómo usar AgregarFrame en una aplicación Tkinter:
if __name__ == "__main__":
    root = tk.Tk()
    agregar_frame = AgregarFrame(root, None)
    agregar_frame.pack()
    root.mainloop()

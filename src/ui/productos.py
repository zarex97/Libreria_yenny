import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from src.ui.styles import apply_styles
from src.models.book import get_book_author_title
from src.logic.book_logic import get_book_img


class ProductosFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.create_widgets()
        apply_styles(self)

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

        books = get_book_author_title()
        row, col = 0, 0

        self.images = []
        self.labels = []

        for book in books:
            book_title = book['title']
            cover_url = get_book_img(book_title)

            frame = tk.Frame(scrollable_frame, bd=2, relief=tk.SOLID, width=150, height=250)
            frame.grid_propagate(False)
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            img_label = tk.Label(frame)
            img_label.pack()

            title_label = tk.Label(frame, text=book_title, wraplength=100)
            title_label.pack()

            self.labels.append(img_label)

            if cover_url:
                response = requests.get(cover_url)
                img_data = response.content
                img = Image.open(BytesIO(img_data))
                img = img.resize((115, 150), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.images.append(photo)
                img_label.config(image=photo)
            else:
                img = Image.open(os.path.join(os.path.dirname(__file__), '..', 'assets', 'defaultimg.png'))
                default_photo = ImageTk.PhotoImage(img)
                self.images.append(default_photo)
                img_label.config(image=default_photo)

            col += 1
            if col == 4:
                col = 0
                row += 1

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        cart_frame = tk.Frame(self)
        cart_frame.pack(side="right", fill="y", padx=10)

        self.cart_items = []  # Lista para almacenar los items del carrito
        self.total_price = tk.DoubleVar(value=0.0)  # Variable para el precio total

        tk.Label(cart_frame, text="Mi Carrito").pack()

        self.cart_listbox = tk.Listbox(cart_frame, height=6, width=30)
        self.cart_listbox.pack(pady=2)

        self.update_cart()

        tk.Label(cart_frame, textvariable=self.total_price).pack(pady=10)

        tk.Button(cart_frame, text="Comprar", command=self.place_order).pack(pady=20)
        tk.Button(cart_frame, text="Mis Pedidos",
                  command=lambda: self.show_frame(self.master.children["!pedidosframe"])).pack(pady=10)

    def update_cart(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart_items:
            self.cart_listbox.insert(tk.END, f"{item['name']} - ${item['price']:.2f}")
        self.total_price.set(f"Total: ${sum(item['price'] for item in self.cart_items):.2f}")

    def add_to_cart(self, item):
        self.cart_items.append(item)
        self.update_cart()

    def place_order(self):
        print("Orden realizada!")
        self.cart_items = []
        self.update_cart()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    productos_frame = ProductosFrame(root, lambda x: print(x))
    productos_frame.pack(fill="both", expand=True)
    root.mainloop()

ui

import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

from src.ui.styles import apply_styles
from src.models.book import get_book_title, get_all_books
from src.logic.book_logic import get_book_img
from src.models.bookOrder import set_order


class ProductosFrame(tk.Frame):
    def __init__(self, parent, show_frame, user_id):
        super().__init__(parent)
        self.show_frame = show_frame
        self.user_id = user_id
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

        books = get_all_books()
        row, col = 0, 0

        self.images = []
        self.labels = []

        for book in books:
            book_id, title, author, isbn, price, stock, category = book

            if stock > 0:
                cover_url = get_book_img(title)

                frame = tk.Frame(scrollable_frame, bd=2, relief=tk.SOLID, width=150, height=250)
                frame.grid_propagate(False)
                frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

                img_label = tk.Label(frame)
                img_label.pack()

                title_label = tk.Label(frame, text=title, wraplength=100)
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

                    img_label.book_title = title
                    title_label.book_title = title

                    img_label.bind("<Button-1>", self.on_book_click)
                    title_label.bind("<Button-1>", self.on_book_click)

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

        self.cart_items = []
        self.total_price = tk.DoubleVar(value=0.0)

        tk.Label(cart_frame, text="Mi Carrito").pack()

        self.cart_listbox = tk.Listbox(cart_frame, height=6, width=30)
        self.cart_listbox.pack(pady=2)

        self.update_cart()

        tk.Label(cart_frame, textvariable=self.total_price).pack(pady=10)

        tk.Button(cart_frame, text="Comprar", command=self.place_order).pack(pady=20)
        tk.Button(cart_frame, text="Volver atras",
                  command=lambda: self.show_frame(self.master.children["!adminframe"])).pack(pady=10)
        tk.Button(cart_frame, text="Cerrar Sesión", command=self.logout).pack(pady=10)
    def update_cart(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart_items:
            self.cart_listbox.insert(tk.END, f"{item['title']} - Cantidad: {item['quantity']} - ${item['price']:.2f}")
            self.total_price.set(f"Total: ${sum(item['price']*item['quantity'] for item in self.cart_items):.2f} ")

    def on_book_click(self, event):
        img_label = event.widget
        book_title = img_label.book_title
        self.add_to_cart(book_title)

    def add_to_cart(self, book_title):
        book = get_book_title(book_title)
        if book:
            for item in self.cart_items:
                if item['title'] == book[1]:
                    if item['quantity'] < book[5]:
                        item['quantity'] += 1
                        self.update_cart()
                    else:
                        messagebox.showwarning("Stock insuficiente", f"No hay suficientes unidades de {book_title}")
                    return

            item = {
                'title': book[1],
                'price': book[4],
                'quantity': 1
            }
            self.cart_items.append(item)
            self.update_cart()
        else:
            messagebox.showerror("Error", f"No se encontró el libro {book_title} en la base de datos")

    def logout(self):
        # Realiza aquí las acciones necesarias para cerrar sesión,
        # como limpiar variables de sesión o mostrar un mensaje de confirmación.

        # Luego, muestra el frame de inicio de sesión:
        self.show_frame(self.master.children["!loginframe"])
    def place_order(self):
        user_id = self.user_id
        books_data = {}

        for item in self.cart_items:
            book_title = item['title']
            book = get_book_title(book_title)
            if book:
                book_id = book[0]
                books_data[book_id] = {
                    'quantity': item['quantity'],
                    'price': item['price']
                }
            else:
                messagebox.showerror("Error", f"No se encontró el libro {book_title} en la base de datos")
                return

        if books_data:
            set_order(user_id, books_data)
            messagebox.showinfo("Pedido realizado", "Se ha creado el pedido correctamente")
            self.cart_items = []
            self.update_cart()

            if hasattr(self.master, 'pedidos_frame'):
                self.master.pedidos_frame.update_orders()
        else:
            messagebox.showwarning("Carrito vacío", "Agrega libros al carrito antes de realizar la compra")




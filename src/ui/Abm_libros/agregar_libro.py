import tkinter as tk
from tkinter import messagebox
from src.ui.styles import apply_styles
from src.models.book import *

class AgregarLibroFrame(tk.Frame):
    def __init__(self, parent, show_frame, abm_libros_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.abm_libros_frame = abm_libros_frame
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Agregar Libro", font=("Helvetica", 24, "bold")).pack(pady=20)

        self.title_entry = self.create_entry("Título:")
        self.author_entry = self.create_entry("Autor:")
        self.isbn_entry = self.create_entry("ISBN:")
        self.price_entry = self.create_entry("Precio:")
        self.stock_entry = self.create_entry("Stock:")
        self.category_entry = self.create_entry("Categoría:")

        self.accept_button = tk.Button(self, text="Aceptar", font=("Helvetica", 12), command=self.add_book)
        self.accept_button.pack(pady=5)

        self.cancel_button = tk.Button(self, text="Cancelar", font=("Helvetica", 12), command=self.cancel)
        self.cancel_button.pack(pady=5)

    def create_entry(self, label_text):
        frame = tk.Frame(self)
        frame.pack(pady=5)
        tk.Label(frame, text=label_text, font=("Helvetica", 12)).pack(side=tk.LEFT)
        entry = tk.Entry(frame, font=("Helvetica", 12))
        entry.pack(side=tk.LEFT)
        return entry

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        price = self.price_entry.get()
        stock = self.stock_entry.get()
        category = self.category_entry.get()

        if title and author and isbn and price and stock and category:
            if not verify_book(title):
                set_book(title, author, isbn, price, stock, category)
                self.abm_libros_frame.load_books()
                self.show_frame(self.abm_libros_frame)
            else:
                messagebox.showwarning("Advertencia", "El libro ya existe")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son requeridos")

    def cancel(self):
        self.show_frame(self.abm_libros_frame)

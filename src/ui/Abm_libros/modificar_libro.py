import tkinter as tk
from tkinter import simpledialog, messagebox
from src.ui.styles import apply_styles
from src.models.book import get_book, update_book

class ModificarLibroFrame(tk.Frame):
    def __init__(self, parent, show_frame, abm_libros_frame, book_id):
        super().__init__(parent)
        self.parent = parent
        self.show_frame = show_frame
        self.abm_libros_frame = abm_libros_frame
        self.book_id = book_id
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Modificar Libro", font=("Helvetica", 24, "bold")).pack(pady=20)

        book = get_book(self.book_id)
        if book:
            self.title_entry = self.create_entry("Título:", book[1])
            self.author_entry = self.create_entry("Autor:", book[2])
            self.isbn_entry = self.create_entry("ISBN:", book[3])
            self.price_entry = self.create_entry("Precio:", book[4])
            self.stock_entry = self.create_entry("Stock:", book[5])
            self.category_entry = self.create_entry("Categoría:", book[6])

            save_button = tk.Button(self, text="Guardar Cambios", font=("Helvetica", 12), command=self.save_changes)
            save_button.pack(pady=10)
        else:
            messagebox.showerror("Error", f"No se encontró ningún libro con id {self.book_id}")
            self.show_frame(self.abm_libros_frame)

        cancel_button = tk.Button(self, text="Cancelar", font=("Helvetica", 12), command=self.cancel)
        cancel_button.pack(pady=10)

    def create_entry(self, label_text, initial_value):
        frame = tk.Frame(self)
        frame.pack(pady=5)
        label = tk.Label(frame, text=label_text, font=("Helvetica", 12))
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
        entry.pack(side=tk.LEFT)
        entry.insert(0, str(initial_value))
        return entry

    def save_changes(self):
        new_title = self.title_entry.get()
        new_author = self.author_entry.get()
        new_isbn = self.isbn_entry.get()
        new_price = self.price_entry.get()
        new_stock = self.stock_entry.get()
        new_category = self.category_entry.get()

        if new_title and new_author and new_isbn and new_price and new_stock and new_category:
            update_book(self.book_id, new_title, new_author, new_isbn, new_price, new_stock, new_category)
            self.show_frame(self.abm_libros_frame)
            self.abm_libros_frame.load_books()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son requeridos")

    def cancel(self):
        self.show_frame(self.abm_libros_frame)

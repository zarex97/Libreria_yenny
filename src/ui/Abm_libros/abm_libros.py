import tkinter as tk
from tkinter import simpledialog, messagebox

from src.ui.Abm_libros.agregar_libro import AgregarLibroFrame
from src.ui.Abm_libros.modificar_libro import ModificarLibroFrame
from src.ui.styles import apply_styles
from src.models.book import *

class ABMLibrosFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        self.show_frame = show_frame
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Administrar Libros", font=("Helvetica", 24, "bold")).pack(pady=20)

        self.libros_listbox = tk.Listbox(self, font=("Helvetica", 12), height=10)
        self.libros_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.load_books()

        self.modify_button = tk.Button(self, text="Modificar", font=("Helvetica", 12), command=self.show_modificar_libro_frame)
        self.modify_button.pack(pady=5)

        self.delete_button = tk.Button(self, text="Eliminar", font=("Helvetica", 12), command=self.delete_book)
        self.delete_button.pack(pady=5)

        self.add_button = tk.Button(self, text="Agregar Libro", font=("Helvetica", 12), command=self.show_agregar_libro_frame)
        self.add_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Volver atrás", font=("Helvetica", 12), command=self.back)
        self.back_button.pack(pady=10)

    def load_books(self):
        self.libros_listbox.delete(0, tk.END)
        libros = get_all_books()
        for libro in libros:
            libro_text = f"{libro[0]} - Titulo:{libro[1]} - Autor: {libro[2]} - ISBN: {libro[3]} - Precio: {libro[4]} - Stock: {libro[5]} - IDCategoria: {libro[6]}"
            self.libros_listbox.insert(tk.END, libro_text)

    def show_modificar_libro_frame(self):
        selected_book_index = self.libros_listbox.curselection()
        if selected_book_index:
            selected_book = self.libros_listbox.get(selected_book_index)
            book_id = selected_book.split(" - ")[0]
            modificar_libro_frame = ModificarLibroFrame(self.master, self.show_frame, self, book_id)
            modificar_libro_frame.grid(row=0, column=0, sticky='nsew', in_=self.master)
            self.show_frame(modificar_libro_frame)
        else:
            messagebox.showinfo("Selección", "Por favor, selecciona un libro para modificar")

    def delete_book(self):
        selected_book_index = self.libros_listbox.curselection()
        if selected_book_index:
            selected_book = self.libros_listbox.get(selected_book_index)
            book_id = selected_book.split(" - ")[0]
            delete_book(book_id)
            self.load_books()
        else:
            messagebox.showinfo("Selección", "Por favor, selecciona un libro para eliminar")

    def show_agregar_libro_frame(self):
        agregar_libro_frame = AgregarLibroFrame(self.master, self.show_frame, self)
        agregar_libro_frame.grid(row=0, column=0, sticky='nsew', in_=self.master)
        self.show_frame(agregar_libro_frame)

    def back(self):
        self.show_frame(self.master.children["!adminframe"])

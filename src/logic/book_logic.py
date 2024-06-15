from src.models.book import *


def add_book(title, author, isbn, price, stock, category):
    if not verify_book():
        set_book(title, author, isbn, price, stock, category)
        print("Se añadio el libro correctamente")
    else:
        print("El libro ya existe")
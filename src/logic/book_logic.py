import requests

from src.models.book import *


def add_book(title, author, isbn, price, stock, category):
    if not verify_book():
        set_book(title, author, isbn, price, stock, category)
        print("Se añadio el libro correctamente")
    else:
        print("El libro ya existe")


def get_book_img(book_title):
    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}"
    response = requests.get(url)
    data = response.json()

    if 'items' in data and len(data['items']) > 0:
        volume_info = data['items'][0]['volumeInfo']
        if 'imageLinks' in volume_info:
            return volume_info['imageLinks'].get('thumbnail')

    return None
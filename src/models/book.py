import sqlite3
import os


class Book:
    def __init__(self, title, author, isbn, price, stock, category):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.stock = stock
        self.category = category


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'db', 'Library.db')


def get_book(title):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('SELECT * FROM book WHERE title = ?', (title,))
    book = cursor.fetchone()
    dbconn.close()
    return book


def set_book(title, author, isbn, price, stock, category):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('''
    INSERT INTO book (title, author, isbn, price, stock, category)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, author, isbn, price, stock, category))
    dbconn.commit()
    dbconn.close()


def delete_book(title):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('DELETE FROM book WHERE title = ?', (title,))
    dbconn.commit()
    dbconn.close()


def verify_book(title):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('SELECT EXISTS(SELECT 1 FROM book WHERE title = ?)', (title,))
    exists = cursor.fetchone()[0] == 1
    dbconn.close()
    return exists


def get_book_author_title():
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('SELECT title, author FROM book')
    books = [{'title': title, 'author': author} for title, author in cursor.fetchall()]
    dbconn.close()
    return books
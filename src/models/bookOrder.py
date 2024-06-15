import sqlite3
import os


class BookOrder:
    def __init__(self, user_id, date, value):
        self.user_id = user_id
        self.date = date
        self.value = value


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'db', 'Library.db')


def set_order(user_id, books_data):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()

    total_value = sum(books['price'] * books['quantity'] for books in books_data.values())

    cursor.execute('''
    INSERT INTO BookOrder (user_id, date, value)
    VALUES (?, DATETIME('now'), ?)
    ''', (user_id, total_value))

    order_id = cursor.lastrowid

    for book_id, book in books_data.items():
        cursor.execute('''
        INSERT INTO OrderDetail (order_id, book_id, quantity, book_price)
        VALUES (?, ?, ?, ?)
        ''', (order_id, book_id, book['quantity'], book['price']))

        cursor.execute('''
        UPDATE Book
        SET stock = stock - ?
        WHERE id = ?
        ''', (book['quantity'], book_id))

    dbconn.commit()
    dbconn.close()



#user_id = 1
#
#books_data = {
#    1: {'quantity': 2, 'price': 19.99},
#    2: {'quantity': 1, 'price': 29.99}
#}

#set_order(user_id, books_data)

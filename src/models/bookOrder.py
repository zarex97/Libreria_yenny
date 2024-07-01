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

    return order_id


def get_order(user_id, role_id):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    if role_id == 3:
        cursor.execute('''
        SELECT o.id, u.name, o.date, o.value
        FROM BookOrder o
        INNER JOIN user u ON o.user_id = u.id
        WHERE u.id = ?
        ORDER BY o.date DESC
        ''', (user_id,))
    else:
        cursor.execute('''
        SELECT o.id, u.name, o.date, o.value
        FROM BookOrder o
        INNER JOIN user u ON o.user_id = u.id
        ORDER BY o.date DESC
        ''')
    orders = cursor.fetchall()
    dbconn.close()
    return orders


def get_order_details(order_id):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('''
        SELECT Book.title, OrderDetail.quantity, OrderDetail.book_price
        FROM OrderDetail
        JOIN Book ON OrderDetail.book_id = Book.id
        WHERE OrderDetail.order_id = ?
    ''', (order_id,))
    order_details = cursor.fetchall()
    dbconn.close()
    return order_details



def delete_order(order_id):
    try:
        dbconn = sqlite3.connect(DB_PATH)
        cursor = dbconn.cursor()

        cursor.execute('''
        DELETE FROM OrderDetail
        WHERE order_id = ?
        ''', (order_id,))

        cursor.execute('''
        DELETE FROM BookOrder
        WHERE id = ?
        ''', (order_id,))

        dbconn.commit()
        dbconn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error al eliminar el pedido #{order_id}: {e}")
        return False
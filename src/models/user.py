import sqlite3
import os


class User:

    def __init__(self, id, name, password, email, role_id):
        self.id = id
        self.name = name
        self.password = password
        self.email = email
        self.role_id = role_id


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'db', 'Library.db')


def get_user(username):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('SELECT * FROM user WHERE name = ?', (username,))
    user_data = cursor.fetchone()
    dbconn.close()
    return user_data


def set_user(username, password, email):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('''
    INSERT INTO user (name, password, email, role_id)
    VALUES (?, ?, ?, ?)
    ''', (username, password, email, 3))
    dbconn.commit()
    dbconn.close()


def verify_email(email):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('SELECT EXISTS(SELECT 1 FROM user WHERE email = ?)', (email,))
    exists = cursor.fetchone()[0] == 1  # Verifica si el resultado es 1
    dbconn.close()
    return exists


def delete_user(user_id):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('DELETE FROM user WHERE id = ?', (user_id,))
    dbconn.commit()
    dbconn.close()
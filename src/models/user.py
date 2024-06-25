import sqlite3
import os


class User:

    def __init__(self, id, name, password, email, role_id, is_premium):
        self.id = id
        self.name = name
        self.password = password
        self.email = email
        self.role_id = role_id
        self.is_premium = is_premium


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'db', 'Library.db')


def get_all_users():
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('SELECT * FROM User')
    user_data = cursor.fetchall()
    dbconn.close()

    users = []
    for data in user_data:
        user = User(*data)
        users.append(user)

    return users


def get_user(email):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('SELECT * FROM user WHERE email = ?', (email,))
    user_data = cursor.fetchone()
    dbconn.close()
    if user_data:
        return User(*user_data)
    return None


def set_user(name, password, email, role_id=3, is_premium=False):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('''
    INSERT INTO user (name, password, email, role_id, premium)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, password, email, role_id, is_premium))
    dbconn.commit()
    dbconn.close()


def update_user(user_email, name, email, role_id, is_premium):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('''
    UPDATE user
    SET name = ?, email = ?, role_id = ?, premium = ?
    WHERE email = ?
    ''', (name, email, role_id, is_premium, user_email))
    dbconn.commit()
    dbconn.close()


def verify_email(email):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('SELECT EXISTS(SELECT 1 FROM user WHERE email = ?)', (email,))
    exists = cursor.fetchone()[0] == 1
    dbconn.close()
    return exists


def delete_user(user_id):
    dbconn = sqlite3.connect(DB_PATH)
    cursor = dbconn.cursor()
    cursor.execute('DELETE FROM user WHERE id = ?', (user_id,))
    dbconn.commit()
    dbconn.close()
import sqlite3


def dbsetup():
    dbcon = sqlite3.connect('Library.db')
    cursor = dbcon.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Role(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS User(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    role_id INTEGER,
    premium BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (role_id) REFERENCES Role (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Category(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT NOT NULL,
    price DECIMAL NOT NULL,
    stock INTEGER NOT NULL,
    category INTEGER,
    FOREIGN KEY (category) REFERENCES Category(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BookOrder(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date DATE NOT NULL,
    value DECIMAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS OrderDetail(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    book_id INTEGER,
    quantity INTEGER NOT NULL,
    book_price DECIMAL NOT NULL,
    FOREIGN KEY (book_id) REFERENCES Book (id),
    FOREIGN KEY (order_id) REFERENCES BookOrder (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES User (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CartDetail(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER,
    book_id INTEGER,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (book_id) REFERENCES Book (id),
    FOREIGN KEY (cart_id) REFERENCES Cart (id)
    )
    ''')

    cursor.execute('''
    INSERT INTO Role (name)
    VALUES ('admin'), ('empleado'), ('cliente')
    ''')

    categories = [
        ('Fantasía', 'Libros de fantasía'),
        ('Ciencia Ficción', 'Libros de ciencia ficción'),
        ('Realismo Mágico', 'Libros de realismo mágico'),
        ('Distopía', 'Libros de distopía'),
        ('Ciencia', 'Libros de ciencia'),
        ('Aventura', 'Libros de aventura'),
        ('Ciberpunk', 'Libros de ciberpunk'),
        ('Misterio', 'Libros de misterio'),
        ('Policial', 'Libros policiales'),
        ('Romance', 'Libros de romance'),
        ('Historia', 'Libros de historia'),
        ('Biografía', 'Libros de biografías'),
        ('Terror', 'Libros de terror')
    ]

    books = [
        ('El Camino de los Reyes', 'Brandon Sanderson', '9780765326355', 29.99, 15, 1),
        ('Palabras Radiantes', 'Brandon Sanderson', '9780765326362', 32.99, 10, 1),
        ('Juramentada', 'Brandon Sanderson', '9780765326379', 34.99, 12, 1),
        ('El Héroe de las Eras', 'Brandon Sanderson', '9780765316899', 27.99, 8, 1),
        ('Elantris', 'Brandon Sanderson', '9780765350374', 22.99, 20, 1),
        ('El Hobbit', 'J.R.R. Tolkien', '9780345339683', 14.99, 25, 1),
        ('La Comunidad del Anillo', 'J.R.R. Tolkien', '9780547928210', 15.99, 18, 1),
        ('Las Dos Torres', 'J.R.R. Tolkien', '9780547928203', 15.99, 18, 1),
        ('El Retorno del Rey', 'J.R.R. Tolkien', '9780547928197', 15.99, 18, 1),
        ('El Silmarillion', 'J.R.R. Tolkien', '9780618126989', 16.99, 14, 1),
        ('Cien Años de Soledad', 'Gabriel García Márquez', '9780060883287', 13.99, 30, 3),
        ('Crónica de una Muerte Anunciada', 'Gabriel García Márquez', '9781400034956', 12.99, 22, 3),
        ('1984', 'George Orwell', '9780451524935', 9.99, 35, 4),
        ('Rebelión en la Granja', 'George Orwell', '9780451526342', 8.99, 40, 4),
        ('Fundación', 'Isaac Asimov', '9780553293357', 7.99, 28, 2),
        ('Fundación e Imperio', 'Isaac Asimov', '9780553293371', 7.99, 28, 2),
        ('Segunda Fundación', 'Isaac Asimov', '9780553293364', 7.99, 28, 2),
        ('Dune', 'Frank Herbert', '9780441013593', 10.99, 33, 2),
        ('El Juego de Ender', 'Orson Scott Card', '9780812550702', 8.99, 37, 2),
        ('Neuromante', 'William Gibson', '9780441569595', 8.99, 29, 7)
    ]

    cursor.execute('''
    INSERT INTO User (name, password, email, role_id)
    VALUES 
        ('Admin', 'admin', 'admin@example.com', (SELECT id FROM Role WHERE name='admin')),
        ('Empleado', 'empleado', 'empleado@example.com', (SELECT id FROM Role WHERE name='empleado')),
        ('Cliente', 'cliente', 'cliente@example.com', (SELECT id FROM Role WHERE name='cliente'))
    ''')

    cursor.executemany('''
    INSERT INTO Category (name, description)
    VALUES (?, ?)
    ''', categories)

    cursor.executemany('''
    INSERT INTO Book (title, author, isbn, price, stock, category)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', books)

    dbcon.commit()
    dbcon.close()


if __name__ == "__main__":
    dbsetup()


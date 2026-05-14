# data access object
# basically all the sql stuff goes in here so the server file doesnt get messy
# i went with sqlite3 instead of mysql cos you dont need wamp or anything running
# got the idea from lab 06.2 but changed it to sqlite
# https://docs.python.org/3/library/sqlite3.html

import sqlite3
 
DATABASE = 'books.db'
 
def get_connection():
    # just connects to the db file, sqlite makes the file if its not there already
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # without this you just get tuples back which is annoying
    return conn
 
def init_db():
    # makes the table if its not already there
    # i run this when the server starts so i dont have to remember to set it up manually
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
 
def getAll():
    # gets every book in the table
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM book')
    results = cursor.fetchall()
    # have to turn each row into a dict or flask cant turn it into json
    books = []
    for row in results:
        books.append(dict(row))
    conn.close()
    return books
 
def findByID(id):
    # gets just one book by its id
    # the ? is a placeholder so you dont get sql injection (learned this in the labs)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return dict(result)
    else:
        return None  # if theres no book with that id
 
def create(book):
    # sticks a new book into the table
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO book (title, author, price) VALUES (?, ?, ?)',
                   (book['title'], book['author'], book['price']))
    conn.commit()
    # lastrowid gives back the id that was auto generated
    newid = cursor.lastrowid
    conn.close()
    book['id'] = newid
    return book
 
def update(id, book):
    # changes the book info for whatever id you give it
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE book SET title = ?, author = ?, price = ? WHERE id = ?',
                   (book['title'], book['author'], book['price'], id))
    conn.commit()
    conn.close()
    book['id'] = id
    return book
 
def delete(id):
    # gets rid of the book with that id
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM book WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return True
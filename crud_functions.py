import sqlite3

def initiate_db():
    with sqlite3.connect('not_telegram.db') as db:
        cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
     id integer PRIMARY KEY,
     title text NOT NULL,
     description text ,
     price integer NOT NULL);
     """)

    for i in range(1, 5):
        cursor.execute("SELECT * FROM Products WHERE title = ?", (f'Продукт {i}',))
        product = cursor.fetchone()

        if product is None:
            cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                           (f'Продукт {i}', f'Описание {i}', i * 100))

    db.commit()

def get_all_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products


import sqlite3

# Створюємо базу даних game_store.db з таблицею games
conn = sqlite3.connect('GameStore.db')
cursor = conn.cursor()

# Створюємо таблицю
cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        rating REAL,
        genres TEXT,
        platforms TEXT,
        stores TEXT,
        image TEXT,
        price REAL
    )
''')

# Тепер замість print(name) можна робити:
# cursor.execute("INSERT INTO games (title, rating, genres) VALUES (?, ?, ?)", (name, rating, genres))
# conn.commit()
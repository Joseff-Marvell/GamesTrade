import sqlite3

def normalize(field):
    conn = sqlite3.connect('GameStore.db')
    cursor = conn.cursor()

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {field} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """
    cursor.execute(create_table_query)

    # 3. Вибираємо всі записи з таблиці games
    cursor.execute(f"SELECT {field} FROM games")
    rows = cursor.fetchall()

    # 4. Збираємо унікальні назви у множину
    unique_items = set()
    for row in rows:
        if row[0]:  # Перевірка, чи поле не порожнє
            # Розділяємо по комі, прибираємо пробіли по краях
            names = [p.strip() for p in row[0].split(',')]
            unique_items.update(names)

    for item in unique_items:
        if item:
            # Використовуємо INSERT OR IGNORE, щоб не виникало помилок при повторному запуску
            cursor.execute(f"INSERT OR IGNORE INTO {field} (name) VALUES (?)", (item,))

    conn.commit()
    conn.close()
    print(f"Дані із стовпчика {field} успішно перенесено в таблицю '{field}'!")

normalize('genres')
normalize('platforms')
normalize('stores')

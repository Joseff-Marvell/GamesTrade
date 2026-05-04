import sqlite3

def cr_relations3(assoc_table):
    conn = sqlite3.connect("../GameStore3.db")
    cursor = conn.cursor()
    cr_relations_query = f"""
        -- 1. Вимикаємо дію зовнішніх ключів на час перебудови
        PRAGMA foreign_keys = OFF;
        BEGIN TRANSACTION;
            -- Крок А: Перейменуємо існуючу асоціативну таблицю
            ALTER TABLE games_{assoc_table} RENAME TO games_{assoc_table}_old;
            -- Крок Б: Створюємо нову асоціативну таблицю зі зв'язками
            CREATE TABLE games_{assoc_table} (
                games_id INTEGER,
                {assoc_table}_id INTEGER,
                PRIMARY KEY (games_id, {assoc_table}_id),
                FOREIGN KEY (games_id) REFERENCES games (id) ON DELETE CASCADE,
                FOREIGN KEY ({assoc_table}_id) REFERENCES {assoc_table} (id) ON DELETE CASCADE
            );
        
            -- Крок В: Переносимо дані зі старої в нову
            INSERT INTO games_{assoc_table} (games_id, {assoc_table}_id)
            SELECT games_id, {assoc_table}_id FROM games_{assoc_table}_old;
        
            -- Крок Г: Видаляємо стару асоціативну таблицю
            DROP TABLE games_{assoc_table}_old;
    
        COMMIT;
    
        -- 2. Вмикаємо дію зовнішніх ключів
        PRAGMA foreign_keys = ON;
    """
    cursor.executescript(cr_relations_query)
    conn.commit()
    conn.close()
    print(f"Асоціативна таблиця {assoc_table} успішно доповнена відношеннями.")

cr_relations3("genres")
cr_relations3("platforms")
cr_relations3("stores")

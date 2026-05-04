import sqlite3
def normalize3(assoc_table):
    conn = sqlite3.connect("../GameStore3.db")
    cursor = conn.cursor()

    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS games_{assoc_table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            games_id INTEGER,
            {assoc_table}_id INTEGER
        );
        """
    cursor.execute(create_table_query)

    normalize_nxn_query = f"""
        INSERT INTO games_{assoc_table} (games_id, {assoc_table}_id)
        WITH RECURSIVE split(id, name, rest) AS (
          SELECT id, '', {assoc_table} || ',' FROM games UNION ALL
            -- Рекурсія: відділяємо перше слово до коми
            SELECT id,
                trim(substr(rest, 1, instr(rest, ',') - 1)),
                substr(rest, instr(rest, ',') + 1)
            FROM split
            WHERE rest <> ''
        )
        SELECT DISTINCT split.id, {assoc_table}.id
        FROM split
        JOIN {assoc_table} ON split.name = {assoc_table}.name
        WHERE split.name <> '';
        """
    cursor.execute(normalize_nxn_query)
    del_column_query = f"ALTER TABLE games DROP COLUMN {assoc_table}"
    cursor.execute(del_column_query)
    conn.commit()
    conn.close()
    print(f"Нормалізація до 3 форми відношення таблиць games та {assoc_table} завершена успішно!")

normalize3("genres")
normalize3("platforms")
normalize3("stores")

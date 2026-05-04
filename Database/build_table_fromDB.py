import sqlite3

conn = sqlite3.connect('../GameStore3.db')
cursor = conn.cursor()
query = f"""
    SELECT g.title, g.rating, gn.name, p.name, s.name
    FROM games g
    JOIN games_genres gg ON g.id = gg.games_id
    JOIN genres gn ON gg.genres_id = gn.id
    JOIN games_platforms gp ON g.id = gp.games_id
    JOIN platforms p ON gp.platforms_id = p.id 
    JOIN games_stores gs ON g.id = gs.games_id
    JOIN stores s ON gs.stores_id = s.id 
    ORDER BY g.title;
"""
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

import streamlit as st
import requests
import sqlite3

API_KEY = st.secrets["RAWG"]["API_KEY"]

# Адреса API (шукаємо найпопулярніші ігри)
url = f"https://api.rawg.io/api/games?key={API_KEY}&ordering=-added&page_size=10"

# try:
response = requests.get(url)
response.raise_for_status()  # Перевірка на помилки
data = response.json()

conn = sqlite3.connect('GameStore.db')
cursor = conn.cursor()

for game in data['results']:
    name = game['name']
    rating = game['rating']
    genres = ", ".join([g['name'] for g in game['genres']])
    platforms = ", ".join([g['platform']['name'] for g in game['parent_platforms']])
    stores = ", ".join([g['store']['name'] for g in game['stores']])
    image = game['background_image']

    cursor.execute("INSERT INTO games (title, rating, image, genres, platforms, stores) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, rating, image, genres, platforms, stores))
    conn.commit()
conn.close()
print("Базу даних успішно наповнено.")
# except Exception as e:
#     print(f"Помилка при отриманні даних: {e}")


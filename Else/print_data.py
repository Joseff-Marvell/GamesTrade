import streamlit as st
import requests
from prettytable import PrettyTable

# API_KEY = "e8637272cf7b4b76b0e6f36a1836de4f"
# url = f"https://api.rawg.io/api/games?key={API_KEY}&ordering=-added&page_size=10"
API_KEY = st.secrets['RAWG']['API_KEY']
url = f"https://api.rawg.io/api/games?key={API_KEY}&ordering=-added&page_size=10"

response = requests.get(url)

data = response.json()
response.raise_for_status()
results = data['results']

# import json
# json_string = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
# print(json_string)

banner = True
try:
    table = PrettyTable()
    table.field_names = ["Назва гри", "Рейтинг", "Жанри", "Платформи", "Магазини"]      #, "Банер"]

    for game in results:
        name = game['name']
        rating = game['rating']
        genres = ", ".join([g['name'] for g in game['genres']])
        parent_platforms = ", ".join([g['platform']['name'] for g in game['parent_platforms']])
        stores = ", ".join([g['store']['name'] for g in game['stores']])
        background_image = game['background_image']

        # Створюємо рядки таблиці
        row = [name, rating, genres, parent_platforms, stores]      #, background_image]
        table.add_row(row)
except Exception as e:
    print(f"Помилка при отриманні даних: {e}")

# Текст в клітинках вирівнюємо вліво
table.align = "l"
print(table)

import streamlit as st

# 1. Налаштування сторінки
st.set_page_config(page_title="My Game Store", page_icon="🎮", layout="wide")

st.title("🚀 Super Indie Game Store")
st.markdown("---")

# 2. Наша локальна база даних (поки API не працює)
games = [
    {
        "title": "The Witcher 3: Wild Hunt",
        "genre": "RPG",
        "price": "599 грн",
        "img": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/292030/header.jpg",
        "desc": "Легендарна пригода Геральта з Рівії."
    },
    {
        "title": "Cyberpunk 2077",
        "genre": "Action",
        "price": "899 грн",
        "img": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1091500/header.jpg",
        "desc": "Майбутнє вже тут, і воно небезпечне."
    },
    {
        "title": "Elden Ring",
        "genre": "RPG",
        "price": "1200 грн",
        "img": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1245620/header.jpg",
        "desc": "Відкрийте таємниці Міжзем'я."
    },
    {
        "title": "Stray",
        "genre": "Adventure",
        "price": "450 грн",
        "img": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1332010/header.jpg",
        "desc": "Пригоди рудого кота у місті роботів."
    },
    {
        "title": "Civilization VI",
        "price": "525 грн",
        "genre": "Strategy",
        "img": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/289070/header.jpg",
        "desc": ""
    }
]

# 3. Створення сітки (Columns) для відображення карток
cols = st.columns(2)  # Розділимо екран на 2 колонки

for i, game in enumerate(games):
    # Визначаємо, в яку колонку ставити гру (0 або 1)
    col = cols[i % 2]

    with col:
        with st.container(border=True):  # Красива рамка навколо гри
            st.image(game["img"], width='stretch')
            st.subheader(game["title"])
            st.write(game["desc"])

            # Рядок з ціною та кнопкою
            c1, c2 = st.columns([1, 1])
            with c1:
                st.info(f"💰 {game['price']}")
            with c2:
                if st.button(f"Купити {i}", key=f"btn_{i}"):
                    st.toast(f"✅ {game['title']} додано до кошика!")

# 2. Налаштування Sidebar (Бічна панель)
st.sidebar.header("🔍 Фільтри")
# Відобразимо лише ті жанри, які є в базі
unique_genres = ["Всі"] + sorted(list(set(g["genre"] for g in games)))
selected_genre = st.sidebar.selectbox("Оберіть жанр:", unique_genres)

search_query = st.sidebar.text_input("Пошук за назвою:").lower()

# 3. Логіка фільтрації
# Створюємо новий список, куди потраплять лише ігри, що пройшли фільтр
filtered_games = [
    g for g in games
    if (selected_genre == "Всі" or g["genre"] == selected_genre) and
       (search_query in g["title"].lower())
]

# 4. Відображення результатів
st.title(f"🎮 Магазин ігор: {selected_genre}")
st.write(f"Знайдено ігор: {len(filtered_games)}")
st.markdown("---")

if not filtered_games:
    st.warning("На жаль, за вашим запитом нічого не знайдено.")
else:
    cols = st.columns(3)  # Тепер 3 колонки для кращого вигляду
    for i, game in enumerate(filtered_games):
        col = cols[i % 3]
        with col:
            with st.container(border=True):
                st.image(game["img"], use_container_width=True)
                st.subheader(game["title"])

                # Відображення жанру як "бейдж"
                st.caption(f"🏷️ Жанр: {game['genre']}")

                c1, c2 = st.columns([1, 1])
                with c1:
                    st.info(f"**{game['price']}**")
                with c2:
                    if st.button("Купити", key=f"btn_{game['title']}"):
                        st.balloons()  # Веселий ефект при покупці
                        st.success("Додано!")
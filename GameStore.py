import streamlit as st
import sqlite3

conn = sqlite3.connect('GameStore3.db')
cursor = conn.cursor()

QueryDB = """
    SELECT 
        g.title, 
        g.rating, 
        g.image, 
        g.price, 
        g.desc,
        REPLACE(GROUP_CONCAT(DISTINCT n.name), ',', ', ') AS genres,
        REPLACE(GROUP_CONCAT(DISTINCT p.name), ',', ', ') AS platforms,
        REPLACE(GROUP_CONCAT(DISTINCT s.name), ',', ', ') AS stores
    FROM games g
    LEFT JOIN games_genres gg    ON g.id = gg.games_id
    LEFT JOIN genres n           ON n.id = gg.genres_id
    LEFT JOIN games_platforms gp ON g.id = gp.games_id
    LEFT JOIN platforms p        ON p.id = gp.platforms_id
    LEFT JOIN games_stores gs    ON g.id = gs.games_id
    LEFT JOIN stores s           ON s.id = gs.stores_id
    GROUP BY g.id;
"""
cursor.execute(QueryDB)

games = cursor.fetchall()

# 1. Налаштування сторінки
st.set_page_config(layout="wide")
st.markdown("""<h1 style="text-align: center; color: blue; font-family: 
    'Times New Roman', Times, serif;font-size:60px;">🚀 Game Store</h1>""",
    unsafe_allow_html=True)
# st.header("🚀 :blue[Game Store]", divider="green")
ntails = 2
with st.expander("Параметри"):
    ntails = st.number_input("Кількість вертикальних смуг", value=ntails)
cols = st.columns(ntails)

i = 0
for game in games:
    name = game[0]
    rating = game[1]
    image = game[2]
    price = game[3]
    desc = game[4]
    genres = game[5]
    platforms = game[6]
    stores = game[7]

    col = cols[i % ntails]
    with col:
        with st.container(border=True, height=750):
            # st.divider()
            st.subheader(name)
            st.image(image, width='stretch')
            st.write(desc)
            st.write("Рейтинг: " + "{:.2f}".format(rating),
                     '&nbsp;' * 5 + "Ціна: " +
                     "{:.2f}".format(price) + " грн.")
            st.write("Жанри: " + genres)
            st.write("Платформи: " + platforms)
            st.write('Інтернет-магазини: ' + stores)
    i = i + 1
conn.close()



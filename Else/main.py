import streamlit as st

st.header("Привіт!")

password = st.text_input("Пароль: ", type="password")
st.write("Пароль: ", password)

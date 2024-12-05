import streamlit as st

st.title("Aplikasi Streamlit Pertama")
st.header("Selamat datang!")
st.write("Ini adalah aplikasi sederhana menggunakan Streamlit.")

# Input teks
name = st.text_input("Masukkan nama Anda:")
if st.button("Submit"):
    st.write(f"Hallo, {name}!")

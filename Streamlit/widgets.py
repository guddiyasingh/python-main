import streamlit as st

st.title("Streamlit Text Input ")

name = st.text_input("Enter your name:")

age = st.slider("Enter your age:", 0, 150, 25)

if name:
    st.write(f"Hello, {name}")
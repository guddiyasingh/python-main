import streamlit as st

st.title("Streamlit Text Input ")

name = st.text_input("Enter your name:")

age = st.text_input("Enter your age:")

if name:
    st.write(f"Hello, {name}")
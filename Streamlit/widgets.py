import streamlit as st

st.title("Streamlit Text Input ")

name = st.text_input("Enter your name:")

age = st.slider("Enter your age:", 0, 150, 25)
st.write(f"Your age is: {age}.")

options = ["python", "java", "c++", "javascript"]
choice = st.selectbox("Choose your favorite programming language:",options)
st.write(f"you selected {choice}.")
if name:
    st.write(f"Hello, {name}")
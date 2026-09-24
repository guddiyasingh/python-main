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


data = {

    "Name": ["jhon", "jane", "jake", "jill"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is note None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
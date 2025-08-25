import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")


age=st.slider("Select your age:",0,100,20)
st.write(f"Your age is {age}.")


options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")


if name:
    st.write(f"Hello, {name}")


data = {
    "Name": ["Chandan", "Ravi", "Prem", "Dharmendra"],
    "Age": [20, 21, 19, 22],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}


df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)


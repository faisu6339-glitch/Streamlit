import streamlit as st

st.title("🚀 My First Streamlit App")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello {name}! Welcome to Streamlit 😄")



import streamlit as st

st.title("📊 Dashboard Page")

age = st.number_input("Enter your age")
salary = st.number_input("Enter your salary")

if st.button("Show"):
    st.write("Age:", age)
    st.write("Salary:", salary)
    st.success("Data displayed successfully!")
import streamlit as st

st.title("Sidebar Example")
st.title("This is the main title of the app")

st.sidebar.title("Sidebar Title")
st.sidebar.header("Sidebar Header")

#Text input

name=st.sidebar.text_input("Enter your name:")
st.sidebar.write(f"Hello, {name}!")

#Number input
num=st.sidebar.number_input("Enter a number:", min_value=0, max_value=100, value=50)
st.sidebar.write(f"You entered: {num}")

#Slider
age=st.sidebar.slider("Select your age:", min_value=0, max_value=120, value=25)
st.sidebar.write(f"Your age is: {age}")

#Checkbox
subscribe=st.sidebar.checkbox("Subscribe to newsletter")
if subscribe:
    st.sidebar.write("Thank you for subscribing!")
else:
    st.sidebar.write("You are not subscribed.")

#Selectbox
course=st.sidebar.selectbox(
    "Choose a course:",
    ["Data Science", "Web Development", "Machine Learning", "Cloud Computing"]
)
st.sidebar.write(f"You selected: {course}")


#Multiselect
languages=st.sidebar.multiselect(
    "Select programming languages you know:",
    ["Python", "JavaScript", "Java", "C++", "Ruby", "Go"]
)
st.sidebar.write(f"You know: {', '.join(languages)}")

#Radio buttons
gender=st.sidebar.radio(
    "Select your gender:",
    ["Male", "Female", "Other"]
)
st.sidebar.write(f"You selected: {gender}")

#Date input
date=st.sidebar.date_input("Select a date:")
st.sidebar.write(f"You selected: {date}")

#Time input
time=st.sidebar.time_input("Select a time:")
st.sidebar.write(f"You selected: {time}")


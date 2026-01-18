import streamlit as st

st.set_page_config(page_title="Sidebar Navbar", layout="wide")

st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio(
    "Go to",
    ["Home", "Dashboard", "Profile", "Settings", "Logout"]
)

st.title("📊 My Application")

if menu == "Home":
    st.header("🏠 Home")
    st.write("Welcome to the Home page")

elif menu == "Dashboard":
    st.header("📈 Dashboard")
    st.write("This is your dashboard")

elif menu == "Profile":
    st.header("👤 Profile")
    st.write("User profile information")

elif menu == "Settings":
    st.header("⚙️ Settings")
    st.write("App settings")

elif menu == "Logout":
    st.header("🚪 Logout")
    st.write("You have been logged out")

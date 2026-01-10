import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.navbar {
    background-color: #2E86C1;
    padding: 15px;
    border-radius: 10px;
}

.navbar a {
    color: white;
    text-decoration: none;
    padding: 14px 20px;
    font-size: 18px;
    font-weight: bold;
}

.navbar a:hover {
    background-color: #1B4F72;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
    <a href="#home">Home</a>
    <a href="#dashboard">Dashboard</a>
    <a href="#profile">Profile</a>
    <a href="#settings">Settings</a>
    <a href="#logout">Logout</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

page = st.selectbox("Select Page", ["Home", "Dashboard", "Profile", "Settings", "Logout"])

if page == "Home":
    st.header("🏠 Home Page")

elif page == "Dashboard":
    st.header("📊 Dashboard Page")

elif page == "Profile":
    st.header("👤 Profile Page")

elif page == "Settings":
    st.header("⚙️ Settings Page")

elif page == "Logout":
    st.header("🚪 Logged Out")

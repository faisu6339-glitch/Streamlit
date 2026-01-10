import streamlit as st

st.set_page_config(layout="wide")

st.title("🚀 Simple Navbar Demo")

# --- NAVBAR ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    home_btn = st.button("🏠 Home")
with col2:
    about_btn = st.button("ℹ️ About")
with col3:
    services_btn = st.button("🛠 Services")
with col4:
    contact_btn = st.button("📞 Contact")

st.markdown("---")

# --- PAGE CONTENT ---
if home_btn:
    st.header("🏠 Home Page")
    st.write("Welcome to the Home page")

elif about_btn:
    st.header("ℹ️ About Page")
    st.write("This is the About page")

elif services_btn:
    st.header("🛠 Services Page")
    st.write("These are our services")

elif contact_btn:
    st.header("📞 Contact Page")
    st.write("Contact us here")

else:
    st.header("🏠 Home Page")
    st.write("Welcome to the Home page")

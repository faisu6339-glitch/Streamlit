import streamlit as st

st.set_page_config(page_title="Advanced Navbar", layout="wide")

# ----------------------------
# CSS FOR NAVBAR
# ----------------------------
st.markdown("""
<style>
.navbar {
    background-color: #0F172A;
    padding: 14px 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 12px;
    margin-bottom: 20px;
}

.nav-left {
    display: flex;
    align-items: center;
    gap: 30px;
}

.logo {
    font-size: 26px;
    font-weight: bold;
    color: #38BDF8;
}

.nav-btn button {
    background-color: transparent;
    color: white;
    border: none;
    font-size: 18px;
    padding: 8px 14px;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.3s;
}

.nav-btn button:hover {
    background-color: #1E293B;
    color: #38BDF8;
}

.active-btn button {
    background-color: #38BDF8 !important;
    color: black !important;
}

.nav-right {
    color: white;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# SESSION STATE
# ----------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ----------------------------
# NAVBAR UI
# ----------------------------
st.markdown("<div class='navbar'>", unsafe_allow_html=True)
left, right = st.columns([8, 2])

with left:
    col1, col2, col3, col4, col5, col6 = st.columns([2,2,2,2,2,2])

    with col1:
        if st.button("🏠 Home"):
            st.session_state.page = "Home"

    with col2:
        if st.button("📊 Dashboard"):
            st.session_state.page = "Dashboard"

    with col3:
        if st.button("👤 Profile"):
            st.session_state.page = "Profile"

    with col4:
        if st.button("⚙️ Settings"):
            st.session_state.page = "Settings"

    with col5:
        if st.button("🚪 Logout"):
            st.session_state.page = "Logout"

with right:
    st.markdown("<div class='nav-right'>👤 Faisal Sheikh</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# PAGE CONTENT
# ----------------------------
if st.session_state.page == "Home":
    st.header("🏠 Home")
    st.write("Welcome to the Home page, Faisal 😎")

elif st.session_state.page == "Dashboard":
    st.header("📊 Dashboard")
    st.write("This is your dashboard overview")

elif st.session_state.page == "Profile":
    st.header("👤 Profile")
    st.write("User profile details go here")

elif st.session_state.page == "Settings":
    st.header("⚙️ Settings")
    st.write("Application settings page")

elif st.session_state.page == "Logout":
    st.header("🚪 Logout")
    st.write("You have been logged out successfully")

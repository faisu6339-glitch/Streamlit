import streamlit as st

st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")

st.title("🔐 Secure Login Page")
st.markdown("Welcome! Please login to continue 👇")

# ----------------------------
# Dummy Database
# ----------------------------
users_db = {
    "faisal@gmail.com": {"password": "12345", "role": "User"},
    "admin@gmail.com": {"password": "admin123", "role": "Admin"}
}

# ----------------------------
# LOGIN FORM
# ----------------------------
with st.form("login_form"):

    st.subheader("Login Details")

    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")

    role = st.selectbox("👤 Login as", ["User", "Admin"])

    remember_me = st.checkbox("Remember me")

    captcha = st.text_input("🤖 Type 'yes' to verify you are human")

    login_btn = st.form_submit_button("Login")

# ----------------------------
# LOGIN VALIDATION
# ----------------------------
if login_btn:

    if email == "" or password == "":
        st.warning("⚠️ Please fill all fields")

    elif captcha.lower() != "yes":
        st.error("❌ Verification failed. Please type 'yes'")

    elif email in users_db:

        if users_db[email]["password"] == password and users_db[email]["role"] == role:
            st.success(f"✅ Login successful! Welcome {role} 😎")

            # Show extra info
            st.markdown("### 🔍 Login Summary")
            st.write("Email:", email)
            st.write("Role:", role)
            st.write("Remember Me:", remember_me)

        else:
            st.error("❌ Incorrect password or role")

    else:
        st.error("❌ User not found. Please check your email")

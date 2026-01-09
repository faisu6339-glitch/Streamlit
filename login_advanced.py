import streamlit as st

st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")

st.title("🔐 Secure Login Page")
st.markdown("Please login to continue 👇")

# ----------------------------
# Dummy Database
# ----------------------------
users_db = {
    "faisal@gmail.com": {"password": "12345", "role": "User"},
    "admin@gmail.com": {"password": "admin123", "role": "Admin"}
}

# ----------------------------
# Session State for UI
# ----------------------------
if "show_password" not in st.session_state:
    st.session_state.show_password = False

if "show_forgot" not in st.session_state:
    st.session_state.show_forgot = False

# ----------------------------
# LOGIN FORM
# ----------------------------
with st.form("login_form"):

    st.subheader("Login Details")

    email = st.text_input("📧 Email")

    # Show / Hide Password Logic
    password_type = "text" if st.session_state.show_password else "password"
    password = st.text_input("🔑 Password", type=password_type)

    show_pass = st.checkbox("👁️ Show Password")

    role = st.selectbox("👤 Login as", ["User", "Admin"])

    remember_me = st.checkbox("Remember me")

    captcha = st.text_input("🤖 Type 'yes' to verify you are human")

    login_btn = st.form_submit_button("Login")

# ----------------------------
# Toggle Show / Hide Password
# ----------------------------
if show_pass:
    st.session_state.show_password = True
else:
    st.session_state.show_password = False

# ----------------------------
# FORGOT PASSWORD UI
# ----------------------------
st.markdown("---")
forgot_btn = st.button("❓ Forgot Password?")

if forgot_btn:
    st.session_state.show_forgot = True

if st.session_state.show_forgot:
    st.subheader("🔁 Reset Password")

    forgot_email = st.text_input("Enter your registered email")

    reset_btn = st.button("Send Reset Link")

    if reset_btn:
        if forgot_email in users_db:
            st.success("📧 Reset link sent to your email (demo message)")
        else:
            st.error("❌ Email not found")

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

            st.markdown("### 🔍 Login Summary")
            st.write("Email:", email)
            st.write("Role:", role)
            st.write("Remember Me:", remember_me)

        else:
            st.error("❌ Incorrect password or role")

    else:
        st.error("❌ User not found. Please check your email")

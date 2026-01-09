import streamlit as st

st.set_page_config(page_title="Signup Page", page_icon="📝", layout="centered")

st.title("📝 Create New Account")
st.markdown("Fill the details below to create your account 👇")

# ----------------------------
# Fake Database (for demo)
# ----------------------------
if "users_db" not in st.session_state:
    st.session_state.users_db = {}

# ----------------------------
# SIGNUP FORM
# ----------------------------
with st.form("signup_form"):

    st.subheader("Signup Details")

    full_name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")
    confirm_password = st.text_input("🔒 Confirm Password", type="password")

    role = st.selectbox("👥 Register as", ["User", "Admin"])

    agree_terms = st.checkbox("I agree to the Terms & Conditions")

    signup_btn = st.form_submit_button("Create Account")

# ----------------------------
# SIGNUP VALIDATION
# ----------------------------
if signup_btn:

    if full_name == "" or email == "" or password == "" or confirm_password == "":
        st.warning("⚠️ All fields are required")

    elif password != confirm_password:
        st.error("❌ Passwords do not match")

    elif not agree_terms:
        st.error("❌ You must agree to the Terms & Conditions")

    elif email in st.session_state.users_db:
        st.error("❌ Email already registered")

    else:
        st.session_state.users_db[email] = {
            "name": full_name,
            "password": password,
            "role": role
        }

        st.success("🎉 Account created successfully!")
        st.balloons()

        st.markdown("### 📄 Account Details")
        st.write("Name:", full_name)
        st.write("Email:", email)
        st.write("Role:", role)

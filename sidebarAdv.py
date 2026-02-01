import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Advanced Sidebar Example",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Advanced Streamlit Sidebar")
st.write("Professional sidebar with form, session state, and logic")

# -----------------------------
# Initialize Session State
# -----------------------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# -----------------------------
# Sidebar Form
# -----------------------------
with st.sidebar:
    st.header("User Settings")
    st.divider()

    with st.form("user_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", 1, 100, 22)

        gender = st.radio(
            "Gender",
            ["Male", "Female", "Other"]
        )

        course = st.selectbox(
            "Course",
            ["Data Science", "Web Development", "AI/ML", "Cloud"]
        )

        experience = st.slider(
            "Experience (years)",
            0, 15, 1
        )

        subscribe = st.checkbox("Subscribe to newsletter")

        submit_btn = st.form_submit_button("Submit")

# -----------------------------
# Submit Logic
# -----------------------------
if submit_btn:
    st.session_state.submitted = True
    st.session_state.name = name
    st.session_state.age = age
    st.session_state.gender = gender
    st.session_state.course = course
    st.session_state.experience = experience
    st.session_state.subscribe = subscribe

# -----------------------------
# Main Content Area
# -----------------------------
if st.session_state.submitted:
    st.success("Form submitted successfully 🎉")

    st.subheader("User Profile")
    st.write("Name:", st.session_state.name)
    st.write("Age:", st.session_state.age)
    st.write("Gender:", st.session_state.gender)
    st.write("Course:", st.session_state.course)
    st.write("Experience:", f"{st.session_state.experience} years")
    st.write("Subscribed:", "Yes" if st.session_state.subscribe else "No")

else:
    st.info("Fill the sidebar form and click Submit")

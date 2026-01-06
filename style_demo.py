import streamlit as st

# ----------------------------
# BASIC COLORED TEXT
# ----------------------------
st.markdown("<h1 style='color:red;'>Red Title Text</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color:green;'>Green Header Text</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue;'>Blue Subheader Text</h3>", unsafe_allow_html=True)

st.markdown("<p style='color:purple;'>This is purple paragraph text</p>", unsafe_allow_html=True)
st.markdown("<p style='color:orange;'>This is orange text</p>", unsafe_allow_html=True)

# ----------------------------
# COLORED TEXT WITH BACKGROUND
# ----------------------------
st.markdown(
    "<div style='background-color:lightblue; padding:10px; border-radius:10px; margin-bottom:15px;'>"
    "<h3 style='color:black;'>This is text with background color</h3>"
    "</div>",
    unsafe_allow_html=True
)

# ----------------------------
# CUSTOM CSS STYLING
# ----------------------------
st.markdown("""
<style>
.big-title {
    font-size: 50px;
    color: #FF5733;
    font-weight: bold;
}

.blue-box {
    background-color: #D6EAF8;
    padding: 15px;
    border-radius: 10px;
    border: 2px solid #3498DB;
    margin-bottom: 15px;
}

.green-text {
    color: #28B463;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>Custom CSS Big Title</div>", unsafe_allow_html=True)
st.markdown("<div class='blue-box'>This is a blue box using CSS class</div>", unsafe_allow_html=True)
st.markdown("<p class='green-text'>This is green text using CSS class</p>", unsafe_allow_html=True)

# ----------------------------
# STATUS MESSAGES
# ----------------------------
st.success("This is success message (green)")
st.info("This is info message (blue)")
st.warning("This is warning message (yellow)")
st.error("This is error message (red)")

# ----------------------------
# BUTTON STYLING
# ----------------------------
st.markdown("""
<style>
div.stButton > button {
    background-color: #8E44AD;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 200px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

if st.button("Styled Button"):
    st.success("You clicked the styled button!")

# ----------------------------
# SECTION SEPARATOR
# ----------------------------
st.markdown("---")

st.markdown("<h2 style='color:#2E86C1;'>Section with Custom Color</h2>", unsafe_allow_html=True)

# ----------------------------
# BACKGROUND COLOR BOXES WITH SPACING
# ----------------------------
st.markdown(
    "<div style='background-color:#D1F2EB; padding:10px; border-radius:8px; margin-bottom:20px;'>"
    "<p style='color:#117A65;'>This is a paragraph in the custom colored section.</p>"
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div style='background-color:#FADBD8; padding:10px; border-radius:8px; margin-bottom:20px;'>"
    "<p style='color:pink;'>This section is using inline CSS color styling</p>"
    "</div>",
    unsafe_allow_html=True
)

# ----------------------------
# ANOTHER WAY – CSS CLASSES
# ----------------------------
st.markdown("""
<style>
.custom-box-1 {
    background-color: #D6EAF8;
    padding: 12px;
    border-radius: 10px;
    color: #1B4F72;
    font-size: 18px;
    margin-bottom: 20px;
}

.custom-box-2 {
    background-color: #F5B7B1;
    padding: 12px;
    border-radius: 10px;
    color: #78281F;
    font-size: 18px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='custom-box-1'>This is first custom colored box</div>", unsafe_allow_html=True)
st.markdown("<div class='custom-box-2'>This is second custom colored box</div>", unsafe_allow_html=True)

# ----------------------------
# EXTRA SPACING EXAMPLE
# ----------------------------
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    "<div style='background-color:#EBDEF0; padding:10px; border-radius:8px;'>"
    "<p style='color:#6C3483;'>This box has extra space before it</p>"
    "</div>",
    unsafe_allow_html=True
)

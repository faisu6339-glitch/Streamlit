import streamlit as st

# ----------------------------
# Title and Header
# ----------------------------
st.title("📊 Dashboard Page")

st.title("Streamlit Text & Display Demo")
st.header("Demonstration of Text and Display Elements")
st.subheader("Using Various Streamlit Functions")


# MARKDOWN HEADER SIZES
# ----------------------------

st.markdown("# Markdown H1 Header (#)")
st.markdown("## Markdown H2 Header (##)")
st.markdown("### Markdown H3 Header (###)")
st.markdown("#### Markdown H4 Header (####)")
st.markdown("##### Markdown H5 Header (#####)")
st.markdown("###### Markdown H6 Header (######)")

# ----------------------------
# TEXT SIZES USING MARKDOWN
# ----------------------------

st.markdown("### Big Text using ###")
st.markdown("#### Medium Text using ####")
st.markdown("##### Small Text using #####")
st.markdown("###### Very Small Text using ######")

# ----------------------------
# Normal Text
# ----------------------------
st.text("This is a simple text element in Streamlit.")
st.write("This is a write element, which can display various data types.")

# ----------------------------
# Markdown
# ----------------------------
st.markdown("### This is a markdown header")
st.markdown("You can use **bold**, *italic*, and `code` formatting in markdown.")
st.markdown("- Item 1\n- Item 2\n- Item 3")
st.markdown("> This is a blockquote in markdown.")
st.markdown("**This text is bold using markdown.**")
st.markdown("*This text is italic using markdown.*")
st.markdown("`This is inline code using markdown.`")

# ----------------------------
# Image
# ----------------------------
st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)

# ----------------------------
# Bullet Points
# ----------------------------
st.markdown("### Bullet Points Example")
st.markdown("""
- First bullet point  
- Second bullet point  
- Third bullet point  
""")

# ----------------------------
# Numbered Lists
# ----------------------------
st.markdown("### Numbered List Example")
st.markdown("""
1. First numbered point  
2. Second numbered point  
3. Third numbered point  
""")

# ----------------------------
# Code Block
# ----------------------------
st.markdown("### Code Block Example")
st.code("""
for i in range(5):
    print(i)
""", language="python")
st.write(range(5))


# ----------------------------
# LaTeX (Math)
# ----------------------------
st.markdown("### Math Formula (LaTeX)")
st.latex(r"a^2 + b^2 = c^2")

# ----------------------------
# Status Messages
# ----------------------------
st.success("This is a success message")
st.info("This is an info message")
st.warning("This is a warning message")
st.error("This is an error message")

# ----------------------------
# Variables Display
# ----------------------------
name = "Faisal"
age = 22

st.markdown("### Displaying Variables")
st.write("Name:", name)
st.write("Age:", age)
st.write(f"My name is {name} and I am {age} years old.")

# ----------------------------
# Caption and Divider
# ----------------------------
st.markdown("---")
st.caption("This is a small caption text at the bottom.")
st.markdown("End of the Streamlit Text & Display Demo.")
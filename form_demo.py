import streamlit as st

st.title("📝 Complete Streamlit Form Demo")

st.markdown("Fill all the fields below and submit the form 👇")

# ----------------------------
# FORM START
# ----------------------------
with st.form("user_form"):

    # TEXT INPUT
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")

    # PASSWORD
    password = st.text_input("Enter your password", type="password")

    # NUMBER INPUT
    age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)

    salary = st.number_input("Enter your salary", min_value=0.0, step=1000.0)

    # TEXT AREA
    address = st.text_area("Enter your address")

    # SELECT BOX
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])

    # MULTISELECT
    skills = st.multiselect(
        "Select your skills",
        ["Python", "Machine Learning", "Deep Learning", "NLP", "SQL", "Power BI"]
    )

    # RADIO BUTTON
    experience = st.radio("Experience Level", ["Fresher", "1-3 Years", "3-5 Years", "5+ Years"])

    # CHECKBOX
    terms = st.checkbox("I agree to the Terms & Conditions")

    # SLIDER
    rating = st.slider("Rate your skill level", 1, 10)

    # DATE INPUT
    dob = st.date_input("Select your Date of Birth")

    # TIME INPUT
    interview_time = st.time_input("Preferred Interview Time")

    # FILE UPLOADER
    resume = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    # COLOR PICKER
    fav_color = st.color_picker("Pick your favourite color")

    # SUBMIT BUTTON
    submit_button = st.form_submit_button("Submit Form")

# ----------------------------
# FORM SUBMISSION RESULT
# ----------------------------
if submit_button:

    if not terms:
        st.error("❌ You must agree to the Terms & Conditions")
    else:
        st.success("✅ Form submitted successfully!")

        st.markdown("### 📄 Submitted Data")

        st.write("**Name:**", name)
        st.write("**Email:**", email)
        st.write("**Age:**", age)
        st.write("**Salary:**", salary)
        st.write("**Address:**", address)
        st.write("**Gender:**", gender)
        st.write("**Skills:**", skills)
        st.write("**Experience Level:**", experience)
        st.write("**Rating:**", rating)
        st.write("**Date of Birth:**", dob)
        st.write("**Interview Time:**", interview_time)
        st.write("**Favourite Color:**", fav_color)

        if resume is not None:
            st.success("📎 Resume uploaded successfully!")


##Another way to show submitted data
import streamlit as st

st.title("📝 Input & Display Demo")

# ----------------------------
# 1. TEXT INPUT
# ----------------------------
st.header('1. Text Input')

name = st.text_input('Enter your name :', value='Aaliya Fatma')
st.write('You entered :', name)

# ----------------------------
# 2. TEXT AREA
# ----------------------------
st.subheader('2. Text Area')

address = st.text_area('Enter your address :', value='123, ABC Street, City')
st.write('You entered :', address)

# ----------------------------
# 3. NUMBER INPUT
# ----------------------------
st.subheader('3. Number Input')

age = st.number_input('Enter your age :', min_value=1, max_value=100, step=1)
st.write('You entered :', age)

# ----------------------------
# 4. SELECT BOX
# ----------------------------
st.subheader('4. Select Box')

gender = st.selectbox('Select your gender :', ['Male', 'Female', 'Other'])
st.write('You selected :', gender)

# ----------------------------
# 5. RADIO BUTTON
# ----------------------------
st.subheader('5. Radio Button')

experience = st.radio('Select experience level :', ['Fresher', '1-3 Years', '3-5 Years', '5+ Years'])
st.write('You selected :', experience)

# ----------------------------
# 6. CHECKBOX
# ----------------------------
st.subheader('6. Checkbox')

agree = st.checkbox('I agree to the terms and conditions')

if agree:
    st.success("You agreed to the terms")
else:
    st.warning("You have not agreed yet")

# ----------------------------
# 7. MULTISELECT
# ----------------------------
st.subheader('7. Multi Select')

skills = st.multiselect(
    'Select your skills :',
    ['Python', 'Machine Learning', 'Deep Learning', 'NLP', 'SQL', 'Power BI']
)
st.write('Your skills :', skills)

# ----------------------------
# 8. SLIDER
# ----------------------------
st.subheader('8. Slider')

rating = st.slider('Rate your skill level :', 1, 10)
st.write('Your rating :', rating)

# ----------------------------
# 9. DATE INPUT
# ----------------------------
st.subheader('9. Date Input')

dob = st.date_input('Select your Date of Birth :')
st.write('Your DOB :', dob)

# ----------------------------
# 10. FILE UPLOADER
# ----------------------------
st.subheader('10. File Uploader')

file = st.file_uploader('Upload your resume (PDF) :', type=['pdf'])

if file is not None:
    st.success("File uploaded successfully!")

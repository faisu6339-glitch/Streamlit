#1️⃣ st.button() – Basic Button
import streamlit as st

if st.button("Click Me"):
    st.write("Button clicked!")

#2️⃣ st.download_button() – Download Button
import streamlit as st

data="Hello,faisal"
st.download_button("Download Data", data)

import pandas as pd
import streamlit as st

df = pd.DataFrame({"Name":["A","B"],"Marks":[90,85]})
st.download_button("Download CSV", df.to_csv(index=False), file_name="data.csv")

#3️⃣ st.form_submit_button() – Form Submit Button
import streamlit as st
with st.form("my_form"):
    name=st.text_input("Enter your name")
    age=st.number_input("Enter your age", min_value=0, max_value=120, step=1)
    submitted=st.form_submit_button("Submit")
    if submitted:
        st.write("Form Submitted:::",f"Name: {name}, Age: {age}")
    else:
        st.write("Form not submitted yet.")

#4️⃣ st.file_uploader() – Upload Button
import streamlit as st
file=st.file_uploader("Upload a file", type=["txt","csv","png","jpg"])
if file is not None:
    st.write("File uploaded successfully:", file.name)
    if file.type.startswith("text/"):
        content = file.read().decode("utf-8")
        st.text_area("File Content", content)
    elif file.type == "image/png" or file.type == "image/jpeg":
        st.image(file)
    elif file.type == "text/csv":
        import pandas as pd
        df = pd.read_csv(file)
        st.dataframe(df)

#5️⃣ st.checkbox() – Button-like Toggle
import streamlit as st

if st.checkbox("Show/Hide Text"):
    st.write("The checkbox is checked!")
else:
    st.write("The checkbox is unchecked.")

#6️⃣ st.radio() – Radio Button Selection
import streamlit as st
option = st.radio("Select an option:", ("Option 1", "Option 2", "Option 3"))
st.write("You selected:", option)

#7️⃣ st.selectbox() – Dropdown Selection
import streamlit as st
option = st.selectbox("Choose an option:", ["Option A", "Option B", "Option C"])
st.write("You chose:", option)

#8️⃣ st.multiselect() – Multiple Selection
import streamlit as st
options = st.multiselect("Select options:", ["Option 1", "Option 2", "Option 3", "Option 4"])
st.write("You selected:", options)

#9️⃣ st.slider() – Slider Input
import streamlit as st
value = st.slider("Select a value:", 0, 100, 50)
st.write("You selected:", value)

#🔟 st.toggle() – Modern On/Off Button (New)
import streamlit as st
darken_mode = st.toggle("Enable Dark Mode", value=False)
if darken_mode:
    st.write("Dark Mode is Enabled")
else:   
    st.write("Dark Mode is Disabled")
print("Dark Mode status:", darken_mode)

#1️⃣1️⃣ st.columns() + Button – Layout Buttons
import streamlit as st
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Button 1"):
        st.write("Button 1 clicked!")
with col2:
    if st.button("Button 2"):
        st.write("Button 2 clicked!")
with col3:
    if st.button("Button 3"):
        st.write("Button 3 clicked!")
        
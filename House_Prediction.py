import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("🏠 House Price Prediction App")
st.write("Enter house details and predict house price using ML model")

# -------------------------
# LOAD MODEL & COLUMNS
# -------------------------
model = joblib.load("house_price_model.pkl")
num_cols = joblib.load("num_cols.pkl")
cat_cols = joblib.load("cat_cols.pkl")

# -------------------------
# USER INPUT UI
# -------------------------
st.subheader("Enter House Details")

user_input = {}

# Numeric Inputs
for col in num_cols:
    user_input[col] = st.number_input(f"{col}", value=0.0)

# Categorical Inputs
for col in cat_cols:
    user_input[col] = st.text_input(f"{col}")

# -------------------------
# PREDICT BUTTON
# -------------------------
if st.button("💰 Predict House Price"):
    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)[0]

    st.success(f"🏷️ Estimated House Price: ₹ {prediction:,.2f}")

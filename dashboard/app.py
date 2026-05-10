import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("../src/model.pkl", "rb"))

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details below:")

time = st.number_input("Time")
amount = st.number_input("Amount")

# Simple input sample
input_data = pd.DataFrame([[time, amount]], columns=["Time", "Amount"])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠ Fraudulent Transaction Detected")
    else:
        st.success("✅ Normal Transaction")
# app/app.py
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)


import streamlit as st
from predict import make_prediction

st.set_page_config(page_title="Loan Eligibility Predictor", page_icon="💰", layout="centered")

st.title("💰 Loan Eligibility Prediction System")
st.write("Fill the details below to check if the loan will be approved.")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

app_income = st.number_input("Applicant Income", min_value=0)
coapp_income = st.number_input("Co-Applicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])

if st.button("Predict Loan Eligibility"):
    data = {
        "Gender": gender,
        "Married": married,
        "Education": education,
        "Self_Employed": self_employed,
        "Property_Area": property_area,
        "ApplicantIncome": app_income,
        "CoapplicantIncome": coapp_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history
    }

    result = make_prediction(data)

    st.success(f"Loan Status: **{result}**")


import streamlit as st
import pandas as pd
import joblib

st.markdown(
    """
    <h1 style="text-align:center; color: #75B06F">🏦 Loan Approval Prediction App</h1>
    <p style="text-align:center;font-size:18px;">
        Predict whether a loan will be approved based on applicant financial details.
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---- TOP IMAGE ----
st.image("Banner.jpg", width=700)


# ---- FORM HEADER ----
st.markdown("## 🧾 Loan Application Form")

# ---- INPUT FIELDS (MAIN PAGE) ----
col1, col2 ,col3= st.columns(3)

with col1:
    no_of_dependents = st.number_input("Number of Dependents", 0, 20)
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    income_annum = st.number_input("Annual Income", 0)
    loan_amount = st.number_input("Loan Amount", 0)
    loan_term = st.number_input("Loan Term (Months)", 6, 480)

with col3:
    cibil_score = st.number_input("CIBIL Score", 300, 900)
    residential_assets_value = st.number_input("Residential Assets Value", 0)
    commercial_assets_value = st.number_input("Commercial Assets Value", 0)

col4, col5, col6 = st.columns(3)

with col4:
    luxury_assets_value = st.number_input("Luxury Assets Value", 0)

with col5:
    bank_asset_value = st.number_input("Bank Asset Value", 0)

# ---- LOAD MODEL ----
model = joblib.load("loan_prediction_model.pkl")

# ---- PREDICTION ----
st.markdown("### 📊 Prediction Result")

if st.button("Predict Loan Approval"):
    input_data = pd.DataFrame({
        "no_of_dependents": [no_of_dependents],
        "education": [education],
        "self_employed": [self_employed],
        "income_annum": [income_annum],
        "loan_amount": [loan_amount],
        "loan_term": [loan_term],
        "cibil_score": [cibil_score],
        "residential_assets_value": [residential_assets_value],
        "commercial_assets_value": [commercial_assets_value],
        "luxury_assets_value": [luxury_assets_value],
        "bank_asset_value": [bank_asset_value]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
        st.image("loan approved.jpg", width=300)
    else:
        st.error("❌ Loan Rejected")
        st.image("loan rejected.jpg", width=300)

# ---- FOOTER ----
st.markdown("---")
st.markdown("<p style='text-align:center'>Developed by Preethi 💼</p>", unsafe_allow_html=True)
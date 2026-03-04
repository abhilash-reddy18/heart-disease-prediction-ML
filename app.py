import streamlit as st
import numpy as np
import pickle
st.sidebar.title("About")
st.sidebar.info(
"""
This app predicts the likelihood of heart disease using a trained Logistic Regression model.

Developed by:  
**Abhilash Reddy**

Machine Learning Project
"""
)
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered"
)

# Load trained model and scaler
model = pickle.load(open("heart_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

# App title
st.title("❤️ Heart Disease Prediction")
st.markdown(
"""
This application predicts the likelihood of **heart disease** using a trained **Logistic Regression model**.

Enter patient medical details below and click **Predict** to see the result.
"""
)
with st.expander("ℹ️ About the Dataset"):
    st.write("""
    The model is trained on the Cleveland Heart Disease dataset which contains clinical attributes such as:

    - Age
    - Sex
    - Chest pain type
    - Blood pressure
    - Cholesterol
    - Maximum heart rate
    - Exercise induced angina

    The model predicts whether a patient is likely to have heart disease.
    """)

st.subheader("Enter Patient Details")

# inputs for prediction
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 20, 100)
    sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0,1])
    cp = st.selectbox("Chest Pain Type", [0,1,2,3])
    trestbps = st.number_input("Resting Blood Pressure")
    chol = st.number_input("Cholesterol")
    fbs = st.selectbox("Fasting Blood Sugar >120", [0,1])
    restecg = st.selectbox("Resting ECG", [0,1,2])

with col2:
   
    thalach = st.number_input("Maximum Heart Rate")
    exang = st.selectbox("Exercise Induced Angina", [0,1])
    oldpeak = st.number_input("ST Depression")
    slope = st.selectbox("Slope of ST segment", [0,1,2])
    ca = st.selectbox("Number of Major Vessels", [0,1,2,3])
    thal = st.selectbox("Thalassemia", [0,1,2,3])

# Prediction button
col1, col2, col3 = st.columns([1,2,1])

with col2:
    predict_button = st.button("🔍 Predict Heart Disease")
    
if predict_button:

    input_data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠ High Risk of Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")

st.markdown("---")
st.markdown(
"""
<center>
Developed by <b>Abhilash Reddy</b>  
Machine Learning Enthusiastic | Data Science
</center>
""",
unsafe_allow_html=True
)
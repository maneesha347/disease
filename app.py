import streamlit as st
import requests

st.title("Disease Prediction App")

# Select disease type
disease = st.selectbox("Select Disease", ["Heart", "Diabetes"])

if disease == "Heart":
    st.header("Heart Disease Prediction")
    age = st.slider("Age", 20, 100)
    sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
    cp = st.selectbox("Chest pain type", [0, 1, 2, 3])
    trestbps = st.slider("Resting BP", 90, 200)
    chol = st.slider("Cholesterol", 100, 400)
    fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
    restecg = st.selectbox("Rest ECG", [0, 1, 2])
    thalach = st.slider("Max heart Rate", 70, 200)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.slider("Oldpeak", 0.0, 6.0, 0.6)
    slope = st.selectbox("Slope", [0, 1, 2])
    ca = st.selectbox("CA", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thal", [0, 1, 2])

    features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    endpoint = "http://localhost:8000/heart_pred"

elif disease == "Diabetes":
    st.header("Diabetes Prediction")
    pregnancies = st.slider("Pregnancies", 0, 20)
    glucose = st.slider("Glucose", 0, 300)
    blood_pressure = st.slider("Blood Pressure", 0, 200)
    skin_thickness = st.slider("Skin Thickness", 0, 100)
    insulin = st.slider("Insulin", 0, 900)
    bmi = st.slider("BMI", 0.0, 70.0)
    dpf = st.slider("Diabetes Pedigree Function", 0.0, 2.5)
    age = st.slider("Age", 10, 100)

    # No Outcome in input — it is the target
    features = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
    endpoint = "http://localhost:8000/diabetes_pred"

if st.button("Predict"):
    response = requests.post(endpoint, json=features)
    if response.status_code == 200:
        risk = response.json()['risk_score']
        st.success(f"Risk score: {risk:.2f}")
    else:
        st.error(f"Error: {response.text}")
 
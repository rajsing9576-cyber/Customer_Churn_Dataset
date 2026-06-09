import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('placement.pickle', 'rb'))

st.title("Placement Prediction App")

st.write("Enter the student details below:")

# Input fields
cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

iq = st.number_input(
    "IQ Score",
    min_value=0,
    max_value=200,
    value=100,
    step=1
)

# Prediction
if st.button("Predict"):
    input_data = np.array([[cgpa, iq]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.success("🎉 Student is likely to be Placed")
    else:
        st.error("❌ Student is unlikely to be Placed")

    st.write(f"Placement Probability: **{probability[1]:.2%}**")
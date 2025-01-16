import streamlit as st
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

# Load the pre-trained model and scaler
with open('regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit Input Fields
st.title("Boston Housing Pred App ⌨🏠")
crim = st.number_input("Enter the crim", value=0.0)
zn = st.number_input("Enter the zn", value=0.0)
indus = st.number_input("Enter the indus", value=0.0)
chas = st.number_input("Enter the chas", value=0.0)
nox = st.number_input("Enter the nox", value=0.0)
rm = st.number_input("Enter the rm", value=0.0)
age = st.number_input("Enter your age", value=0.0)
dis = st.number_input("Enter the dis", value=0.0)
rad = st.number_input("Enter the rad", value=0.0)
ptratio = st.number_input("Enter the ptratio", value=0.0)
b = st.number_input("Enter B", value=0.0)
istat = st.number_input("Enter istat", value=0.0)
tax = st.number_input("Enter tax", value=0.0)

# Predict when button is pressed
if st.button("Predict"):
    # Prepare the input data
    input_data = np.array([[crim,zn, indus, chas, nox, rm, age, dis, rad, ptratio, b, istat, tax]])

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Make the prediction
    result = model.predict(input_data_scaled)

    # Display the prediction
    st.write(f"The predicted result is: {result[0]:.2f}$")


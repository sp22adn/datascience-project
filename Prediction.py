import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the best model and preprocessor
model = joblib.load('best_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

# Streamlit application title
st.title('House Price Prediction App')

# Input fields for the user
bedrooms = st.number_input('Bedrooms', min_value=0, max_value=10, value=3)
bathrooms = st.number_input('Bathrooms', min_value=0.0, max_value=10.0, value=2.0)
sqft_living = st.number_input('Living Area (sqft)', min_value=0, max_value=10000, value=2000)
sqft_lot = st.number_input('Lot Area (sqft)', min_value=0, max_value=100000, value=5000)
floors = st.number_input('Floors', min_value=0.0, max_value=5.0, value=1.0)
waterfront = st.selectbox('Waterfront', options=[0, 1])
view = st.selectbox('View', options=[0, 1, 2, 3, 4])
condition = st.selectbox('Condition', options=[1, 2, 3, 4, 5])
grade = st.selectbox('Grade', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
sqft_above = st.number_input('Sqft Above', min_value=0, max_value=10000, value=1500)
sqft_basement = st.number_input('Sqft Basement', min_value=0, max_value=5000, value=500)
zipcode = st.number_input('Zipcode', min_value=0, max_value=99999, value=98000)
lat = st.number_input('Latitude', min_value=0.0, max_value=100.0, value=47.5)
long = st.number_input('Longitude', min_value=-180.0, max_value=180.0, value=-122.0)
yr_built = st.number_input('Year Built', min_value=1800, max_value=2024, value=1990)
yr_renovated = st.number_input('Year Renovated', min_value=0, max_value=2024, value=0)

# Compute additional features
age = 2024 - yr_built
renovated = 1 if yr_renovated > 0 else 0

# Create a DataFrame for the input features
input_features = pd.DataFrame({
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'sqft_living': [sqft_living],
    'sqft_lot': [sqft_lot],
    'floors': [floors],
    'waterfront': [waterfront],
    'view': [view],
    'condition': [condition],
    'grade': [grade],
    'sqft_above': [sqft_above],
    'sqft_basement': [sqft_basement],
    'zipcode': [zipcode],
    'lat': [lat],
    'long': [long],
    'age': [age],
    'renovated': [renovated]
})

# Add a predict button
if st.button('Predict'):
    # Preprocess the input features
    input_features_preprocessed = preprocessor.transform(input_features)

    # Make a prediction
    predicted_price = model.predict(input_features_preprocessed)

    # Display the prediction
    st.subheader(f'Predicted House Price: ${predicted_price[0]:,.2f}')

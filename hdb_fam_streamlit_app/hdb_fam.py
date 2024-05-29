import streamlit as st
from joblib import load
import pandas as pd

st.image('hdb_fam_streamlit_app/PropNex logo.png', width=200)  # Adjust width as needed

# Load your trained pipeline
pipeline = load('hdb_fam_streamlit_app/housing_price_prediction_pipeline.joblib')

with st.form(key='input_form'):
    flat_type = st.selectbox('Flat Type', options=['3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI-GENERATION'])
    
    # Define floor area ranges for each flat type
    floor_area_ranges = {
        '3 ROOM': (50, 80),
        '4 ROOM': (70, 110),
        '5 ROOM': (100, 140),
        'EXECUTIVE': (130, 160),
        'MULTI-GENERATION': (150, 200),
    }
    
    # Get the floor area range based on the selected flat type
    min_area, max_area = floor_area_ranges[flat_type]
    floor_area_sqm = st.slider('Floor Area (sqm)', min_value=min_area, max_value=max_area, value=(min_area + max_area) // 2, step=1)
    
    flat_age = st.slider('Age of Flat (years)', min_value=5, max_value=60, value=10, step=1)
    pri_sch_tier = st.selectbox('Primary School Tier', options=['Tier 1', 'Tier 2', 'Tier 3'])
    Mall_Within = st.selectbox('Mall Within', options=['1km', '2km', '>2km'])
    dist_from_cbd_km = st.slider('Distance from CBD (km)', min_value=0.0, max_value=50.0, value=25.0, step=0.5)

    submit_button = st.form_submit_button(label='Predict')

if submit_button:
    input_data = {
        'flat_age': [flat_age],
        'floor_area_sqm': [floor_area_sqm],
        # Additional one-hot encoding for flat_type as before
        'flat_type_MULTI-GENERATION': [1 if flat_type == 'MULTI-GENERATION' else 0],
        'flat_type_3 ROOM': [1 if flat_type == '3 ROOM' else 0],
        'flat_type_5 ROOM': [1 if flat_type == '5 ROOM' else 0],
        'flat_type_4 ROOM': [1 if flat_type == '4 ROOM' else 0],
        'flat_type_EXECUTIVE': [1 if flat_type == 'EXECUTIVE' else 0],
        'pri_sch_tier_1': [1 if pri_sch_tier == 'Tier 1' else 0],
        'pri_sch_tier_2': [1 if pri_sch_tier == 'Tier 2' else 0],
        'Mall_Within_1km': [1 if Mall_Within == '1km' else 0],
        'Mall_Within_2km': [1 if Mall_Within == '2km' else 0],
        'dist_from_cbd_km': [dist_from_cbd_km],
    }

    input_df = pd.DataFrame(input_data)
    
    # Make prediction with the pipeline
    prediction = pipeline.predict(input_df)
    st.write(f'Predicted Resale Price: {prediction[0] * 2.5:.2f}')  # Adjust the display of prediction as needed

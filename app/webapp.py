import streamlit as st


def predict():
    import random

    prediction_placeholder.empty()
    prediction_placeholder.text(round(random.random(), 4))


def predict_with_ml():
    import mlflow
    import pandas as pd

    research_code = 1 if research == 'Yes' else 0
    model_name = 'Graduate Admission Predictor'
    stage = 'production'

    # Load model
    mlflow.set_tracking_uri('http://localhost:5000')
    model_uri = f'models:/{model_name}/{stage}'
    model_from_registry = mlflow.sklearn.load_model(model_uri)

    # Load data
    production_data = pd.DataFrame([[gre, toefl, u_rating, sop, lor, gpa, research_code, gender]],
                                   columns=['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA',
                                            'Research', 'Gender'])

    # Predict
    prediction = model_from_registry.predict(production_data)
    prediction_placeholder.empty()
    prediction_placeholder.text(round(prediction[0], 4))


st.title('Graduate Admission Prediction')

c1 = st.container()

with c1:
    col1, col2, col3, col4 = st.columns(4)
    gre = col1.number_input('GRE Score', min_value=0, max_value=340, value=300, step=1, on_change=None)
    toefl = col2.number_input('TOEFL Score', min_value=0, max_value=120, value=100, step=1, on_change=None)
    u_rating = col3.selectbox('University Rating', [1, 2, 3, 4, 5], index=0, key='UNIVERSITY_RATING', on_change=None)
    sop = col4.number_input('SOP Strength', min_value=0.0, max_value=5.0, value=3.0, step=0.1, on_change=None)
    lor = col1.number_input('LOR Strength', min_value=0.0, max_value=5.0, value=3.0, step=0.1, on_change=None)
    gpa = col2.number_input('GPA', min_value=0.0, max_value=10.0, value=8.5, step=0.1, on_change=None)
    research = col3.selectbox('Research Experience', ['Yes', 'No'], index=0, key='RESEARCH', on_change=None)
    gender = col4.selectbox('Gender', ['M', 'F'], index=0, key='GENDER', on_change=None)

c2 = st.container()
with c2:
    col1, col2, col3, prediction_placeholder, col5, col6 = st.columns(6)

    # Change 'on_click' below to use models registered in MLFlow
    predict_button = col3.button('Predict', on_click=predict, type="secondary")

    prediction_placeholder.empty()

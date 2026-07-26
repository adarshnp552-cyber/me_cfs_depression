import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("lr_dep.pkl")

st.title("ME/CFS Depression Prediction")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=25)

gender = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

sleep_quality_index = st.number_input("Sleep Quality Index", value=5.0)
brain_fog_level = st.number_input("Brain Fog Level", value=5.0)
physical_pain_score = st.number_input("Physical Pain Score", value=5.0)
stress_level = st.number_input("Stress Level", value=5.0)
depression_phq9_score = st.number_input("Depression PHQ9 Score", value=10.0)
fatigue_severity_scale_score = st.number_input("Fatigue Severity Scale Score", value=20.0)
pem_duration_hours = st.number_input("PEM Duration Hours", value=10.0)
hours_of_sleep_per_night = st.number_input("Hours of Sleep Per Night", value=7.0)

pem_present = st.selectbox("PEM Present", [0, 1])
work_status = st.number_input("Work Status", value=0)
social_activity_level = st.number_input("Social Activity Level", value=0)
exercise_frequency = st.number_input("Exercise Frequency", value=0)
meditation_or_mindfulness = st.selectbox("Meditation or Mindfulness", [0, 1])

if st.button("Predict"):

    data = pd.DataFrame([[
        age,
        gender,
        sleep_quality_index,
        brain_fog_level,
        physical_pain_score,
        stress_level,
        depression_phq9_score,
        fatigue_severity_scale_score,
        pem_duration_hours,
        hours_of_sleep_per_night,
        pem_present,
        work_status,
        social_activity_level,
        exercise_frequency,
        meditation_or_mindfulness
    ]], columns=[
        'age',
        'gender',
        'sleep_quality_index',
        'brain_fog_level',
        'physical_pain_score',
        'stress_level',
        'depression_phq9_score',
        'fatigue_severity_scale_score',
        'pem_duration_hours',
        'hours_of_sleep_per_night',
        'pem_present',
        'work_status',
        'social_activity_level',
        'exercise_frequency',
        'meditation_or_mindfulness'
    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Prediction: Depression")
    else:
        st.success("Prediction: ME/CFS")

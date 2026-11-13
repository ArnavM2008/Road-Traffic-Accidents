import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Set up the app
st.set_page_config(
    page_title="Road Traffic Accident Risk Analysis",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Road Traffic Accident Risk Analysis")

st.write(
    "Select the driving conditions below to estimate "
    "the severity of a potential road accident."
)

# Find the saved model and dataset
app_folder = Path(__file__).resolve().parent

@st.cache_resource
def load_model():
    return joblib.load(app_folder / "risk_model.joblib")

@st.cache_data
def load_data():
    df = pd.read_csv(app_folder / "crashes_clean.csv")
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )
    return df

try:
    model = load_model()
    crashes = load_data()
except (FileNotFoundError, OSError) as error:
    st.error(f"Unable to load the model or dataset: {error}")
    st.stop()

# Let users choose driving conditions
st.subheader("Driving Conditions")

def get_options(column):
    return sorted(
        crashes[column].dropna().astype(str).unique().tolist()
    )

light = st.selectbox(
    "Lighting Conditions",
    get_options("light_conditions")
)

weather = st.selectbox(
    "Weather Conditions",
    get_options("weather_conditions")
)

road = st.selectbox(
    "Road Surface Conditions",
    get_options("road_surface_conditions")
)

junction = st.selectbox(
    "Junction Type",
    get_options("types_of_junction")
)

hour = st.slider(
    "Hour of Day",
    min_value=0,
    max_value=23,
    value=12
)

# Predict severity using the trained model
if st.button("Predict Accident Severity"):

    user_input = pd.DataFrame({
        "light_conditions": [light],
        "weather_conditions": [weather],
        "road_surface_conditions": [road],
        "types_of_junction": [junction],
        "hour": [hour]
    })

    prediction = model.predict(user_input)[0]

    class_index = list(model.classes_).index(1)
    score = model.predict_proba(user_input)[0][class_index]

    st.subheader("Prediction Results")

    st.metric(
        "High-Severity Prediction Score",
        f"{score:.1%}"
    )

    if prediction == 1:
        st.warning(
            "The model predicts a serious or fatal accident."
        )
    else:
        st.success(
            "The model predicts a slight-injury accident."
        )

st.divider()

st.caption(
    "This model uses historical human-driven crash data "
    "from Addis Ababa. The score is a model estimate of "
    "severity if a crash occurs, not the probability of "
    "having an accident. It is not a calibrated safety "
    "or real-world driving risk measurement."
)

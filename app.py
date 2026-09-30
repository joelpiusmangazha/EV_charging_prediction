import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="EV Charging Duration Prediction",
    page_icon="🔋",
    layout="wide"
)

# App title
st.title("🔋 EV Charging Duration Prediction")
st.write("Explore electric vehicle charging session data.")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("ev_charging_patterns.csv")

try:
    data = load_data()

    # Dataset overview
    st.header("Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Charging Sessions", data.shape[0])

    with col2:
        st.metric("Total Columns", data.shape[1])

    # Show dataset
    st.subheader("Dataset Preview")
    st.dataframe(data.head(10), use_container_width=True)

    # Missing values
    st.subheader("Missing Values")

    missing_values = data.isnull().sum()
    missing_values = missing_values[missing_values > 0]

    if missing_values.empty:
        st.success("No missing values found.")
    else:
        st.dataframe(
            missing_values.rename("Missing Count"),
            use_container_width=True
        )

    # Data cleaning
    st.subheader("Cleaned Dataset")

    cleaned_data = data.copy()
    numerical_columns = cleaned_data.select_dtypes(include=np.number).columns

    for column in numerical_columns:
        cleaned_data[column] = cleaned_data[column].fillna(
            cleaned_data[column].median()
        )

    st.success("Missing numerical values filled using median values.")
    st.dataframe(cleaned_data.head(10), use_container_width=True)

    # Charging duration chart
    st.subheader("Charging Duration Distribution")

    st.bar_chart(
        cleaned_data["Charging Duration (hours)"].value_counts(
            bins=20
        ).sort_index()
    )

except FileNotFoundError:
    st.error(
        "Dataset not found. Place ev_charging_patterns.csv "
        "in the same folder as app.py."
    )
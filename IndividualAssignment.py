import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Setup ---
st.set_page_config(
    page_title="Student Mental Health Dashboard",
    page_icon=":material/school:",
    layout="wide"
)

# --- Header ---
st.header("Scientific Visualization", divider="gray")
st.subheader("Individual Assignment: Student Mental Health")

# --- Load CSV from GitHub ---
url = "https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Student_Mental_Health.csv"

@st.cache_data
def load_data(data_url):
    try:
        df = pd.read_csv(data_url)
        st.success("✅ DataFrame loaded successfully from GitHub!")
        return df
    except Exception as e:
        st.error(f"❌ Error while loading data: {e}")
        return pd.DataFrame()

# --- Load the Data ---
Student_Mental_Health_df = load_data(url)

# --- Display Data ---
if not Student_Mental_Health_df.empty:
    st.subheader("📊 Preview of Student Mental Health Dataset")
    st.dataframe(Student_Mental_Health_df.head())

    st.info(f"Dataset Shape: {Student_Mental_Health_df.shape[0]} rows × {Student_Mental_Health_df.shape[1]} columns")
else:
    st.warning("⚠️ No data to display. Please check the CSV link.")

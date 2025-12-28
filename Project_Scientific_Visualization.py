import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization : Project Group"
)

st.header("Scientific Visualization : Project Group", divider="gray")

st.subheader("🎯 Objective Statement")
st.write("""
The purpose of this visualization is to identify Demographic Differences in Mental Health Experiences among students
""")

st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Exploring Internet Use and Suicidality")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Student_Mental_Health.csv'

# Streamlit page setup
st.set_page_config(page_title="Exploring Internet Use and Suicidality Dashboard")

# Load data from GitHub
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/main/Student_Mental_Health.csv'

try:
    df = pd.read_csv(url)
    st.success("✅ Data loaded successfully from GitHub!")
    st.write("Dataset of Exploring Internet Use and Suicidality")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"An error occurred while loading data: {e}")
    st.stop()

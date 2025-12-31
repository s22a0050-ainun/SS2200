import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization : Project Group"
)

st.header("Scientific Visualization : Project Group", divider="gray")

st.subheader("🎯 Objective Statement")
st.write("""
The purpose of this visualization is to analyze the relationship between student's gender, 
academic courses and mental health conditions such as depression, anxiety and panic attacks. 
This can help in understanding how different factors contribute to mental well-being among students.
""")

st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Exploring Internet Use and Suicidality in Mental Health Populations")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Student_Mental_Health.csv'

# Streamlit page setup
st.set_page_config(page_title="Exploring Internet Use and Suicidality in Mental Health Populations Dashboard")

# Load data from GitHub
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/main/Student_Mental_Health.csv'

try:
    df = pd.read_csv(url)
    st.success("✅ Data loaded successfully from GitHub!")
    st.write("Dataset of Student Mental Health")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"An error occurred while loading data: {e}")
    st.stop()

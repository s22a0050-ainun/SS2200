import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization : Project Group"
)

st.header("Scientific Visualization : Project Group", divider="gray")

st.subheader("🎯 Objective Statement")
st.write("""
The purpose of this visualization is to identify and analyze the demographic differences in mental health experiences 
among students, with a particular focus on how factors such as gender, age, race and year of study influence student's 
perceptions and experiences of mental health challenges."
""")

st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Exploring Internet Use and Suicidality in Mental Health Populations")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Exploring%20Internet%20Use%20and%20Suicidality%20in%20Mental%20Health%20Populations.csv'

# Streamlit page setup
st.set_page_config(page_title="Exploring Internet Use and Suicidality in Mental Health Populations Dashboard")

# Load data from GitHub
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Exploring%20Internet%20Use%20and%20Suicidality%20in%20Mental%20Health%20Populations.csv'

try:
    df = pd.read_csv(url)
    st.success("✅ Data loaded successfully from GitHub!")
    st.write("Dataset of Student Mental Health")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"An error occurred while loading data: {e}")
    st.stop()

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Mental Health Dashboard", layout="wide"
                   
st.title("🎓 Student Mental Health Dashboard")
st.write("Explore and visualize data about student mental health.")

uploaded_file = st.file_uploader("https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Student_Mental_Health.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

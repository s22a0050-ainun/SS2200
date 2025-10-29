import streamlit as st
import pandas as pd

def student_mental_health():
    st.title("📊 Student Mental Health Dataset")

    url = "https://raw.githubusercontent.com/s22a0050-ainun/SS2200/main/Student_Mental_Health.csv"

    @st.cache_data
    def load_data(data_url):
        try:
            df = pd.read_csv(data_url)
            st.success("✅ Data loaded successfully from GitHub!")
            return df
        except Exception as e:
            st.error(f"❌ Error loading data: {e}")
            return pd.DataFrame()

    df = load_data(url)

    if not df.empty:
        st.subheader("Preview of Dataset")
        st.dataframe(df.head())

        st.info(f"Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")


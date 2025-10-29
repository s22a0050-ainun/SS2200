import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Student Mental Health")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Student_Mental_Health.csv'

# Streamlit page setup
st.set_page_config(page_title="Student Mental Health Dashboard")

st.title("🧠 Student Mental Health Data")

# Load data from GitHub
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/main/Student_Mental_Health.csv'

try:
    df = pd.read_csv(url)
    st.success("✅ Data loaded successfully from GitHub!")
    st.write("### Preview of Dataset")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"An error occurred while loading data: {e}")
    st.stop()



# Load your dataset
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/main/Student_Mental_Health.csv'
mental_df = pd.read_csv(url)

# Group data
cgpa_gender_counts = mental_df.groupby(['What is your CGPA?', 'Choose your gender']).size().reset_index(name='Count')

# Plotly grouped bar chart
fig = px.bar(
    cgpa_gender_counts,
    x='What is your CGPA?',
    y='Count',
    color='Choose your gender',
    barmode='group',
    title='Count of Students per CGPA Range by Gender'
)

# Show in Streamlit
st.plotly_chart(fig)

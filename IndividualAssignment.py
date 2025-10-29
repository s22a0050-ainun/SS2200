import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit page setup
st.set_page_config(page_title="Student Mental Health Dashboard")

st.title("🧠 Student Mental Health Data Visualization")

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

# --- Plotly Visualization Example ---
st.subheader("📊 Visualization Example")

# Dropdowns for column selection
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
categorical_cols = df.select_dtypes(exclude=['number']).columns.tolist()

x_col = st.selectbox("Select X-axis (categorical)", categorical_cols, index=0)
y_col = st.selectbox("Select Y-axis (numeric)", numeric_cols, index=0)

# Plot using Plotly
fig = px.box(df, x=x_col, y=y_col, color=x_col, title=f"{y_col} by {x_col}")
st.plotly_chart(fig, use_container_width=True)


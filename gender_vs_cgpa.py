import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Gender vs CGPA")

df = pd.read_csv("Student_Mental_Health.csv")

fig = px.box(df, x="Choose your gender", y="What is your CGPA?")
st.plotly_chart(fig)

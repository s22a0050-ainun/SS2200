import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Gender vs Mental Health Condition")

df = pd.read_csv("Student_Mental_Health.csv")

fig = px.histogram(df, x="Choose your gender", color="Do you have a mental health condition?")
st.plotly_chart(fig)



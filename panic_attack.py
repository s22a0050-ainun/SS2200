import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Panic Attack Among Students")

df = pd.read_csv("Student_Mental_Health.csv")

fig = px.pie(df, names="Do you have panic attacks?", title="Panic Attack Distribution")
st.plotly_chart(fig)

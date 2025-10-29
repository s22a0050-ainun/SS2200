import streamlit as st

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Student Mental Health")

url = 'https://github.com/s22a0050-ainun/SS2200/blob/main/Student_Mental_Health.csv'

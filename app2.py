import streamlit as st
from home import homepage
from student_data import student_mental_health

# Page setup
st.set_page_config(page_title="Student Mental Health Dashboard", layout="wide")

# Sidebar menu
st.sidebar.title("Menu")
page = st.sidebar.radio("Go to", ["Homepage", "Student Mental Health"])

# Navigation logic
if page == "Homepage":
    homepage()
elif page == "Student Mental Health":
    student_mental_health()

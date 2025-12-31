import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Student Mental Health",
    page_icon=":material/school:",
    layout="wide"
)

# Define pages
home = st.Page(
    "home.py",
    title="Home",
    icon=":material/home:",
    default=True
)

tutorial3 = st.Page(
    "tutorial3.py",
    title="Pencapaian Akademik Pelajar",
    icon=":material/school:"
)

individual = st.Page(
    "IndividualAssignment.py",
    title="Individual Assignment",
    icon=":material/menu_book:"
)

gender_mental = st.Page(
    "gender_vs_mentalhealth.py",
    title="Gender vs Mental Health",
    icon=":material/favorite:"
)

panic = st.Page(
    "panic_attack.py",
    title="Panic Attack",
    icon=":material/psychology:"
)

cgpa = st.Page(
    "gender_vs_cgpa.py",
    title="Gender vs CGPA",
    icon=":material/school:"
)

project = st.Page(
    "Project_Scientific_Visualization.py",
    title="Project Scientific Visualization",
    icon=":material/menu_book:"
)  

# Create navigation menu
pg = st.navigation({
    "Menu": [home, individual, gender_mental, panic, cgpa, project]
})

pg.run()

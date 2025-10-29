import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Student Dashboard",
    page_icon=":material/menu_book:",
    layout="wide"
)

# --- Define Pages ---
home = st.Page(
    'home.py',
    title='🏠 Homepage',
    default=True,
    icon=":material/home:"
)

tutorial3 = st.Page(
    'tutorial3.py',
    title='📘 Tutorial 3: Pencapaian Akademik Pelajar',
    icon=":material/school:"
)

mental_health = st.Page(
    'student_mental_health.py',
    title='🧠 Student Mental Health',
    icon=":material/psychology:"
)

# --- Navigation Menu ---
pg = st.navigation(
    {
        "Menu": [home, tutorial3, mental_health]
    }
)

# --- Run Navigation ---
pg.run()


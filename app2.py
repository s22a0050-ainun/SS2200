import streamlit as st

st.set_page_config(
    page_title="Student Mental Health Dashboard",
    page_icon=":material/school:",
    layout="wide"
)

home = st.Page('home.py', title='🏠 Homepage', icon=":material/home:", default=True)
visualise = st.Page('visualisation.py', title='📊 Student Mental Health', icon=":material/bar_chart:")

# Navigation setup
pg = st.navigation(
    {
        "Main Menu": [home, visualise]
    }
)

pg.run()


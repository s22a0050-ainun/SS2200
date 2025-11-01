import streamlit as st

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

# Create navigation menu
pg = st.navigation({
    "Menu": [home, individual, gender_mental, panic, cgpa]
})

pg.run()


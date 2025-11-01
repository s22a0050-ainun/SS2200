import streamlit as st

st.set_page_config(

    page_title="Student Mental Health"
)

visualise = st.Page('tutorial3.py', title='Pencapaian Akademik Pelajar', icon=":material/school:"),

visualise = st.Page('IndividualAssignment.py', title='Student Mental Health', icon=":material/school:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

# Define your pages
page1 = st.Page(
    "gender_vs_mentalhealth.py",
    title="Gender vs Mental Health Condition",
    icon=":material/favorite:"
)

page2 = st.Page(
    "panic_attack.py",
    title="Panic Attack Among Students",
    icon=":material/psychology:"
)

page3 = st.Page(
    "gender_vs_cgpa.py",
    title="Gender vs CGPA",
    icon=":material/school:"
)

# You can add a homepage if you want (optional)
home = st.Page(
    "home.py",
    title="Homepage",
    default=True,
    icon=":material/home:"
)

# Navigation
pg = st.navigation({
    "Main Menu": [home, IndividualAssignment, page1, page2, page3]
})

pg.run()

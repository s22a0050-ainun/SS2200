import streamlit as st

# Page configuration
st.set_page_config(page_title="Student Mental Health Dashboard")

# 🧭 Navigation setup
home = st.Page("home.py", title="Home", icon="🏠")
objectives = st.Page("objectives.py", title="Objectives", icon="🎯")
IndividualAssignment = st.Page("IndividualAssignment.py", title="Visualization (IndividualAssignment)", icon="📊")

# Navigation menu
pg = st.navigation([home, objectives, IndividualAssignment])
pg.run()

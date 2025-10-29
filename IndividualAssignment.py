import streamlit as st

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

st.set_page_config(
    page_title="Indivual Assignment"
)

visualise = st.Page('IndividualAssignment.py', title='Student Mental Health', icon=":material/school:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, visualise]
        }
    )

pg.run()

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Student Mental Health")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Student_Mental_Health.csv'

# Data Loading Function with Caching 
@st.cache_data
def load_data(data_url):
    try:
        data_frame = pd.read_csv(data_url)
        # st.success replaces print() for a styled success message
        st.success("DataFrame loaded successfully from URL! 🎉")
        return data_frame
    except Exception as e:
        # st.error replaces print() for error handling
        st.error(f"An error occurred while loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on failure

Student_Mental_Health_df_url = load_data(url)

# Streamlit Display
if not Student_Mental Health_df_url.empty:
    st.subheader("Preview of Student_Mental_Health")
    # st.dataframe() replaces the display() function, providing an interactive table
    st.dataframe(Student_Mental_Health_df_url.head())
    
    st.info(f"DataFrame Shape: {Student_Mental_Health_df_url.shape[0]} rows, {Student_Mental_Health_df_url.shape[1]} columns.")


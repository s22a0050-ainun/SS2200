import streamlit as st
import pandas as pd

# 1. Configuration (Optional but good practice)
st.set_page_config(layout="wide", page_title="Data Loading Example")

# 2. URL of the CSV file on GitHub
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/arts_faculty_data.csv'

# 3. Read the CSV file into a pandas DataFrame
st.title("GitHub Data Loader")

# Use st.cache_data to cache the DataFrame. 
# This is HIGHLY recommended in Streamlit to prevent reloading the data every time the app updates.
@st.cache_data
def load_data(data_url):
    try:
        data_frame = pd.read_csv(data_url)
        st.success("DataFrame loaded successfully from URL! 🎉")
        return data_frame
    except Exception as e:
        st.error(f"An error occurred while loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on failure

arts_df_from_url = load_data(url)

# 4. Streamlit Display (Replaces print and display)
if not arts_df_from_url.empty:
    st.subheader("Preview of Arts Faculty Data")
    # st.dataframe() displays the entire DataFrame interactively
    # We use .head() to only show the first few rows, matching your original code's intent
    st.dataframe(arts_df_from_url.head())

    # Optional: Displaying basic info
    st.info(f"The DataFrame has {arts_df_from_url.shape[0]} rows and {arts_df_from_url.shape[1]} columns.")

import streamlit as st
import pandas as pd
import plotly.express as px

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



# 1. --- Data Preparation (Using mock data for a runnable example) ---
# NOTE: In a real app, you would load your data here, for example:
# arts_df_url = pd.read_csv('your_data_url_here.csv') 

# MOCK DATA: Create a dummy DataFrame to simulate your 'arts_df_url'
data = {'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Other', 'Female', 'Male', 'Female', 'Female']}
arts_df_url = pd.DataFrame(data)

# Count the occurrences of each gender (Uses your exact logic)
gender_counts = arts_df_url['Gender'].value_counts()
st.title('Arts Faculty Data Visualization')

# 2. --- Plotly Chart Creation (Replaces Matplotlib code) ---

# Plotly Express is the easiest way to create the chart
fig = px.pie(
    # The 'names' are your labels (gender_counts.index)
    names=gender_counts.index,     
    # The 'values' are your counts (gender_counts.values)
    values=gender_counts.values,   
    title='Gender Distribution in Arts Faculty'
)

# Customize the traces for a better visual display (optional)
fig.update_traces(
    textposition='inside',        # Puts the label/percentage inside the slice
    textinfo='percent+label',     # Displays both percentage and the label
    hovertemplate="%{label}: %{value} (%{percent})<extra></extra>" # Custom hover text
)

# Adjust the layout for centered title
fig.update_layout(
    title_x=0.5
)

# 3. --- Streamlit Display (Replaces plt.show()) ---

# st.plotly_chart displays the interactive Plotly figure
st.plotly_chart(fig, use_container_width=True)

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




# 1. --- Data Preparation (Replaces the first two lines of your original code) ---
# Assuming 'arts_df' is loaded and processed somewhere above this.
# We will use a mock 'arts_df' and 'gender_counts' for a runnable example.

# MOCK DATA: Replace this section with your actual data loading and processing
data = {'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Other', 'Female', 'Male', 'Female', 'Female']}
arts_df = pd.DataFrame(data)

# Count the occurrences of each gender (Uses your exact logic)
gender_counts = arts_df['Gender'].value_counts()

# The gender_counts Series now has the indices (labels) and values (counts)

# 2. --- Plotly Chart Creation (Replaces the Matplotlib code) ---

# Plotly Express is the easiest way to create the chart
fig = px.pie(
    names=gender_counts.index,     # These are the labels (e.g., 'Female', 'Male')
    values=gender_counts.values,   # These are the counts
    title='Gender Distribution in Arts Faculty',
    hole=0.3                       # Optional: You can make it a donut chart
)

# Optional: Customize the appearance for a cleaner look
fig.update_traces(
    textposition='inside',         # Position the text inside the slices
    textinfo='percent+label'       # Show both percentage and label
)

# Optional: Adjust the title font and size
fig.update_layout(
    title_x=0.5,                   # Center the title
    title_font_size=20
)

# 3. --- Streamlit Display (Replaces plt.show()) ---

# Display the interactive Plotly chart in the Streamlit app
st.header("Arts Faculty Data Visualization")
st.plotly_chart(fig, use_container_width=True)

# You can also show the raw data
st.subheader("Gender Counts Data")
st.dataframe(gender_counts)

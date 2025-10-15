import streamlit as st
import pandas as pd
import plotly.express as px

# 1. --- Configuration and Data Source ---
st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Streamlit Data Loader from GitHub 📄")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/arts_faculty_data.csv'

# 2. --- Data Loading Function with Caching ---

# @st.cache_data is crucial. It tells Streamlit to run this function 
# and store the result (the DataFrame) in a local cache. 
# This prevents the app from re-downloading the file every time the user interacts with the app.
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

arts_df_url = load_data(url)

# 3. --- Streamlit Display ---
if not arts_df_url.empty:
    st.subheader("Preview of Arts Faculty Data")
    # st.dataframe() replaces the display() function, providing an interactive table
    st.dataframe(arts_df_url.head())
    
    st.info(f"DataFrame Shape: {arts_df_url.shape[0]} rows, {arts_df_url.shape[1]} columns.")



# --- Setup and Data Loading (Required for a runnable Streamlit app) ---
# NOTE: Assume 'arts_df_url' is loaded here, for example:
# arts_df_url = pd.read_csv('your_url_here.csv') 

# MOCK DATA: Using dummy data to make the example runnable
data = {'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female']}
arts_df_url = pd.DataFrame(data)

# Count the occurrences of each gender (Your original logic)
gender_counts = arts_df_url['Gender'].value_counts()

st.title('Gender Distribution Visualization 📊')

# 2. --- Plotly Chart Creation (Replaces Matplotlib) ---

# Use Plotly Express to create the interactive pie chart
fig = px.pie(
    # 'names' are the labels (e.g., 'Female', 'Male')
    names=gender_counts.index,     
    # 'values' are the counts 
    values=gender_counts.values,   
    title='Gender Distribution in Arts Faculty'
)

# Optional: Customize the appearance for better readability
fig.update_traces(
    textposition='inside',      # Position text inside slices
    textinfo='percent+label'    # Show both percentage and label
)

fig.update_layout(
    title_x=0.5 # Center the title
)

# 3. --- Streamlit Display (Replaces plt.show()) ---

# Display the interactive Plotly figure in the Streamlit app
st.plotly_chart(fig, use_container_width=True)


# Load dataset
df = pd.read_csv("arts_faculty_data.csv")

# Count academic years for Bachelor and Masters
bachelor = df['Bachelor  Academic Year in EU'].value_counts()
masters = df['Masters Academic Year in EU'].value_counts()

# Combine into one DataFrame
academic_years = pd.DataFrame({'Bachelor': bachelor, 'Masters': masters}).fillna(0)

# Create the plot
fig, ax = plt.subplots(figsize=(8,6))
academic_years.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e'], ax=ax)
ax.set_title('Academic Year Distribution by Degree Type')
ax.set_xlabel('Academic Year')
ax.set_ylabel('Number of Students')
plt.xticks(rotation=45)

# Display in Streamlit
st.pyplot(fig)

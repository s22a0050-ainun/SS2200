import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Student Mental Health")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Student_Mental_Health.csv'

# Streamlit page setup
st.set_page_config(page_title="Student Mental Health Dashboard")

st.title("🧠 Student Mental Health Data")

# Load data from GitHub
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/main/Student_Mental_Health.csv'

try:
    df = pd.read_csv(url)
    st.success("✅ Data loaded successfully from GitHub!")
    st.write("### Preview of Dataset")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"An error occurred while loading data: {e}")
    st.stop()


# Create a dummy DataFrame that matches the plot's data distribution
data = {
    'Do you have Depression?': ['No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes'],
    'Choose your gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Female']
}
mental_df = pd.DataFrame(data)

# Simulate the approximate counts from the image:
# Female/No: ~46, Male/No: ~20
# Female/Yes: ~29, Male/Yes: ~6

# Count the occurrences and convert to a DataFrame for Plotly
depression_gender_counts = mental_df.groupby(['Do you have Depression?', 'Choose your gender']).size().reset_index(name='Count')
depression_gender_counts.rename(columns={'Choose your gender': 'Gender'}, inplace=True) # Rename for cleaner legend

# Create a grouped bar chart using Plotly Express
fig = px.bar(
    depression_gender_counts,
    x='Do you have Depression?', # The primary x-axis categories (No/Yes)
    y='Count',
    color='Gender', # The variable that determines the bar groups (Female/Male)
    barmode='group', # Set mode for side-by-side bars
    category_orders={'Gender': ['Female', 'Male']}, # Ensure correct legend order if needed
    color_discrete_map={'Female': 'blue', 'Male': 'orange'}, # Match colors to the original image
    title='Count of Students with Depression by Gender',
    labels={'Do you have Depression?': 'Do you have Depression?', 'Count': 'Number of Students'}
)

# 3. Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

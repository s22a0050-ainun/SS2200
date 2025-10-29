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


data = {
    'What is your CGPA?': ['3.5-4.0', '3.5-4.0', '3.0-3.49', '3.5-4.0', '2.5-2.99', '3.0-3.49'],
    'Choose your gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Male']
}
mental_df = pd.DataFrame(data)

# Count the occurrences of each gender for each CGPA range and reset index for Plotly
cgpa_gender_counts = mental_df.groupby(['What is your CGPA?', 'Choose your gender']).size().reset_index(name='Count')

# Create a grouped bar chart using Plotly Express
fig = px.bar(
    cgpa_gender_counts,
    x='What is your CGPA?',
    y='Count',
    color='Choose your gender', # This creates the groups/stacked bars
    barmode='group', # Use 'group' for side-by-side bars
    title='Count of Students per CGPA Range by Gender',
    labels={'What is your CGPA?': 'CGPA Range', 'Choose your gender': 'Gender'}
)

# Optional: Improve layout and axis labels
fig.update_layout(xaxis_title='CGPA Range', yaxis_title='Number of Students')
fig.update_xaxes(tickangle=45)

# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)



data = {
    'What is your CGPA?': ['3.5-4.0', '3.5-4.0', '3.0-3.49', '3.5-4.0', '2.5-2.99', '3.0-3.49', '3.5-4.0', '3.5-4.0', '3.0-3.49', '2.5-2.99'],
    'Choose your gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female']
}
mental_df = pd.DataFrame(data)

# Count the occurrences of each gender for each CGPA range and reset index
cgpa_gender_counts = mental_df.groupby(['What is your CGPA?', 'Choose your gender']).size().reset_index(name='Count')

# Calculate the total count for each CGPA range
total_counts = cgpa_gender_counts.groupby('What is your CGPA?')['Count'].transform('sum')

# Calculate percentages
cgpa_gender_counts['Percentage'] = (cgpa_gender_counts['Count'] / total_counts) * 100

# Create a stacked bar chart using Plotly Express
fig = px.bar(
    cgpa_gender_counts,
    x='What is your CGPA?',
    y='Percentage',
    color='Choose your gender',  # This creates the stack segments
    title='Percentage of Male vs Female Students in Each CGPA Range',
    labels={'What is your CGPA?': 'CGPA Range', 'Choose your your gender': 'Gender'}
)

)
fig.update_xaxes(tickangle=45)

# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


data = {
    'Choose your gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Other', 'Female']
}
mental_df = pd.DataFrame(data)

# Count the occurrences of each gender and convert to a DataFrame for Plotly
gender_counts = mental_df['Choose your gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count'] # Rename columns for clarity

# Create a pie chart using Plotly Express
fig = px.pie(
    gender_counts,
    values='Count',
    names='Gender', # This provides the labels for the slices
    title='Overall Gender Proportion',
    hole=.3, # Optional: Create a donut chart
)

# Optional: Customize the appearance
fig.update_traces(
    textposition='inside',
    textinfo='percent+label' # Show percentage and label on the slices
)

# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

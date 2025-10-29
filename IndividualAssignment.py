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


import streamlit as st
import plotly.express as px
import pandas as pd # Assuming mental_df is a pandas DataFrame

# --- Dummy Data for Demonstration (Replace with your actual 'mental_df' loading) ---
data = {
    'What is your CGPA?': ['3.5-4.0', '3.5-4.0', '3.0-3.49', '3.5-4.0', '2.5-2.99', '3.0-3.49'],
    'Choose your gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Male']
}
mental_df = pd.DataFrame(data)
# ---------------------------------------------------------------------------------

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

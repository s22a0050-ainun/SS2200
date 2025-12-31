import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization : Project Group",
    layout="wide"
)

st.header("Scientific Visualization : Project Group", divider="gray")

st.subheader("🎯 Objective Statement")
st.write("""
The purpose of this visualization is to identify and analyze the demographic 
differences in mental health experiences among students, with a particular focus 
on how factors such as gender, age, race, and year of study influence students' 
perceptions and experiences of mental health challenges.
""")

st.title("Exploring Internet Use and Suicidality in Mental Health Populations")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Exploring%20Internet%20Use%20and%20Suicidality%20in%20Mental%20Health%20Populations.csv"
    return pd.read_csv(url)

try:
    df = load_data()
    st.success("✅ Data loaded successfully from GitHub!")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# Use df directly (no undefined filtered_data)
filtered_data = df.copy()


st.title("📊 Individual Visualizations : Ainun")

df = pd.read_csv("https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Exploring%20Internet%20Use%20and%20Suicidality%20in%20Mental%20Health%20Populations.csv")

# =================================================================
# 📉 CHART 1: GENDER DISTRIBUTION ACROSS COURSES
# =================================================================

import pandas as pd
import plotly.express as px
import streamlit as st

# Step 1: Filter only required columns (safe practice)
filtered_df = df[['Year_of_Study', 'Gender']].dropna().copy()

# Step 2: Count occurrences and convert to long format
year_gender_counts = (
    filtered_df.groupby(['Year_of_Study', 'Gender'])
    .size()
    .reset_index(name='Count')
)

# Step 3: Calculate percentage within each Year of Study
total_counts = year_gender_counts.groupby('Year_of_Study')['Count'].transform('sum')
year_gender_counts['Percentage'] = (year_gender_counts['Count'] / total_counts) * 100

# Step 4: Create stacked bar chart using Plotly
fig = px.bar(
    year_gender_counts,
    x='Year_of_Study',
    y='Percentage',
    color='Gender',  # stacked segments
    title='Stacked Bar Chart: Percentage of Gender Across Year of Study',
    labels={
        'Year_of_Study': 'Year of Study',
        'Percentage': 'Percentage of Respondents',
        'Gender': 'Gender'
    },
    barmode='stack'
)

# Step 5: Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
True)

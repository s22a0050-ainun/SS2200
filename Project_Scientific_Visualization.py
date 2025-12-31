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

import streamlit as st
import plotly.express as px

# Streamlit Title
st.title("Student Demographic Analysis")

# Creating the Plotly Grouped Bar Chart
# Note: px.histogram acts as a countplot when only an x-axis is provided
fig = px.histogram(
    df, 
    x='Year_of_Study', 
    color='Gender', 
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Set2,
    title='Gender Distribution Across Year of Study',
    labels={'Year_of_Study': 'Year of Study', 'count': 'Number of Respondents'}
)

# Optional: Update layout for better aesthetics
fig.update_layout(
    xaxis_title="Year of Study",
    yaxis_title="Number of Respondents",
    legend_title="Gender",
    xaxis={'categoryorder':'category ascending'} # Ensures years are in order
)

# Render the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import plotly.express as px
import pandas as pd

# 1. Prepare the data (Crosstab)
year_living_crosstab = pd.crosstab(df['Year_of_Study'], df['Current_Living_Situation'])

# 2. Create the Heatmap using Plotly Express
fig = px.imshow(
    year_living_crosstab,
    text_auto=True,                # Replaces annot=True (shows numbers)
    aspect="auto",                 # Adjusts the cell size
    color_continuous_scale='YlGnBu', # Matches your Seaborn cmap
    labels=dict(x="Living Situation", y="Year of Study", color="Count"),
    title='Heatmap: Year of Study vs Current Living Situation'
)

# 3. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import plotly.express as px
import pandas as pd

# 1. Prepare the crosstab data
gender_impact = pd.crosstab(df['Gender'], df['Social_Media_Positive_Impact_on_Wellbeing'])

# 2. Create the Stacked Bar Chart in Plotly
# We use .reset_index() because Plotly works best when columns are named
fig = px.bar(
    gender_impact, 
    barmode='stack',
    color_discrete_map={'Positive Impact': 'lightgreen', 'Negative Impact': 'salmon'},
    title='Gender vs. Social Media Impact on Wellbeing',
    labels={'value': 'Number of Respondents', 'Gender': 'Gender', 'Social_Media_Positive_Impact_on_Wellbeing': 'Impact Type'}
)

# 3. Refine Layout (Optional)
fig.update_layout(
    xaxis_title="Gender",
    yaxis_title="Number of Respondents",
    legend_title="Social Media Impact",
    xaxis={'categoryorder':'array', 'categoryarray':['Female', 'Male', 'Other']}
)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import plotly.express as px

# 1. Title for the specific section
st.subheader("Routine & Demographics")

# 2. Create the Plotly Grouped Bar Chart
fig = px.histogram(
    filtered_data, 
    x='Social_Media_Daily_Routine', 
    color='Race', 
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Set3,
    title='Race vs. Social Media as Part of Daily Routine',
    labels={
        'Social_Media_Daily_Routine': 'Daily Routine Integration', 
        'count': 'Number of Respondents',
        'Race': 'Race/Ethnicity'
    }
)

# 3. Clean up the axis and layout
fig.update_layout(
    xaxis_title="Social Media as Part of Daily Routine",
    yaxis_title="Number of Respondents",
    legend_title="Race",
    xaxis={'categoryorder': 'total descending'} # Useful for ordering by most common response
)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import plotly.express as px

# 1. Section Header
st.subheader("Health & Wellbeing Analysis")

# 2. Create the Plotly Grouped Bar Chart
fig = px.histogram(
    filtered_data, 
    x='Difficulty_Sleeping_University_Pressure', 
    color='Gender', 
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Set3,
    title='Gender vs. Difficulty Sleeping Due to University Pressure',
    labels={
        'Difficulty_Sleeping_University_Pressure': 'Difficulty Sleeping',
        'count': 'Number of Respondents',
        'Gender': 'Gender'
    }
)

# 3. Enhance the layout
fig.update_layout(
    xaxis_title="Difficulty Sleeping Due to University Pressure",
    yaxis_title="Number of Respondents",
    legend_title="Gender",
    xaxis={'categoryorder': 'category ascending'}, # Ensures "Low/Medium/High" or "Yes/No" order
    hovermode="x unified"                          # Shows all gender values in one tooltip
)

# 4. Render in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Individual Visualizations")

# Load the main DataFrame
df = pd.read_csv("Exploring Internet Use and Suicidality in Mental Health Populations.csv")

# Check column names and data types
st.write("Dataframe Columns:")
st.write(df.columns)

# Check for missing values
st.write("Missing Values in Data:")
st.write(df.isna().sum())

# Check the data types of columns
st.write("Data Types in Data:")
st.write(df.dtypes)

# Fix missing data or type issues
df = df.dropna(subset=['Year_of_Study', 'Gender', 'Social_Media_Positive_Impact_on_Wellbeing'])
df['Year_of_Study'] = df['Year_of_Study'].astype(str)
df['Gender'] = df['Gender'].astype(str)

# =================================================================
# 📉 VISUALIZATION 1: GENDER DISTRIBUTION ACROSS YEAR OF STUDY
# =================================================================
st.title("Group Bar Chart : Gender Distribution Across Year of Study")

# Group the data
gender_year_counts = df.groupby(['Year_of_Study', 'Gender']).size().reset_index(name='Count')

# Create the bar chart
fig1 = px.bar(
    gender_year_counts,
    x='Year_of_Study',
    y='Count',
    color='Gender',
    barmode='group',
    category_orders={"Year_of_Study": sorted(df['Year_of_Study'].unique())},  # Ensures years are in order
    color_discrete_sequence=px.colors.qualitative.Set2,
    title='Gender Distribution Across Year of Study',
    labels={'Year_of_Study': 'Year of Study', 'Count': 'Number of Respondents'}
)
fig1.update_layout(xaxis={'tickangle': 45})
st.plotly_chart(fig1, use_container_width=True)


# =================================================================
# 📉 VISUALIZATION 2: YEAR OF STUDY VS CURRENT LIVING SITUATION
# =================================================================
st.title("Heatmap : Year of Study vs Current Living Situation")

# Create the crosstab
year_living_crosstab = pd.crosstab(df['Year_of_Study'], df['Current_Living_Situation'])

# Create the Heatmap
fig2 = px.imshow(
    year_living_crosstab,
    text_auto=True,
    color_continuous_scale='YlGnBu',
    labels=dict(x="Living Situation", y="Year of Study", color="Count"),
    title='Heatmap: Year of Study vs Current Living Situation'
)
st.plotly_chart(fig2, use_container_width=True)


# =================================================================
# 📉 VISUALIZATION 3: GENDER VS SOCIAL MEDIA IMPACT ON WELLBEING
# =================================================================
st.title("Stacked Bar Chart : Gender vs Social Media Impact")

# Group the data (Explicitly summarizing for px.bar)
wellbeing_counts = df.groupby(['Gender', 'Social_Media_Positive_Impact_on_Wellbeing']).size().reset_index(name='Count')

# Rename categories for the legend if they are numeric (0/1)
wellbeing_counts['Social_Media_Positive_Impact_on_Wellbeing'] = wellbeing_counts['Social_Media_Positive_Impact_on_Wellbeing'].replace({0: 'Positive Impact', 1: 'Negative Impact'})

# Create Stacked Bar
fig3 = px.bar(
    wellbeing_counts,
    x='Gender',
    y='Count',
    color='Social_Media_Positive_Impact_on_Wellbeing',
    barmode='stack',
    color_discrete_map={'Positive Impact': 'lightgreen', 'Negative Impact': 'salmon'},
    title='Gender vs. Social Media Impact on Wellbeing',
    labels={'Social_Media_Positive_Impact_on_Wellbeing': 'Impact Type'}
)
st.plotly_chart(fig3, use_container_width=True)


# =================================================================
# 📉 VISUALIZATION 4: RACE VS SOCIAL MEDIA AS PART OF DAILY ROUTINE
# =================================================================
st.title("Group Bar Chart : Race vs Social Media Routine")

# Group the data
race_routine_counts = df.groupby(['Social_Media_Daily_Routine', 'Race']).size().reset_index(name='Count')

# Create Grouped Bar
fig4 = px.bar(
    race_routine_counts,
    x='Social_Media_Daily_Routine',
    y='Count',
    color='Race',
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Set3,
    title='Race vs. Social Media as Part of Daily Routine'
)
fig4.update_layout(xaxis={'tickangle': 45}, hovermode='x unified')
st.plotly_chart(fig4, use_container_width=True)


# =================================================================
# 📉 VISUALIZATION 5 : GENDER VS DIFFICULTY SLEEPING
# =================================================================
st.title("Bar Chart : Gender vs Difficulty Sleeping")

# Group the data
sleep_counts = df.groupby(['Difficulty_Sleeping_University_Pressure', 'Gender']).size().reset_index(name='Count')

# Create Grouped Bar
fig5 = px.bar(
    sleep_counts,
    x='Difficulty_Sleeping_University_Pressure',
    y='Count',
    color='Gender',
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Set3,
    title='Gender vs. Difficulty Sleeping Due to University Pressure'
)
fig5.update_layout(xaxis={'tickangle': 45}, hovermode='x unified')
st.plotly_chart(fig5, use_container_width=True)

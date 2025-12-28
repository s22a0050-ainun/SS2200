import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Individual Visualizations")

# Load the main DataFrame
df = pd.read_csv("Exploring Internet Use and Suicidality in Mental Health Populations.csv")

st.markdown("### 🎯 Objective ")
st.info("""
To identify demographic differences in mental health experiences
""")

# =================================================================
# 📉 VISUALIZATION 1: GENDER DISTRIBUTION ACROSS YEAR OF STUDY
# =================================================================

import plotly.express as px
import streamlit as st

# Assuming 'df' is your DataFrame
fig = px.bar(df, 
             x='Year_of_Study', 
             color='Gender', 
             title='Gender Distribution Across Year of Study', 
             labels={'Year_of_Study': 'Year of Study', 'Gender': 'Gender'},
            color_discrete_sequence=px.colors.qualitative.Set3)

# Update layout for better readability
fig.update_layout(
    xaxis_tickangle=45,
    xaxis_title='Year of Study',
    yaxis_title='Number of Respondents',
    legend_title='Gender'
)

# Display the plot in Streamlit
st.plotly_chart(fig)

# =================================================================
# 📉 VISUALIZATION 2: YEAR OF STUDY VS CURRENT LIVING SITUATION
# =================================================================

# Assuming 'df' is your DataFrame and pd.crosstab has been calculated
year_living_crosstab = pd.crosstab(df['Year_of_Study'], df['Current_Living_Situation'])

# Plotting Heatmap for Year of Study vs Current Living Situation using Plotly
fig = px.imshow(year_living_crosstab,
                labels={'x': 'Living Situation', 'y': 'Year of Study'},
                title='Heatmap: Year of Study vs Current Living Situation',
                color_continuous_scale='YlGnBu',
                text_auto=True)

# Update layout for better readability
fig.update_layout(
    xaxis_title='Living Situation',
    yaxis_title='Year of Study'
)

# Display the heatmap in Streamlit
st.plotly_chart(fig)

# =================================================================
# 📉 VISUALIZATION 3: GENDER VS SOCIAL MEDIA IMPACT ON WELLBEING
# =================================================================

# Assuming 'df' is your DataFrame and pd.crosstab has been calculated
gender_impact = pd.crosstab(df['Gender'], df['Social_Media_Positive_Impact_on_Wellbeing'])

# Create a stacked bar chart using Plotly
fig = go.Figure()

# Add traces for each category (Positive Impact, Negative Impact)
fig.add_trace(go.Bar(
    x=gender_impact.index,
    y=gender_impact[1],  # Assuming '1' corresponds to Positive Impact
    name='Positive Impact',
    marker_color='lightgreen'
))

fig.add_trace(go.Bar(
    x=gender_impact.index,
    y=gender_impact[0],  # Assuming '0' corresponds to Negative Impact
    name='Negative Impact',
    marker_color='salmon'
))

# Update layout
fig.update_layout(
    title='Gender vs. Social Media Impact on Wellbeing',
    xaxis_title='Gender',
    yaxis_title='Number of Respondents',
    xaxis=dict(
        tickmode='array',
        tickvals=[0, 1, 2],  # These are the indices for 'Female', 'Male', 'Other'
        ticktext=['Female', 'Male', 'Other']
    ),
    barmode='stack',  # Stacked bars
    legend_title='Social Media Impact',
    legend=dict(title='Social Media Impact', x=0, y=1)
)

# Display the chart in Streamlit
st.plotly_chart(fig)

# =================================================================
# 📉 VISUALIZATION 4: RACE VS SOCIAL MEDIA AS PART OF DAILY ROUTINE
# =================================================================

# Assuming 'filtered_data' is your DataFrame
fig = px.histogram(filtered_data, 
                   x='Social_Media_Daily_Routine', 
                   color='Race', 
                   title='Race vs. Social Media as Part of Daily Routine', 
                   labels={'Social_Media_Daily_Routine': 'Social Media as Part of Daily Routine'},
                   color_discrete_sequence=px.colors.qualitative.Set3)

# Update layout for better readability
fig.update_layout(
    xaxis_title='Social Media as Part of Daily Routine',
    yaxis_title='Number of Respondents',
    xaxis_tickangle=45,  # Rotate x-axis labels
    legend_title='Race'
)

# Display the plot in Streamlit
st.plotly_chart(fig)

# =================================================================
# 📉 VISUALIZATION 5 : GENDER VS DIFFICULTY SLEEPING DUE TO UNIVERSITY PRESSURE
# =================================================================

# Assuming 'filtered_data' is your DataFrame
fig = px.histogram(filtered_data, 
                   x='Difficulty_Sleeping_University_Pressure', 
                   color='Gender', 
                   title='Gender vs. Difficulty Sleeping Due to University Pressure', 
                   labels={'Difficulty_Sleeping_University_Pressure': 'Difficulty Sleeping Due to University Pressure'},
                   color_discrete_sequence=px.colors.qualitative.Set3)

# Update layout for better readability
fig.update_layout(
    xaxis_title='Difficulty Sleeping Due to University Pressure',
    yaxis_title='Number of Respondents',
    xaxis_tickangle=45,  # Rotate x-axis labels
    legend_title='Gender'
)

# Display the plot in Streamlit
st.plotly_chart(fig)

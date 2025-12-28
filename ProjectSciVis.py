import streamlit as st
import pandas as pd
import plotly.express as px

# Load the main DataFrame 
df = pd.read_csv("/content/Exploring Internet Use and Suicidality in Mental Health Populations.csv")

st.markdown("### 🎯 Objective")
st.info("""
To Identify Demographic Differences in Mental Health Experiences
""")

# Load data from GitHub 
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Exploring%20Internet%20Use%20and%20Suicidality%20in%20Mental%20Health%20Populations.csv'
data = pd.read_csv(url)

# Data Collection Page
st.title('Data Collection')
st.write("/content/Exploring Internet Use and Suicidality in Mental Health Populations.csv")
st.write(data.head())  # Show the first few rows of the dataset

import streamlit as st
import plotly.express as px

# Streamlit Title
st.title("Student Demographics Dashboard")

# Plotting Grouped Bar Chart for Gender vs Year of Study
# Plotly Express handles the "counting" automatically using the 'color' and 'barmode' arguments
fig = px.histogram(
    df, 
    x='Year_of_Study', 
    color='Gender', 
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Set2,
    title='Gender Distribution Across Year of Study',
    labels={'Year_of_Study': 'Year of Study', 'count': 'Number of Respondents'}
)

# Optional: Improve the layout
fig.update_layout(
    xaxis_title="Year of Study",
    yaxis_title="Number of Respondents",
    legend_title="Gender"
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)



import streamlit as st
import plotly.express as px
import pandas as pd

# 1. Create the crosstab (same as before)
year_living_crosstab = pd.crosstab(df['Year_of_Study'], df['Current_Living_Situation'])

# 2. Plotting Heatmap using Plotly Express
fig = px.imshow(
    year_living_crosstab,
    text_auto=True,                # Equivalent to annot=True
    color_continuous_scale='YlGnBu', # Matches your Seaborn cmap
    labels=dict(x="Living Situation", y="Year of Study", color="Count"),
    title='Heatmap: Year of Study vs Current Living Situation'
)

# 3. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)


import streamlit as st
import plotly.express as px

# Plotting Stacked Bar Chart
# Note: Using the original 'df' is often easier with Plotly Express
fig = px.histogram(
    df, 
    x='Gender', 
    color='Social_Media_Positive_Impact_on_Wellbeing',
    barmode='stack',
    color_discrete_map={
        'Positive Impact': 'lightgreen', 
        'Negative Impact': 'salmon'
    },
    title='Gender vs. Social Media Impact on Wellbeing',
    labels={'Social_Media_Positive_Impact_on_Wellbeing': 'Impact'}
)

# Refine the layout
fig.update_layout(
    xaxis_title="Gender",
    yaxis_title="Number of Respondents",
    legend_title="Social Media Impact"
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)


import streamlit as st
import plotly.express as px

# Plotting Grouped Bar Chart for Race vs Social Media Routine
fig = px.histogram(
    filtered_data, 
    x='Social_Media_Daily_Routine', 
    color='Race', 
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Set3,
    title='Race vs. Social Media as Part of Daily Routine',
    labels={
        'Social_Media_Daily_Routine': 'Social Media as Part of Daily Routine',
        'count': 'Number of Respondents',
        'Race': 'Race'
    }
)

# Refine the layout and axis appearance
fig.update_layout(
    xaxis_title="Social Media as Part of Daily Routine",
    yaxis_title="Number of Respondents",
    legend_title="Race",
    xaxis={'categoryorder':'total descending'} # Useful for organizing categorical data
)

# Display the interactive chart in the Streamlit app
st.plotly_chart(fig, use_container_width=True)


import streamlit as st
import plotly.express as px

# Plotting Grouped Bar Chart for Gender vs Difficulty Sleeping
fig = px.histogram(
    filtered_data, 
    x='Difficulty_Sleeping_University_Pressure', 
    color='Gender', 
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Set3,
    title='Gender vs. Difficulty Sleeping Due to University Pressure',
    category_orders={"Difficulty_Sleeping_University_Pressure": ["Yes", "No", "Sometimes"]} # Optional: force order
)

# Update layout for better readability
fig.update_layout(
    xaxis_title="Difficulty Sleeping Due to University Pressure",
    yaxis_title="Number of Respondents",
    legend_title="Gender",
    xaxis={'categoryorder':'total descending'} # Optional: sorts bars by size
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)



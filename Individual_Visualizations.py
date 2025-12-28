import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Individual Visualizations")

# Load the main DataFrame
df = pd.read_csv("Exploring Internet Use and Suicidality in Mental Health Populations.csv")

# Display columns to verify data
st.write(df.columns)

# Display missing data if needed for debugging
st.write(df.isna().sum())

st.markdown("### 🎯 Objective ")
st.info("""To identify demographic differences in mental health experiences.""")

# =================================================================
# 📉 VISUALIZATION 1: GENDER DISTRIBUTION ACROSS YEAR OF STUDY
# =================================================================

st.title("Group Bar Chart : Gender Distribution Across Year of Study")

# Plotting Grouped Bar Chart for Gender vs Year of Study
fig = px.histogram(
    df, 
    x='Year_of_Study',  # Ensure this column name is correct
    color='Gender', 
    barmode='group',
    category_orders={"Year_of_Study": sorted(df['Year_of_Study'].unique())},  # Ensures years are in order
    color_discrete_sequence=px.colors.qualitative.Set2,
    labels={'Year_of_Study': 'Year of Study', 'count': 'Number of Respondents'},
    title='Gender Distribution Across Year of Study'
)

fig.update_layout(
    xaxis_title="Year of Study",
    yaxis_title="Number of Respondents",
    legend_title="Gender",
    xaxis={'tickangle': 45}
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

# =================================================================
# 📉 VISUALIZATION 2: YEAR OF STUDY VS CURRENT LIVING SITUATION
# =================================================================

st.title("Heatmap : Year of Study vs Current Living Situation")

# Create the crosstab
year_living_crosstab = pd.crosstab(df['Year_of_Study'], df['Current_Living_Situation'])

# Create the Heatmap using Plotly Express
fig = px.imshow(
    year_living_crosstab,
    text_auto=True,                # Equivalent to annot=True
    color_continuous_scale='YlGnBu',  # Matches your cmap
    labels=dict(x="Living Situation", y="Year of Study", color="Count"),
    title='Heatmap: Year of Study vs Current Living Situation'
)

fig.update_layout(
    xaxis_title='Living Situation',
    yaxis_title='Year of Study',
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

# =================================================================
# 📉 VISUALIZATION 3: GENDER VS SOCIAL MEDIA IMPACT ON WELLBEING
# =================================================================

st.title("Stacked Bar Chart : Gender vs Social Media Impact on Wellbeing")

# Create the crosstab (keeps your original data structure)
gender_impact = pd.crosstab(df['Gender'], df['Social_Media_Positive_Impact_on_Wellbeing'])

# Reset index to make 'Gender' a column for Plotly
gender_impact_reset = gender_impact.reset_index()

# Create the Stacked Bar Chart
fig = px.bar(
    gender_impact_reset, 
    x='Gender', 
    y=gender_impact.columns,  # Plot all impact categories
    title='Gender vs. Social Media Impact on Wellbeing',
    labels={'value': 'Number of Respondents', 'variable': 'Social Media Impact'},
    color_discrete_sequence=['lightgreen', 'salmon'], # Matches your original colors
    template='plotly_white'
)

fig.update_layout(
    xaxis_title='Gender',
    yaxis_title='Number of Respondents',
    legend_title='Social Media Impact',
    barmode='stack'
)

# Change Legend Labels manually if needed (matches your 'labels' list)
new_names = {'0': 'Positive Impact', '1': 'Negative Impact'}
fig.for_each_trace(lambda t: t.update(name = new_names.get(t.name, t.name)))

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

# =================================================================
# 📉 VISUALIZATION 4: RACE VS SOCIAL MEDIA AS PART OF DAILY ROUTINE
# =================================================================

st.title("Group Bar Chart : Race vs Social Media as Part of Daily Routine")

# Creating the Grouped Bar Chart
fig = px.histogram(
    df,  # Replacing filtered_data with df
    x='Social_Media_Daily_Routine', 
    color='Race', 
    barmode='group',  # Side-by-side bars (like hue in Seaborn)
    color_discrete_sequence=px.colors.qualitative.Set3,
    title='Race vs. Social Media as Part of Daily Routine',
    labels={
        'Social_Media_Daily_Routine': 'Daily Routine Status',
        'count': 'Number of Respondents',
        'Race': 'Race/Ethnicity'
    }
)

fig.update_layout(
    xaxis_title='Social Media as Part of Daily Routine',
    yaxis_title='Number of Respondents',
    legend_title='Race',
    xaxis={'tickangle': 45},
    hovermode='x unified'  # Shows all race counts in one tooltip when hovering
)

# Display the plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# =================================================================
# 📉 VISUALIZATION 5 : GENDER VS DIFFICULTY SLEEPING DUE TO UNIVERSITY PRESSURE
# =================================================================

st.title("Bar Chart : Gender vs Difficulty Sleeping due to University Pressure")

# Create the grouped bar chart
fig = px.histogram(
    df,  # Replacing filtered_data with df
    x='Difficulty_Sleeping_University_Pressure', 
    color='Gender', 
    barmode='group',  # Ensures bars are side-by-side rather than stacked
    color_discrete_sequence=px.colors.qualitative.Set3,  # Matches your palette
    title='Gender vs. Difficulty Sleeping Due to University Pressure',
    labels={
        'Difficulty_Sleeping_University_Pressure': 'Difficulty Sleeping Score',
        'count': 'Number of Respondents'
    }
)

fig.update_layout(
    xaxis_title='Difficulty Sleeping Due to University Pressure',
    yaxis_title='Number of Respondents',
    legend_title='Gender',
    xaxis={'tickangle': 45},
    hovermode='x unified'
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

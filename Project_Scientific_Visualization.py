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

st.markdown("### 1️⃣ Gender Distribution Across Year of Study")

gender_year_counts = (
    df.groupby(['Year of Study', 'Gender'])
      .size()
      .reset_index(name='Count')
)

fig1 = px.bar(
    gender_year_counts,
    x='Year of Study',
    y='Count',
    color='Gender',
    barmode='group',
    title='Gender Distribution Across Year of Study',
    labels={
        'Year_of_Study': 'Year of Study',
        'Count': 'Number of Respondents'
    }
)

st.plotly_chart(fig1, use_container_width=True)


st.markdown("### 2️⃣ Year of Study vs Current Living Situation")

year_living_crosstab = pd.crosstab(
    df['Year of Study'],
    df['Current Living Situation']
)

fig2 = px.imshow(
    year_living_crosstab,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="YlGnBu",
    title="Heatmap: Year of Study vs Current Living Situation",
    labels=dict(
        x="Living Situation",
        y="Year of Study",
        color="Count"
    )
)

st.plotly_chart(fig2, use_container_width=True)


st.markdown("### 3️⃣ Gender vs Social Media Impact on Wellbeing")

gender_impact = (
    df.groupby(['Gender', 'Social_Media_Positive_Impact_on_Wellbeing'])
      .size()
      .reset_index(name='Count')
)

fig3 = px.bar(
    gender_impact,
    x='Gender',
    y='Count',
    color='Social_Media_Positive_Impact_on_Wellbeing',
    title='Gender vs Social Media Impact on Wellbeing',
    labels={
        'Gender': 'Gender',
        'Count': 'Number of Respondents',
        'Social_Media_Positive_Impact_on_Wellbeing': 'Social Media Impact'
    }
)

st.plotly_chart(fig3, use_container_width=True)


st.markdown("### 4️⃣ Race vs Social Media as Part of Daily Routine")

race_social_counts = (
    df.groupby(['Social_Media_Daily_Routine', 'Race'])
      .size()
      .reset_index(name='Count')
)

fig4 = px.bar(
    race_social_counts,
    x='Social_Media_Daily_Routine',
    y='Count',
    color='Race',
    barmode='group',
    title='Race vs Social Media as Part of Daily Routine',
    labels={
        'Social_Media_Daily_Routine': 'Social Media as Part of Daily Routine',
        'Count': 'Number of Respondents'
    }
)

st.plotly_chart(fig4, use_container_width=True)


st.markdown("### 5️⃣ Gender vs Difficulty Sleeping Due to University Pressure")

sleep_gender_counts = (
    df.groupby(['Difficulty_Sleeping_University_Pressure', 'Gender'])
      .size()
      .reset_index(name='Count')
)

fig5 = px.bar(
    sleep_gender_counts,
    x='Difficulty_Sleeping_University_Pressure',
    y='Count',
    color='Gender',
    barmode='group',
    title='Gender vs Difficulty Sleeping Due to University Pressure',
    labels={
        'Difficulty_Sleeping_University_Pressure': 'Difficulty Sleeping Due to University Pressure',
        'Count': 'Number of Respondents'
    }
)

st.plotly_chart(fig5, use_container_width=True)


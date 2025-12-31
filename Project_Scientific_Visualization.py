import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration (ONLY ONCE)
# --------------------------------------------------
st.set_page_config(
    page_title="Scientific Visualization : Project Group",
    layout="wide"
)

# --------------------------------------------------
# Header & Objective
# --------------------------------------------------
st.header("Scientific Visualization : Project Group", divider="gray")

st.subheader("🎯 Objective Statement")
st.write("""
The purpose of this visualization is to identify and analyze the demographic 
differences in mental health experiences among students, with a particular focus 
on how factors such as gender, age, race, and year of study influence students' 
perceptions and experiences of mental health challenges.
""")

st.title("Exploring Internet Use and Suicidality in Mental Health Populations")

# --------------------------------------------------
# Load Data from GitHub
# --------------------------------------------------
url = "https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Exploring%20Internet%20Use%20and%20Suicidality%20in%20Mental%20Health%20Populations.csv"

try:
    df = pd.read_csv(url)
    st.success("✅ Data loaded successfully from GitHub!")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

st.markdown("---")
st.title("📊 Individual Visualizations")

# --------------------------------------------------
# 1. Gender vs Year of Study (Grouped Bar Chart)
# --------------------------------------------------
st.subheader("1️⃣ Gender Distribution Across Year of Study")

fig1 = px.bar(
    df,
    x="Year_of_Study",
    color="Gender",
    title="Gender Distribution Across Year of Study",
    labels={
        "Year_of_Study": "Year of Study",
        "count": "Number of Respondents"
    },
    barmode="group"
)

fig1.update_layout(xaxis_tickangle=45)
st.plotly_chart(fig1, use_container_width=True)

# --------------------------------------------------
# 2. Heatmap: Year of Study vs Current Living Situation
# --------------------------------------------------
st.subheader("2️⃣ Heatmap: Year of Study vs Current Living Situation")

year_living_crosstab = pd.crosstab(
    df["Year_of_Study"],
    df["Current_Living_Situation"]
)

fig2 = px.imshow(
    year_living_crosstab,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="YlGnBu",
    title="Heatmap: Year of Study vs Current Living Situation"
)

fig2.update_layout(
    xaxis_title="Living Situation",
    yaxis_title="Year of Study"
)

st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# 3. Gender vs Social Media Impact on Wellbeing (Stacked Bar)
# --------------------------------------------------
st.subheader("3️⃣ Gender vs Social Media Impact on Wellbeing")

gender_impact = pd.crosstab(
    df["Gender"],
    df["Social_Media_Positive_Impact_on_Wellbeing"]
).reset_index()

gender_impact_melted = gender_impact.melt(
    id_vars="Gender",
    var_name="Social Media Impact",
    value_name="Number of Respondents"
)

fig3 = px.bar(
    gender_impact_melted,
    x="Gender",
    y="Number of Respondents",
    color="Social Media Impact",
    title="Gender vs Social Media Impact on Wellbeing",
    barmode="stack"
)

st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------------
# 4. Race vs Social Media as Part of Daily Routine
# --------------------------------------------------
st.subheader("4️⃣ Race vs Social Media as Part of Daily Routine")

fig4 = px.bar(
    df,
    x="Social_Media_Daily_Routine",
    color="Race",
    title="Race vs Social Media as Part of Daily Routine",
    labels={
        "Social_Media_Daily_Routine": "Social Media as Part of Daily Routine"
    }
)

fig4.update_layout(xaxis_tickangle=45)
st.plotly_chart(fig4, use_container_width=True)

# --------------------------------------------------
# 5. Gender vs Difficulty Sleeping Due to University Pressure
# --------------------------------------------------
st.subheader("5️⃣ Gender vs Difficulty Sleeping Due to University Pressure")

fig5 = px.bar(
    df,
    x="Difficulty_Sleeping_University_Pressure",
    color="Gender",
    title="Gender vs Difficulty Sleeping Due to University Pressure",
    labels={
        "Difficulty_Sleeping_University_Pressure": 
        "Difficulty Sleeping Due to University Pressure"
    }
)

fig5.update_layout(xaxis_tickangle=45)
st.plotly_chart(fig5, use_container_width=True)

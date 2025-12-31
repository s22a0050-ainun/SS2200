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

# ==================================================
# 🔒 SAFETY FIX: Standardise column names
# ==================================================

# Make a copy to avoid modifying original data
df = df.copy()

# Clean column names: strip spaces
df.columns = df.columns.str.strip()

# Rename ONLY if the original column exists
rename_map = {
    "Year of Study": "Year_of_Study",
    "Current Living Situation": "Current_Living_Situation",
    "Social Media Positive Impact on Wellbeing": "Social_Media_Positive_Impact_on_Wellbeing",
    "Social Media Daily Routine": "Social_Media_Daily_Routine",
    "Difficulty Sleeping Due to University Pressure": "Difficulty_Sleeping_University_Pressure"
}

df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns}, inplace=True)

# Safe alias
filtered_data = df.copy()

# Debug (can remove later)
st.write("✅ Columns detected:", df.columns.tolist())


st.subheader("1️⃣ Gender Distribution Across Year of Study")

fig1 = px.histogram(
    df,
    x="Year_of_Study",
    color="Gender",
    barmode="group",
    title="Gender Distribution Across Year of Study"
)

fig1.update_layout(
    xaxis_title="Year of Study",
    yaxis_title="Number of Respondents",
    legend_title="Gender"
)

st.plotly_chart(fig1, use_container_width=True)

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
    barmode="stack",
    title="Gender vs Social Media Impact on Wellbeing"
)

st.plotly_chart(fig3, use_container_width=True)


st.subheader("4️⃣ Race vs Social Media as Part of Daily Routine")

fig4 = px.histogram(
    filtered_data,
    x="Social_Media_Daily_Routine",
    color="Race",
    barmode="group",
    title="Race vs Social Media as Part of Daily Routine"
)

fig4.update_layout(
    xaxis_title="Social Media as Part of Daily Routine",
    yaxis_title="Number of Respondents",
    legend_title="Race",
    xaxis_tickangle=45
)

st.plotly_chart(fig4, use_container_width=True)


st.subheader("5️⃣ Gender vs Difficulty Sleeping Due to University Pressure")

fig5 = px.histogram(
    filtered_data,
    x="Difficulty_Sleeping_University_Pressure",
    color="Gender",
    barmode="group",
    title="Gender vs Difficulty Sleeping Due to University Pressure"
)

fig5.update_layout(
    xaxis_title="Difficulty Sleeping Due to University Pressure",
    yaxis_title="Number of Respondents",
    legend_title="Gender",
    xaxis_tickangle=45
)

st.plotly_chart(fig5, use_container_width=True)




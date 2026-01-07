import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Scientific Visualization",
    layout="wide"
)

st.title("Scientific Visualization : Project Group")

# --------------------------------------------------
# OBJECTIVE
# --------------------------------------------------
st.subheader("🎯 Objective Statement")
st.write("""
This visualization aims to identify demographic differences in mental health 
experiences among students, focusing on how internet use, stress, and social 
media engagement relate to wellbeing.
""")

# --------------------------------------------------
# DATA LOADING
# --------------------------------------------------
@st.cache_data
def load_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQnrGG72xRS-qLoiM2zon4eP8t5XMiO5MhoLUEe2jJer0G5EzodiU4e0NOmx_ssmCwZf-AnbQXhBbTM/pub?gid=1791189796&single=true&output=csv"
    return pd.read_csv(url)

df = load_data()

# ✅ TOTAL RESPONDENTS (RAW DATA)
total_respondents = len(df)  # = 101

# --------------------------------------------------
# DATA TRANSFORMATION
# --------------------------------------------------

# Likert scale mapping
likert_map = {
    "Strongly disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly agree": 5
}

df["Stress_Index_Num"] = df[
    "I have difficulty sleeping due to university-related pressure. / Saya sukar tidur kerana tekanan berkaitan universiti."
].map(likert_map)

df["SM_Routine_Num"] = df[
    "Using social media is an important part of my daily routine. / Menggunakan media sosial adalah bahagian penting dalam rutin harian saya."
].map(likert_map)

# --------------------------------------------------
# DATA FILTERING (ONLY FOR ANALYSIS)
# --------------------------------------------------
filtered_data = df[
    ["Gender / Jantina:",
     "Year of Study / Tahun Belajar:",
     "Race / Bangsa:",
     "Stress_Index_Num",
     "SM_Routine_Num"]
].dropna()

# --------------------------------------------------
# SUMMARY METRICS (BOXED)
# --------------------------------------------------
st.subheader("📊 Summary Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Respondents", total_respondents)

with col2:
    st.metric("Avg Stress Index", round(filtered_data["Stress_Index_Num"].mean(), 2))

with col3:
    st.metric("Avg Social Media Usage", round(filtered_data["SM_Routine_Num"].mean(), 2))

with col4:
    high_usage_pct = (filtered_data["SM_Routine_Num"] >= 4).mean() * 100
    st.metric("High Usage (%)", f"{high_usage_pct:.1f}%")

# ==================================================
# VISUALIZATIONS
# ==================================================
col1, col2 = st.columns(2)

# --------------------------------------------------
# COLUMN 1
# --------------------------------------------------
with col1:

    st.subheader("Gender Distribution Across Year of Study")
    st.metric("Total Respondents", len(filtered_data))

    fig1 = px.histogram(
        filtered_data,
        x="Year_of_Study",
        color="Gender",
        barmode="group"
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("""
**Interpretation:** Year 1 students form the largest group of respondents. 
Female students consistently outnumber male students across most years.
""")

    st.subheader("Gender vs Social Media Impact")

    fig2 = px.histogram(
        filtered_data,
        x="Gender",
        color="Social_Media_Positive_Impact_on_Wellbeing",
        barmode="stack"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Gender vs Difficulty Sleeping")

    fig3 = px.histogram(
        filtered_data,
        x="Difficulty_Sleeping_University_Pressure",
        color="Gender",
        barmode="group"
    )
    st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------------
# COLUMN 2
# --------------------------------------------------
with col2:

    st.subheader("Year of Study vs Living Situation")

    heatmap_data = pd.crosstab(
        filtered_data['Year_of_Study'],
        filtered_data['Current_Living_Situation']
    )

    fig4 = px.imshow(
        heatmap_data,
        text_auto=True,
        color_continuous_scale="YlGnBu"
    )
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("Race vs Social Media Routine")

    fig5 = px.histogram(
        filtered_data,
        x="Social_Media_Daily_Routine",
        color="Race",
        barmode="group"
    )
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("Employment Status Distribution")

    fig6 = px.pie(
        filtered_data,
        names="Employment_Status"
    )
    st.plotly_chart(fig6, use_container_width=True)

# ==================================================
# SUMMARY
# ==================================================
st.markdown("""
### 📌 Summary

The visualizations show clear demographic differences in students’ mental health experiences. Female students report stronger impacts from academic pressure and social media, while senior students 
tend to live more independently off-campus. Most respondents are full-time students, highlighting academic demands as a key factor affecting wellbeing.
""")

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

# ==================================================
# DATA TRANSFORMATION
# ==================================================
df["Gender_Num"] = df["Gender"].map({
    "Female": 0,
    "Male": 1,
    "Other": 2
})

df["Year_Num"] = df["Year_of_Study"].str.extract(r"(\d)").astype(float)

df["Race_Num"] = df["Race"].map({
    "Malay": 0,
    "Chinese": 1,
    "Indian": 2,
    "Other": 3,
    "Others": 3
})

# ==================================================
# DATA FILTERING (NO RESPONDENTS REMOVED)
# ==================================================
st.sidebar.header("🔍 Data Filtering")

gender_filter = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].dropna().unique(),
    default=df["Gender"].dropna().unique()
)

year_filter = st.sidebar.multiselect(
    "Year of Study",
    options=df["Year_of_Study"].dropna().unique(),
    default=df["Year_of_Study"].dropna().unique()
)

race_filter = st.sidebar.multiselect(
    "Race",
    options=df["Race"].dropna().unique(),
    default=df["Race"].dropna().unique()
)

filtered_data = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Year_of_Study"].isin(year_filter)) &
    (df["Race"].isin(race_filter))
]

# ==================================================
# SUMMARY METRIC BOXES (SHOWS 101)
# ==================================================
st.subheader("📊 Summary Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Respondents", len(filtered_data))

with col2:
    st.metric(
        "Majority Gender",
        filtered_data["Gender"].mode(dropna=True)[0]
    )

with col3:
    st.metric(
        "Most Common Race",
        filtered_data["Race"].mode(dropna=True)[0]
    )

with col4:
    st.metric(
        "Dominant Year of Study",
        filtered_data["Year_of_Study"].mode(dropna=True)[0]
    )
    
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

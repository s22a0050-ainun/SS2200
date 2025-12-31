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

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Load Data
@st.cache_data
def load_data():
    # Load the uploaded CSV
    df = pd.read_csv('Exploring Internet Use and Suicidality in Mental Health Populations.csv')
    
    # Mapping raw long column names to the short names used in your logic
    column_mapping = {
        'Gender / Jantina:': 'Gender',
        'Year of Study / Tahun Belajar:': 'Year_of_Study',
        'Current living situation / Keadaan hidup sekarang:': 'Current_Living_Situation',
        'Race / Bangsa:': 'Race',
        'Social media has a generally positive impact on my wellbeing. / Media sosial secara amnya mempunyai kesan positif terhadap kesejahteraan saya.': 'Social_Media_Positive_Impact_on_Wellbeing',
        'I have difficulty sleeping due to university-related pressure. / Saya sukar tidur kerana tekanan berkaitan universiti.': 'Difficulty_Sleeping_University_Pressure',
        'Using social media is an important part of my daily routine. / Menggunakan media sosial adalah bahagian penting dalam rutin harian saya.': 'Social_Media_Daily_Routine'
    }
    df = df.rename(columns=column_mapping)
    return df

df = load_data()

# 2. Transformation Logic
# Cleaning strings to match your map (e.g., "Off-campus (rental)" -> "Off-campus")
df['Current_Living_Situation'] = df['Current_Living_Situation'].str.replace(r' \(.*\)', '', regex=True)
df['Race'] = df['Race'].replace('Others', 'Other')

# Applying your specific numeric mapping
df['Gender_Num'] = df['Gender'].map({'Female': 0, 'Male': 1, 'Other': 2}).fillna(2)
df['Year_of_Study_Num'] = df['Year_of_Study'].map({'Year 1': 1, 'Year 2': 2, 'Year 3': 3, 'Year 4': 4, 'Year 5': 5}).fillna(0)
df['Current_Living_Situation_Num'] = df['Current_Living_Situation'].map({
    'With family': 0, 'On-campus': 1, 'Off-campus': 2, 'Other': 3
}).fillna(3)

# Note: If your raw data is Likert (1-5), you may need to group them into 'Yes'/'No' first.
# Here we apply your requested string-to-numeric mapping:
df['Impact_Num'] = df['Social_Media_Positive_Impact_on_Wellbeing'].map({'Positive impact': 1, 'Negative impact': 0, 'No impact': 2}).fillna(2)
df['Sleep_Pressure_Num'] = df['Difficulty_Sleeping_University_Pressure'].map({'Yes': 1, 'No': 0}).fillna(0)
df['Race_Num'] = df['Race'].map({'Malay': 0, 'Chinese': 1, 'Indian': 2, 'Other': 3}).fillna(3)
df['Routine_Num'] = df['Social_Media_Daily_Routine'].map({'Important part of daily routine': 1, 'Not important part of daily routine': 0}).fillna(0)

# Create filtered_data for specific plots
filtered_data = df[['Gender', 'Year_of_Study', 'Current_Living_Situation', 
                    'Social_Media_Positive_Impact_on_Wellbeing', 'Difficulty_Sleeping_University_Pressure', 
                    'Race', 'Social_Media_Daily_Routine']].dropna()

# --- VISUALIZATIONS ---


# =================================================================
# 📉 VISUALIZATION 1 : GENDER DISTRIBUTION ACROSS COURSES
# =================================================================

st.header("Data Visualizations")

# 1. Gender Distribution Across Year of Study
st.subheader("1. Gender Distribution Across Year of Study")
fig1 = px.histogram(df, x='Year_of_Study', color='Gender', barmode='group',
                   title='Gender Distribution Across Year of Study',
                   color_discrete_sequence=px.colors.qualitative.Set2)
fig1.update_layout(xaxis_title='Year of Study', yaxis_title='Number of Respondents')
st.plotly_chart(fig1)

# =================================================================
# 📉 VISUALIZATION 2 : GENDER DISTRIBUTION ACROSS COURSES
# =================================================================

# 2. Year of Study vs Current Living Situation (Heatmap)
st.subheader("2. Heatmap: Year of Study vs Current Living Situation")
year_living_crosstab = pd.crosstab(df['Year_of_Study'], df['Current_Living_Situation'])
fig2 = px.imshow(year_living_crosstab, text_auto=True, color_continuous_scale='YlGnBu',
                title='Heatmap: Year of Study vs Current Living Situation')
fig2.update_layout(xaxis_title='Living Situation', yaxis_title='Year of Study')
st.plotly_chart(fig2)

# =================================================================
# 📉 VISUALIZATION 3 : GENDER DISTRIBUTION ACROSS COURSES
# =================================================================

# 3. Gender vs. Social Media Impact on Wellbeing (Stacked Bar)
st.subheader("3. Gender vs. Social Media Impact on Wellbeing")
# For Plotly, it's easier to use the original categorical columns for labels
fig3 = px.histogram(df, x='Gender', color='Social_Media_Positive_Impact_on_Wellbeing', 
                   title='Gender vs. Social Media Impact on Wellbeing',
                   barmode='stack', color_discrete_map={'Positive impact': 'lightgreen', 'Negative impact': 'salmon'})
fig3.update_layout(yaxis_title='Number of Respondents')
st.plotly_chart(fig3)

# =================================================================
# 📉 VISUALIZATION 4 : GENDER DISTRIBUTION ACROSS COURSES
# =================================================================

# 4. Race vs. Social Media as Part of Daily Routine
st.subheader("4. Race vs. Social Media as Part of Daily Routine")
fig4 = px.histogram(filtered_data, x='Social_Media_Daily_Routine', color='Race', 
                   barmode='group', title='Race vs. Social Media as Part of Daily Routine',
                   color_discrete_sequence=px.colors.qualitative.Set3)
fig4.update_layout(xaxis_title='Social Media as Part of Daily Routine', yaxis_title='Number of Respondents')
st.plotly_chart(fig4)

# =================================================================
# 📉 VISUALIZATION 5 : GENDER DISTRIBUTION ACROSS COURSES
# =================================================================

# 5. Gender vs. Difficulty Sleeping Due to University Pressure
st.subheader("5. Gender vs. Difficulty Sleeping Due to University Pressure")
fig5 = px.histogram(filtered_data, x='Difficulty_Sleeping_University_Pressure', color='Gender', 
                   barmode='group', title='Gender vs. Difficulty Sleeping Due to University Pressure',
                   color_discrete_sequence=px.colors.qualitative.Set3)
fig5.update_layout(xaxis_title='Difficulty Sleeping Due to University Pressure', yaxis_title='Number of Respondents')
st.plotly_chart(fig5)

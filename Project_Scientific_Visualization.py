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

import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. DATA LOADING & MAPPING ---
@st.cache_data
def load_data():
    # Load the uploaded CSV
    df = pd.read_csv('Exploring Internet Use and Suicidality in Mental Health Populations.csv')

# --- 2. DATA FILTERING ---
    
    # Mapping raw long column names to the short names used in your logic
    column_mapping = {
        'Gender / Jantina:': 'Gender',
        'Year of Study / Tahun Belajar:': 'Year_of_Study',
        'Current living situation / Keadaan hidup sekarang:': 'Current_Living_Situation',
        'Employment Status / Status Pekerjaan:': 'Employment_Status',
        'Race / Bangsa:': 'Race',
        'Social media has a generally positive impact on my wellbeing. / Media sosial secara amnya mempunyai kesan positif terhadap kesejahteraan saya.': 'Social_Media_Positive_Impact_on_Wellbeing',
        'I have difficulty sleeping due to university-related pressure. / Saya sukar tidur kerana tekanan berkaitan universiti.': 'Difficulty_Sleeping_University_Pressure',
        'Using social media is an important part of my daily routine. / Menggunakan media sosial adalah bahagian penting dalam rutin harian saya.': 'Social_Media_Daily_Routine'
    }
    df = df.rename(columns=column_mapping)
    return df

df_original = load_data()
df = df_original.copy()

# --- 3. DATA TRANSFORMATION  ---

# Mapping Gender
gender_map = {0: 'Female', 1: 'Male', 2: 'Other'}
df['Gender_Num'] = df['Gender'].map({'Female': 0, 'Male': 1, 'Other': 2}).fillna(2)

# Mapping Year of Study
year_map = {1: 'Year 1', 2: 'Year 2', 3: 'Year 3', 4: 'Year 4', 5: 'Year 5', 0: 'Unknown'}
df['Year_of_Study_Num'] = df['Year_of_Study'].map({'Year 1': 1, 'Year 2': 2, 'Year 3': 3, 'Year 4': 4, 'Year 5': 5}).fillna(0)

# Mapping Living Situation
living_map = {0: 'With family', 1: 'On-campus', 2: 'Off-campus', 3: 'Other'}
df['Current_Living_Situation_Num'] = df['Current_Living_Situation'].map({
    'With family': 0, 'On-campus': 1, 'Off-campus (rental)': 2, 'Off-campus': 2, 'Other': 3
}).fillna(3)

# Mapping Employment (Clean string variations from CSV)
df['Employment_Status_Num'] = df['Employment_Status'].map({
    'Full-time student': 3,
    'In paid employment (including part-time, self-employed)': 2,
    'Internship': 1,
    'Unemployed': 0
}).fillna(2)

# Mapping Impact
impact_map = {1: 'Positive Impact', 0: 'Negative Impact', 2: 'No impact'}
df['Social_Media_Positive_Impact_on_Wellbeing_Num'] = df['Social_Media_Positive_Impact_on_Wellbeing'].map({
    'Positive impact': 1, 'Negative impact': 0, 'No impact': 2
}).fillna(2)

# Mapping Race
race_map = {0: 'Malay', 1: 'Chinese', 2: 'Indian', 3: 'Other'}
df['Race_Num'] = df['Race'].map({'Malay': 0, 'Chinese': 1, 'Indian': 2, 'Others': 3, 'Other': 3}).fillna(3)

# Filtered data subset
filtered_data = df[['Gender', 'Year_of_Study', 'Current_Living_Situation', 
                    'Social_Media_Positive_Impact_on_Wellbeing', 
                    'Difficulty_Sleeping_University_Pressure', 'Race', 
                    'Social_Media_Daily_Routine', 'Employment_Status']].dropna()

# --- 4. INDIVIDUAL VISUALIZATIONS ( AINUN ) ---

# Layout into two columns
col1, col2 = st.columns(2)

with col1:
    # VISUALIZATION 1 : Gender Distribution Across Year of Study (Group Bar Chart)
    st.subheader("Gender Distribution Across Year of Study")
    fig1 = px.histogram(df, x='Year_of_Study', color='Gender', barmode='group',
                       category_orders={"Year_of_Study": ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]},
                       color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig1, use_container_width=True)

    # VISUALIZATION 2 : Gender vs. Social Media Impact (Stacked Bar Chart)
    st.subheader("Gender vs. Social Media Impact")
    fig3 = px.histogram(df, x='Gender', color='Social_Media_Positive_Impact_on_Wellbeing', 
                       barmode='stack', 
                       color_discrete_map={'Positive impact': 'lightgreen', 'Negative impact': 'salmon', 'No impact': 'grey'})
    st.plotly_chart(fig3, use_container_width=True)

    # VISUALIZATION 3 : Gender vs. Difficulty Sleeping (Bar Chart)
    st.subheader("Gender vs. Difficulty Sleeping")
    fig5 = px.histogram(filtered_data, x='Difficulty_Sleeping_University_Pressure', color='Gender', 
                       barmode='group', color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    # VISUALIZATION 4 : Year of Study vs Current Living Situation (Heatmap)
    st.subheader("Heatmap: Year vs Living Situation")
    year_living_xtab = pd.crosstab(df['Year_of_Study'], df['Current_Living_Situation'])
    fig2 = px.imshow(year_living_xtab, text_auto=True, color_continuous_scale='YlGnBu')
    st.plotly_chart(fig2, use_container_width=True)

    # VISUALIZATION 5 : Race vs. Social Media Routine (Group Bar Chart)
    st.subheader("Race vs. Social Media Routine")
    fig4 = px.histogram(filtered_data, x='Social_Media_Daily_Routine', color='Race', 
                       barmode='group', color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig4, use_container_width=True)

    # VISUALIZATION 6 : Employment Status (Pie Chart)
    st.subheader("Employment Status Distribution")
    fig6 = px.pie(df, names='Employment_Status', title='', 
                 color_discrete_sequence=px.colors.qualitative.Paired)
    fig6.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig6, use_container_width=True)

st.divider()
st.write("### Data Preview")
st.dataframe(df[['Gender', 'Year_of_Study', 'Race', 'Employment_Status']].head(10))

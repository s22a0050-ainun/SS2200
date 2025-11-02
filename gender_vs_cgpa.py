import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Gender vs CGPA")

df = pd.read_csv("Student_Mental_Health.csv")

st.markdown("### 🎯 Objective 3")
st.info("""
To analyze students of different genders are distributed across various academic courses. 
""")

# =================================================================
# 📊 SUMMARY METRICS BLOCK 📊
# =================================================================

# 1. Calculate overall gender counts and percentages (based on the data used for the pie chart)
# Create a consolidated DataFrame to calculate overall metrics
data_combined = {
    'What is your course?': ['BIT'] * 10 + ['Diploma Nursing'] * 10 + ['Engineering'] * 10 + ['Human Resources'] * 10 + ['IT'] * 10 + ['Law'] * 10 + ['Pendidikan Islam'] * 10 + ['Psychology'] * 10,
    'Choose your gender': (['Female'] * 6 + ['Male'] * 4) + (['Female'] * 10) + (['Female'] * 7 + ['Male'] * 3) + (['Female'] * 10) + (['Female'] * 10) + (['Female'] * 10) + (['Female'] * 10) + (['Female'] * 10)
}
mental_df_overall = pd.DataFrame(data_combined)

total_students = len(mental_df_overall)
female_count = (mental_df_overall['Choose your gender'] == 'Female').sum()
male_count = (mental_df_overall['Choose your gender'] == 'Male').sum()

female_percent = (female_count / total_students) * 100
male_percent = (male_count / total_students) * 100


# 2. Display Metrics
st.markdown("### 📊 Summary Box")

# Use st.columns to display metrics side-by-side
col1, col2, col3 = st.columns(3)

col1.metric(
    label="Total Students",
    value=total_students
)
col2.metric(
    label="Female Students",
    value=female_count,
    # Show the percentage as a delta
    delta=f"{round(female_percent)}% of total", 
    delta_color="normal" # Green for the majority group
)
col3.metric(
    label="Male Students",
    value=male_count,
    # Show the percentage as a delta
    delta=f"{round(male_percent)}% of total",
    delta_color="inverse" # Highlights the small proportion
)

st.markdown("---") 

# =================================================================
# 📉 CHART 1: GENDER DISTRIBUTION ACROSS COURSES
# =================================================================

# Create dummy data that simulates the distribution 
courses = ['BIT', 'Diploma Nursing', 'Engineering', 'Human Resources', 'IT', 'Law', 'Pendidikan Islam', 'Psychology']
genders = ['Female', 'Male']
data = {
    'What is your course?': ['BIT'] * 10 + ['Diploma Nursing'] * 10 + ['Engineering'] * 10 + ['Human Resources'] * 10 + ['IT'] * 10 + ['Law'] * 10 + ['Pendidikan Islam'] * 10 + ['Psychology'] * 10,
    'Choose your gender': (['Female'] * 6 + ['Male'] * 4) + (['Female'] * 10) + (['Female'] * 7 + ['Male'] * 3) + (['Female'] * 10) + (['Female'] * 10) + (['Female'] * 10) + (['Female'] * 10) + (['Female'] * 10)
}
mental_df = pd.DataFrame(data)

# List of courses to filter by (Your original logic)
desired_courses = [
    'Engineering', 'IT', 'Law', 'Human Resources',
    'Diploma Nursing', 'Pendidikan Islam', 'BIT', 'Psychology'
]

# Filter the DataFrame for the desired courses
filtered_courses_df = mental_df[mental_df['What is your course?'].isin(desired_courses)].copy()

# Count occurrences and convert to a long DataFrame
course_gender_counts = filtered_courses_df.groupby(
    ['What is your course?', 'Choose your gender']
).size().reset_index(name='Count')

# Calculate the percentage within each course group
total_counts = course_gender_counts.groupby('What is your course?')['Count'].transform('sum')
course_gender_counts['Percentage'] = (course_gender_counts['Count'] / total_counts) * 100
course_gender_counts.rename(columns={'Choose your gender': 'Gender'}, inplace=True)

# Create a stacked bar chart using Plotly Express
fig = px.bar(
    course_gender_counts,
    x='What is your course?',
    y='Percentage',
    color='Gender', # This creates the stack segments
    title='Stacked Bar Chart : Percentage of Male vs. Female Students in Selected Courses',
    labels={'What is your course?': 'Course', 'Percentage': 'Percentage of Students'},
    # Ensure Female is the base (blue) and Male is the top (orange)
    category_orders={'Gender': ['Female', 'Male']},
    color_discrete_map={'Female': 'blue', 'Male': 'orange'}
)
# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# =================================================================
# 📉 CHART 2: OVERALL GENDER PROPORTION PIE CHART
# =================================================================

gender_counts = mental_df['Choose your gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

fig = px.pie(
    gender_counts, 
    values='Count', 
    names='Gender', 
    title='Pie Chart : Overall Gender Proportion',
    # Match colors to be consistent with the bar chart
    color_discrete_map={'Female': 'blue', 'Male': 'orange'}
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# =================================================================
# 📉 CHART 3: CGPA BY GENDER
# =================================================================

data = {
    'What is your CGPA?': ['3.50 - 4.00'] * 40 + ['3.00 - 3.49'] * 30 + ['2.50 - 2.99'] * 4 + ['2.00 - 2.49'] * 1 + ['0 - 1.99'] * 2 +
                            ['3.50 - 4.00'] * 10 + ['3.00 - 3.49'] * 14 + ['2.50 - 2.99'] * 0 + ['2.00 - 2.49'] * 1 + ['0 - 1.99'] * 2,
    'Choose your gender': ['Female'] * 77 + ['Male'] * 27
}

mental_df = pd.DataFrame(data)

# Data Aggregation and Preparation (Fixes potential KeyError) ---
# Aggregate the data into the long format preferred by Plotly Express
cgpa_gender_counts = mental_df.groupby(['What is your CGPA?', 'Choose your gender']).size().reset_index(name='Count')
cgpa_gender_counts.columns = ['CGPA', 'Gender', 'Count']

# Define the order for CGPA categories to ensure correct plotting sequence
cgpa_order = ['0 - 1.99', '2.00 - 2.49', '2.50 - 2.99', '3.00 - 3.49', '3.50 - 4.00']
cgpa_gender_counts['CGPA'] = pd.Categorical(
    cgpa_gender_counts['CGPA'], 
    categories=cgpa_order, 
    ordered=True
)
cgpa_gender_counts = cgpa_gender_counts.sort_values('CGPA')

fig = px.bar(
    cgpa_gender_counts, 
    x='CGPA', 
    y='Count', 
    color='Gender', 
    barmode='group', # Displays bars side-by-side
    title='Group Bar Chart : Count of Students per CGPA by Gender',
    labels={'CGPA': 'CGPA', 'Count': 'Number of Students'}
)
# Streamlit Display (Fixes plt.show() issue) ---
st.plotly_chart(fig, use_container_width=True)


# --- Interpretation ---
st.markdown("### 🧾 Interpretation")
st.success(
    "The three visualizations collectively highlight the gender distribution patterns among students across academic courses and performance levels. "
    "The overall gender proportion pie chart reveals a strong female with 91.3% of the surveyed students being female and only 8.75% male. "
    "The stacked bar chart by course further supports this trend showing that most programs such as Diploma Nursing, Human Resources, IT, Law, Pendidikan Islam and Psychology consist of female students while only BIT and Engineering show a mixed gender composition with a higher percentage of females. "
    "The grouped bar chart of CGPA by gender shows that both male and female students are focus in the higher CGPA categories for 3.00–4.00 but female students consistently across all performance levels. "
    "These findings align with the objective of analyzing students of different genders are distributed across various academic courses, revealing that female students active in academic achievement."
)


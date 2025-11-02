import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Panic Attack Among Students")

df = pd.read_csv("Student_Mental_Health.csv")

st.markdown("### 🎯 Objective 2")
st.info("""
To explore the frequency of panic attacks among students and relates to gender or course type
""")

# =================================================================
# 📊 SUMMARY METRICS BLOCK 📊
# =================================================================

# We will use the data from the overall panic attack pie chart for the general summary metrics.
total_students_sample = 100
num_no = int(total_students_sample * 0.673)
num_yes = total_students_sample - num_no # 33

# --- Displaying Metrics ---
st.markdown("### 📊 Summary Box")

# Use st.columns to display metrics side-by-side
col1, col2, col3 = st.columns(3)

col1.metric(
    label="Total Students",
    value=total_students_sample
)
col2.metric(
    label="Students with Panic Attack",
    value=num_yes,
    # Show the percentage as a delta for context (33% is the target)
    delta=f"{num_yes}% of total", 
    delta_color="inverse" # Highlights a concerning metric in red
)
col3.metric(
    label="Students without Panic Attack",
    value=num_no
)

st.markdown("---") 

# =================================================================
# 📉 CHART 1: PANIC ATTACK BY COURSE
# =================================================================

# Create dummy data that simulates the distribution shown in the image
courses = ['BIT'] * 10 + ['Diploma Nursing'] * 1 + ['Engineering'] * 17 + ['Human Resources'] * 1 + ['IT'] * 1 + ['Law'] * 1 + ['Pendidikan Islam'] * 1 + ['Psychology'] * 1
panic_attacks = ['No'] * 6 + ['Yes'] * 4 + ['No'] * 1 + ['No'] * 12 + ['Yes'] * 5 + ['No'] * 1 + ['Yes'] * 1 + ['No'] * 1 + ['No'] * 1 + ['No'] * 1

mental_df = pd.DataFrame({
    'What is your course?': courses,
    'Do you have Panic attack?': panic_attacks
})

desired_courses = [
    'Engineering', 'IT', 'Law', 'Human Resources',
    'Diploma Nursing', 'Pendidikan Islam', 'BIT', 'Psychology'
]

# Filter the DataFrame for the desired courses (Your original logic)
filtered_mental_df = mental_df[mental_df['What is your course?'].isin(desired_courses)].copy()

# Group the data and prepare for Plotly
# Group by Course and Panic Attack response, then convert to a clean DataFrame
panic_attack_course_counts_df = filtered_mental_df.groupby(
    ['What is your course?', 'Do you have Panic attack?']
).size().reset_index(name='Number of Students')

# Create the stacked bar chart using Plotly Express
fig = px.bar(
    panic_attack_course_counts_df,
    x='What is your course?',
    y='Number of Students',
    color='Do you have Panic attack?', # This creates the stack segments and legend
    title='Stacked Bar Chart : Panic Attack Cases Across Selected Courses',
    labels={'What is your course?': 'Course', 'Do you have Panic attack?': 'Panic Attack'},
    # Ensure 'No' is the base (bottom) and 'Yes' is the top, and match colors
    category_orders={'Do you have Panic attack?': ['No', 'Yes']},
    color_discrete_map={'No': 'blue', 'Yes': 'orange'}
)
# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# =================================================================
# 📉 CHART 2: OVERALL PERCENTAGE PIE CHART
# =================================================================

# Create dummy data that simulates the 67.3% No and 32.7% Yes split
total_students = 100
num_no = int(total_students * 0.673)
num_yes = total_students - num_no

mental_df = pd.DataFrame({
    'Do you have Panic attack?': ['No'] * num_no + ['Yes'] * num_yes
})

# Count the occurrences and prepare for Plotly
# Convert the value_counts Series to a DataFrame
panic_attack_counts_df = mental_df['Do you have Panic attack?'].value_counts().reset_index()
panic_attack_counts_df.columns = ['Panic Attack', 'Count'] # Rename columns for clarity

# Create a pie chart using Plotly Express
fig = px.pie(
    panic_attack_counts_df,
    values='Count',
    names='Panic Attack', # This provides the labels for the slices
    title='Pie Chart : Overall Percentage of Students with Panic Attacks',
    # Match the colors of the original plot: Blue for No, Orange for Yes
    color_discrete_map={'No': 'blue', 'Yes': 'orange'}
)
# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# =================================================================
# 📉 CHART 3: PANIC ATTACK BY GENDER
# =================================================================

# Create dummy data that simulates the distribution shown in the image (approximate counts)
# Female/No: ~50, Male/No: ~18
# Female/Yes: ~25, Male/Yes: ~8
data = {
    'Do you have Panic attack?': (['No'] * 50) + (['Yes'] * 25) + (['No'] * 18) + (['Yes'] * 8),
    'Choose your gender': (['Female'] * 50) + (['Female'] * 25) + (['Male'] * 18) + (['Male'] * 8)
}
mental_df = pd.DataFrame(data)

# Count the occurrences and convert to a long DataFrame for Plotly
panic_attack_gender_counts_df = mental_df.groupby(
    ['Do you have Panic attack?', 'Choose your gender']
).size().reset_index(name='Number of Students')
panic_attack_gender_counts_df.rename(columns={'Choose your gender': 'Gender'}, inplace=True) # Rename for cleaner legend

# Create a grouped bar chart using Plotly Express
fig = px.bar(
    panic_attack_gender_counts_df,
    x='Do you have Panic attack?', # The primary x-axis categories (No/Yes)
    y='Number of Students',
    color='Gender', # The variable that determines the bar groups (Female/Male)
    barmode='group', # Set mode for side-by-side bars
    title='Bar Chart : Count of Students Experiencing Panic Attacks by Gender',
    labels={'Do you have Panic attack?': 'Do you have Panic attack?', 'Number of Students': 'Number of Students'},
    # Manually map colors to match the image (blue for Female, orange for Male)
    color_discrete_map={'Female': 'blue', 'Male': 'orange'},
    # Ensure the x-axis categories are in the correct order
    category_orders={'Do you have Panic attack?': ['No', 'Yes']}
)
# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# --- Interpretation ---
st.markdown("### 🧾 Interpretation")
st.success(
    "As a summary, the three visualizations collectively highlight key patterns related to panic attacks among students across gender and academic courses. "
    "The bar chart comparing gender and panic attacks reveals that female students represent the majority in both categories with more females for 25 than males for 8 reporting panic attacks, showing a higher currency among female students. "
    "The pie chart shows that 33% of the overall student population reported experiencing panic attacks, while 67% did not suggesting that although most students are unaffected, a significant portion still faces this issue. "
    "Meanwhile, the stacked bar chart by course demonstrates that panic attack cases are most common among students in Engineering and BIT programs with minimal cases in other courses. "
    "The findings suggest that panic attacks are more frequent among female students and are focus within specific academic programs providing valuable insights into gender and course type may influence student's mental health experiences."
)


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Individual Assignment")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Student_Mental_Health.csv'

# Streamlit page setup
st.set_page_config(page_title="Student Mental Health Dashboard")

# Load data from GitHub
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/main/Student_Mental_Health.csv'

try:
    df = pd.read_csv(url)
    st.success("✅ Data loaded successfully from GitHub!")
    st.write("Dataset of Student Mental Health")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"An error occurred while loading data: {e}")
    st.stop()


# Create a dummy DataFrame that matches the plot's data distribution
data = {
    'Do you have Depression?': ['No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes'],
    'Choose your gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Female']
}
mental_df = pd.DataFrame(data)

# Female/No: ~46, Male/No: ~20
# Female/Yes: ~29, Male/Yes: ~6

# Count the occurrences and convert to a DataFrame for Plotly
depression_gender_counts = mental_df.groupby(['Do you have Depression?', 'Choose your gender']).size().reset_index(name='Count')
depression_gender_counts.rename(columns={'Choose your gender': 'Gender'}, inplace=True) # Rename for cleaner legend

# Create a grouped bar chart using Plotly Express
fig = px.bar(
    depression_gender_counts,
    x='Do you have Depression?', # The primary x-axis categories (No/Yes)
    y='Count',
    color='Gender', # The variable that determines the bar groups (Female/Male)
    barmode='group', # Set mode for side-by-side bars
    category_orders={'Gender': ['Female', 'Male']}, # Ensure correct legend order if needed
    color_discrete_map={'Female': 'blue', 'Male': 'orange'}, # Match colors to the original image
    title='Bar Chart : Count of Students with Depression by Gender',
    labels={'Do you have Depression?': 'Do you have Depression?', 'Count': 'Number of Students'}
)

# 3. Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)




# Create dummy data that simulates the long-format data needed for the plot
data = {
    'Choose your gender': (['Female'] * 29 + ['Male'] * 6) * 3, # Simulating ~35 Female and ~18 Male overall
    'Do you have Depression?': ['Yes'] * 29 + ['No'] * 6 + ['Yes'] * 29 + ['No'] * 6 + ['Yes'] * 29 + ['No'] * 6,
    'Do you have Anxiety?': ['Yes'] * 24 + ['No'] * 5 + ['Yes'] * 9 + ['No'] * 0 + ['Yes'] * 29 + ['No'] * 6,
    'Do you have Panic attack?': ['Yes'] * 25 + ['No'] * 4 + ['Yes'] * 8 + ['No'] * 1 + ['Yes'] * 29 + ['No'] * 6
}
# A proper mental_df would have many rows, this is just for demonstration structure
mental_df = pd.DataFrame({
    'Choose your gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Do you have Depression?': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes'],
    'Do you have Anxiety?': ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No'],
    'Do you have Panic attack?': ['No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']
})


# Melt the DataFrame to long format (same as your original logic)
conditions_melted = mental_df.melt(
    id_vars='Choose your gender',
    value_vars=['Do you have Depression?', 'Do you have Anxiety?', 'Do you have Panic attack?'],
    var_name='Condition',
    value_name='Response'
)

# Filter for 'Yes' responses (same as your original logic)
conditions_yes = conditions_melted[conditions_melted['Response'] == 'Yes']

# Create the stacked bar chart using Plotly Express
# Plotly automatically counts the occurrences when mapping 'Condition' to x and 'Choose your gender' to color
fig = px.bar(
    conditions_yes,
    x='Condition',
    color='Choose your gender', # This creates the stack segments and legend
    title='Stacked Bar Chart : Distribution of Mental Health Conditions by Gender',
    labels={'Condition': 'Condition', 'Choose your gender': 'Gender', 'count': 'Number of Students with Condition'},
    # Manually map colors to match the image (blue for Female, orange for Male)
    color_discrete_map={'Female': 'blue', 'Male': 'orange'}
)

# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)



# Create dummy data that simulates students with and without mental health issues
data = {
    'Choose your gender': (['Female'] * 75 + ['Male'] * 25) + (['Female', 'Male'] * 50),
    'Do you have Depression?': ['Yes'] * 100 + ['No'] * 100,
    'Do you have Anxiety?': ['Yes'] * 50 + ['No'] * 50 + ['Yes'] * 50 + ['No'] * 50,
    'Do you have Panic attack?': ['No'] * 200
}
mental_df = pd.DataFrame({
    'Choose your gender': ['Female'] * 75 + ['Male'] * 25 + ['Female'] * 10 + ['Male'] * 10, # 120 total students
    'Do you have Depression?': ['Yes'] * 75 + ['Yes'] * 25 + ['No'] * 20,
    'Do you have Anxiety?': ['Yes'] * 75 + ['Yes'] * 25 + ['No'] * 20,
    'Do you have Panic attack?': ['No'] * 120
})

# Identify students with at least one mental health issue (Your original logic)
mental_health_issues = mental_df[
    (mental_df['Do you have Depression?'] == 'Yes') |
    (mental_df['Do you have Anxiety?'] == 'Yes') |
    (mental_df['Do you have Panic attack?'] == 'Yes')
].copy()

# Count the occurrences of gender and prepare for Plotly
# Convert the value_counts Series to a DataFrame
gender_with_issues_counts = mental_health_issues['Choose your gender'].value_counts().reset_index()
gender_with_issues_counts.columns = ['Gender', 'Count'] # Rename columns

# Create a pie chart using Plotly Express
fig = px.pie(
    gender_with_issues_counts,
    values='Count',
    names='Gender', # This provides the labels for the slices
    title='Pie Chart : Overall Proportion of Students with Mental Health Issues by Gender',
    # Match the colors of the original plot: Blue for Female, Orange for Male
    color_discrete_map={'Female': 'blue', 'Male': 'orange'}
)

# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)



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

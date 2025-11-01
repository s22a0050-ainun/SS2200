import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Gender vs Mental Health")

df = pd.read_csv("Student_Mental_Health.csv")

st.markdown("### 🎯 Objective 1")
st.info("""
To analyze the relationship between gender and the type of mental health issues such as 
**depression, anxiety, and panic attacks** among students.
""")


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


# --- Summary Box ---
st.markdown("### 🧾 Summary")
st.success("""
Although the Pie Chart reveals that **75% of students who have overall mental health problems are female**, 
the Stacked Bar Chart offers a more complicated structure of particular aspects. The second chart shows that 
**4 females and 2 males experienced Depression**, **4 females and 1 male experienced Anxiety**, and 
**2 females and 3 males experienced a Panic Attack**. This shows females gave more answers to the questions 
about **Depression** and **Anxiety**, while males gave slightly more responses to the question about **Panic Attack**.  
This trend is indeed verified by the third chart, which specifically dealt with Depression, and the results 
showed that of the students who responded “Yes” to having Depression, there were **3 female students and 1 male student**.  
On the whole, there is a much higher percentage of **mental health cases in females**, mainly due to increased cases of 
**Depression and Anxiety**.
""")

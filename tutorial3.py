import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Scientific Visualization", layout="wide")
st.title("Student Survey")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/arts_faculty_data.csv'

col1, col2, col3, col4 = st.columns(4)
   
col1.metric(label="PLO 2", value=f"3.3", help="PLO 2: Cognitive Skill", border=True)
col2.metric(label="PLO 3", value=f"3.5", help="PLO 3: Digital Skill", border=True)
col3.metric(label="PLO 4", value=f"4.0", help="PLO 4: Interpersonal Skill", border=True)
col4.metric(label="PLO 5", value=f"4.3", help="PLO 5: Communication Skill", border=True)

def load_data(data_url):
    try:
        data_frame = pd.read_csv(data_url)
        st.success
        return data_frame
    except Exception as e:
        # st.error replaces print() for error handling
        st.error(f"An error occurred while loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on failure

arts_df_url = load_data(url)

if not arts_df_url.empty:
    st.subheader("Preview of Arts Faculty Data")
    # st.dataframe() replaces the display() function, providing an interactive table
    st.dataframe(arts_df_url.head())
    
    st.info(f"DataFrame Shape: {arts_df_url.shape[0]} rows, {arts_df_url.shape[1]} columns.")


data = {'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female']}
arts_df_url = pd.DataFrame(data)

# Count the occurrences of each gender 
gender_counts = arts_df_url['Gender'].value_counts()

st.title('Visualization Tutorial 3 📊')


# Use Plotly Express to create the interactive pie chart
fig = px.pie(
    # 'names' are the labels (e.g., 'Female', 'Male')
    names=gender_counts.index,     
    # 'values' are the counts 
    values=gender_counts.values,   
    title='Gender Distribution in Arts Faculty'
)


fig.update_traces(
    textposition='inside',      # Position text inside slices
    textinfo='percent+label'    # Show both percentage and label
)

fig.update_layout(
    title_x=0.5 # Center the title
)



# Display the interactive Plotly figure in the Streamlit app
st.plotly_chart(fig, use_container_width=True)


data = {'Gender': ['Male', 'Female', 'Male', 'Female'],
        'S.S.C (GPA)': [4.5, 4.8, 4.2, 4.9],
        'H.S.C (GPA)': [4.0, 4.7, 3.8, 4.6]}
df = pd.DataFrame(data)



avg_gpa = df.groupby('Gender')[['S.S.C (GPA)', 'H.S.C (GPA)']].mean().reset_index()

avg_gpa_long = pd.melt(avg_gpa,
                       id_vars='Gender',
                       value_vars=['S.S.C (GPA)', 'H.S.C (GPA)'],
                       var_name='Exam Level',
                       value_name='Average GPA')

fig = px.bar(avg_gpa_long,
             x='Gender',
             y='Average GPA',
             color='Exam Level',
             barmode='group', # Group bars side-by-side
             title='Average S.S.C and H.S.C GPA by Gender',
             labels={'Average GPA': 'Average GPA', 'Gender': 'Gender'})

fig.update_layout(xaxis_tickangle=0)

st.plotly_chart(fig, use_container_width=True)


data = {'Did you ever attend a Coaching center?': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No']}
arts_df = pd.DataFrame(data)


coaching_counts = arts_df['Did you ever attend a Coaching center?'].value_counts().reset_index()
coaching_counts.columns = ['Response', 'Count']

fig = px.pie(coaching_counts,
             values='Count',
             names='Response',
             title='Did students attend a Coaching Center?')

fig.update_traces(textposition='inside', textinfo='percent+label')

# 3. Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# Create DataFrame based on the graph values 
data = {
    'Arts Program': ['B.A. in English', 'M. A. in ELT (1.4 Year)', 'M. A. in ELT (2 Year)', 'M.A. in English'],
    # Approximate values read from the graph
    'Number of Students': [69, 13, 3, 2]
}
df_arts = pd.DataFrame(data)

# Create the Plotly Bar Chart
fig = px.bar(df_arts,
             x='Arts Program',
             y='Number of Students',
             title='Distribution of Arts Programs',
             color_discrete_sequence=['#1f77b4'])

fig.update_layout(xaxis_tickangle=45)

# Display the chart in Streamlit ---
st.plotly_chart(fig, use_container_width=True)


data = {'H.S.C or Equivalent study medium': ['Bangla', 'English', 'Madrasa', 'Bangla', 'Bangla', 'Bangla', 'Bangla']}
arts_df = pd.DataFrame(data)


## 🥧 Streamlit Plotly Pie Chart

# Count the occurrences and format the data for Plotly
study_medium_counts = arts_df['H.S.C or Equivalent study medium'].value_counts().reset_index()
study_medium_counts.columns = ['Study Medium', 'Count']

# Create the Plotly Pie Chart
fig = px.pie(study_medium_counts,
             values='Count',
             names='Study Medium',
             title='Distribution of H.S.C or Equivalent Study Medium')

fig.update_traces(textposition='inside', textinfo='percent+label')

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)



# Create DataFrame based on the graph values 
data = {
    'Arts Program': [
        'B.A. in English', 'B.A. in English',
        'M. A. in ELT (1.4 Year)', 'M. A. in ELT (1.4 Year)',
        'M. A. in ELT (2 Year)', 'M. A. in ELT (2 Year)',
        'M.A. in English', 'M.A. in English'
    ],
    'Gender': [
        'Female', 'Male',
        'Female', 'Male',
        'Female', 'Male',
        'Female', 'Male'
    ],
    # Approximate values read from the graph
    'Count': [
        52, 17, # B.A. in English
        11, 2,  # M. A. in ELT (1.4 Year)
        2, 1,   # M. A. in ELT (2 Year)
        0, 1    # M.A. in English
    ]
}
program_gender_counts = pd.DataFrame(data)

# Create the Plotly Grouped Bar Chart
fig = px.bar(program_gender_counts,
             x='Arts Program',
             y='Count',
             color='Gender',
             barmode='group', # Puts the 'Gender' bars side-by-side
             title='Arts Program by Gender',
             labels={'Count': 'Number of Students', 'Arts Program': 'Arts Program'})

fig.update_layout(xaxis_tickangle=45)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. --- Configuration and Data Source ---
st.set_page_config(page_title="GitHub Data Loader", layout="wide")
st.title("Streamlit Data Loader from GitHub 📄")

url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/arts_faculty_data.csv'

# 2. --- Data Loading Function with Caching ---

# @st.cache_data is crucial. It tells Streamlit to run this function 
# and store the result (the DataFrame) in a local cache. 
# This prevents the app from re-downloading the file every time the user interacts with the app.
@st.cache_data
def load_data(data_url):
    try:
        data_frame = pd.read_csv(data_url)
        # st.success replaces print() for a styled success message
        st.success("DataFrame loaded successfully from URL! 🎉")
        return data_frame
    except Exception as e:
        # st.error replaces print() for error handling
        st.error(f"An error occurred while loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on failure

arts_df_url = load_data(url)

# 3. --- Streamlit Display ---
if not arts_df_url.empty:
    st.subheader("Preview of Arts Faculty Data")
    # st.dataframe() replaces the display() function, providing an interactive table
    st.dataframe(arts_df_url.head())
    
    st.info(f"DataFrame Shape: {arts_df_url.shape[0]} rows, {arts_df_url.shape[1]} columns.")



# --- Setup and Data Loading (Required for a runnable Streamlit app) ---
# NOTE: Assume 'arts_df_url' is loaded here, for example:
# arts_df_url = pd.read_csv('your_url_here.csv') 

# MOCK DATA: Using dummy data to make the example runnable
data = {'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female']}
arts_df_url = pd.DataFrame(data)

# Count the occurrences of each gender (Your original logic)
gender_counts = arts_df_url['Gender'].value_counts()

st.title('Gender Distribution Visualization 📊')

# 2. --- Plotly Chart Creation (Replaces Matplotlib) ---

# Use Plotly Express to create the interactive pie chart
fig = px.pie(
    # 'names' are the labels (e.g., 'Female', 'Male')
    names=gender_counts.index,     
    # 'values' are the counts 
    values=gender_counts.values,   
    title='Gender Distribution in Arts Faculty'
)

# Optional: Customize the appearance for better readability
fig.update_traces(
    textposition='inside',      # Position text inside slices
    textinfo='percent+label'    # Show both percentage and label
)

fig.update_layout(
    title_x=0.5 # Center the title
)

# 3. --- Streamlit Display (Replaces plt.show()) ---

# Display the interactive Plotly figure in the Streamlit app
st.plotly_chart(fig, use_container_width=True)


# --- Assume 'df' is your loaded DataFrame ---
# For demonstration, creating a dummy DataFrame that matches the structure:
data = {'Gender': ['Male', 'Female', 'Male', 'Female'],
        'S.S.C (GPA)': [4.5, 4.8, 4.2, 4.9],
        'H.S.C (GPA)': [4.0, 4.7, 3.8, 4.6]}
df = pd.DataFrame(data)
# --- End of dummy DataFrame creation ---

## 📊 Streamlit Plotly Chart

# 1. Calculate the average GPA by Gender
avg_gpa = df.groupby('Gender')[['S.S.C (GPA)', 'H.S.C (GPA)']].mean().reset_index()

# 2. Reshape the data for Plotly (from wide to long format)
# This makes plotting multiple columns as separate bars easier with Plotly Express
avg_gpa_long = pd.melt(avg_gpa,
                       id_vars='Gender',
                       value_vars=['S.S.C (GPA)', 'H.S.C (GPA)'],
                       var_name='Exam Level',
                       value_name='Average GPA')

# 3. Create the Plotly Bar Chart
fig = px.bar(avg_gpa_long,
             x='Gender',
             y='Average GPA',
             color='Exam Level',
             barmode='group', # Group bars side-by-side
             title='Average S.S.C and H.S.C GPA by Gender',
             labels={'Average GPA': 'Average GPA', 'Gender': 'Gender'})

# Optional: Customize layout for better appearance (like setting fixed x-tick rotation)
fig.update_layout(xaxis_tickangle=0)

# 4. Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# --- Assume 'arts_df' is your loaded DataFrame ---
# For demonstration, creating a dummy DataFrame that matches the structure:
data = {'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Arts Program': ['Music', 'Drama', 'Music', 'Visual Arts', 'Drama', 'Music']}
arts_df = pd.DataFrame(data)
# --- End of dummy DataFrame creation ---

## 📊 Streamlit Plotly Grouped Bar Chart

# 1. Count the occurrences of each Arts Program by Gender
# This is already in a good "long" format for Plotly, just need to rename the count column.
program_gender_counts = arts_df.groupby(['Gender', 'Arts Program']).size().reset_index(name='Count')

# 2. Create the Plotly Grouped Bar Chart
fig = px.bar(program_gender_counts,
             x='Arts Program',
             y='Count',
             color='Gender', # Used for grouping the bars
             barmode='group', # Puts the 'Gender' bars side-by-side
             title='Arts Program by Gender',
             labels={'Count': 'Number of Students', 'Arts Program': 'Arts Program'})

# Optional: Customize layout for better appearance
fig.update_layout(xaxis_tickangle=45) # Rotate x-axis labels

# 3. Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# --- Assume 'arts_df' is your loaded DataFrame ---
# For demonstration, creating a dummy DataFrame that matches the structure:
data = {'Did you ever attend a Coaching center?': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No']}
arts_df = pd.DataFrame(data)
# --- End of dummy DataFrame creation ---

## 🥧 Streamlit Plotly Pie Chart

# 1. Count the occurrences of each response
coaching_counts = arts_df['Did you ever attend a Coaching center?'].value_counts().reset_index()
coaching_counts.columns = ['Response', 'Count']

# 2. Create the Plotly Pie Chart
fig = px.pie(coaching_counts,
             values='Count',
             names='Response',
             title='Did students attend a Coaching Center?')

# Optional: Ensure text labels are visible inside the slices
fig.update_traces(textposition='inside', textinfo='percent+label')

# 3. Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)



# --- Configuration ---
st.set_page_config(layout="wide")
st.title("GPA Distribution Visualization")

# --- Sample Data (Replace with your actual data loading) ---
# NOTE: This creates a simplified placeholder DataFrame 'arts_df'
# with columns 'S.S.C (GPA)' and 'H.S.C (GPA)' for demonstration.
# You MUST replace this with your actual data loading (e.g., pd.read_csv('your_data.csv')).
data = {
    'S.S.C (GPA)': [1.0, 1.5, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0] * 5 + [4.8] * 15 + [5.0] * 20,
    'H.S.C (GPA)': [1.0, 1.5, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0] * 4 + [3.8] * 10 + [4.5] * 10 + [5.0] * 15
}
arts_df = pd.DataFrame(data)
arts_df = arts_df.melt(var_name='GPA Type', value_name='GPA') # Reshape for easy plotting

# --- Visualization using Plotly Express ---
gpa_columns = ['S.S.C (GPA)', 'H.S.C (GPA)']

# Use a multi-column layout for side-by-side plots
col1, col2 = st.columns(2)

for i, col in enumerate(gpa_columns):
    # Filter the data for the specific GPA type
    df_filtered = arts_df[arts_df['GPA Type'] == col].dropna()

    # Create the Plotly Histogram with a Kernel Density Estimate (KDE) curve
    # Plotly's 'histnorm'='probability density' is used with 'marginal'='box'
    # or 'marginal'='rug' or 'marginal'='violin'. 'kde' is not a direct
    # marginal option for standard hist plots in px.histogram.
    # To mimic KDE, you can use the density plot directly or use 'marginal'
    # for secondary info, or use a combination (more complex).
    # The image shows a 'density' curve overlaid on a histogram.

    # A simpler approach that provides both histogram and smooth curve:
    fig = px.histogram(
        df_filtered,
        x='GPA',
        nbins=7, # Adjust the number of bins to match the image
        title=f'Distribution of {col}',
        labels={'GPA': 'GPA', 'count': 'Frequency'}, # Set labels
        height=400,
        opacity=0.6,
    )

    # To add the smooth curve (KDE/Density plot) using Plotly Graph Objects (go):
    # This part can be more complex to exactly replicate the Seaborn KDE overlay.
    # Plotly Express doesn't have a direct 'kde=True' for histogram.
    # We will stick to the histogram for simplicity and speed, as requested (short code).

    # To mimic the KDE curve, you could consider using a Density plot *instead*
    # fig = px.density_heatmap(df_filtered, x='GPA', marginal_y="histogram")

    # Display the plot in the corresponding column
    if i == 0:
        with col1:
            st.plotly_chart(fig, use_container_width=True)
    else:
        with col2:
            st.plotly_chart(fig, use_container_width=True)

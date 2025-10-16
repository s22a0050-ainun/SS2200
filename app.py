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



# --- 1. Create a statistically representative dummy DataFrame ---
# The distributions appear highly negatively skewed (most data points are high).
np.random.seed(42)

# S.S.C (Left Graph): High frequency around 4.5-5.0
ssc_data = np.concatenate([
    np.random.uniform(4.0, 5.0, size=70), # Majority high scores
    np.random.uniform(3.0, 4.0, size=20),
    np.random.uniform(1.0, 3.0, size=10)
])

# H.S.C (Right Graph): High frequency around 4.5-5.0, slightly fewer total points
hsc_data = np.concatenate([
    np.random.uniform(4.0, 5.0, size=50), # Majority high scores
    np.random.uniform(3.5, 4.5, size=25),
    np.random.uniform(1.0, 3.5, size=15)
])

# Create the DataFrame
df_hist = pd.DataFrame({
    'S.S.C (GPA)': ssc_data,
    'H.S.C (GPA)': hsc_data
})
# --- End of dummy DataFrame creation ---

## 📊 Streamlit Plotly Histograms

# 2. Reshape the data from Wide to Long using pd.melt()
# This creates a single 'GPA Value' column and a 'GPA Type' column for faceting.
df_hist_long = pd.melt(df_hist,
                       value_vars=['S.S.C (GPA)', 'H.S.C (GPA)'],
                       var_name='GPA Type',
                       value_name='GPA Value').dropna() # Drop NA values if any

# 3. Create the Plotly Faceted Histograms
fig = px.histogram(df_hist_long,
                   x='GPA Value',
                   # 'GPA Type' is used to create separate plots (columns)
                   facet_col='GPA Type',
                   # Optional: Adds the KDE-like line (Density)
                   histnorm='probability density',
                   marginal='box', # or 'violin', 'rug' for marginal plot
                   title='Distribution of S.S.C and H.S.C GPA')

# 4. Customize the plot to match the appearance
# Update titles and ensure independent axes for better comparison
fig.for_each_annotation(lambda a: a.update(text=a.text.replace("GPA Type=", "Distribution of ")))
fig.update_xaxes(title_text="GPA")
fig.update_yaxes(title_text="Frequency")
fig.update_layout(bargap=0.05) # Add space between bars

# 5. Display the chart in Streamlit
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



# --- Assume 'arts_df' is your loaded DataFrame ---
# For demonstration, creating a dummy DataFrame that matches the structure:
data =  {'S.S.C (GPA)': [4.5, 4.8, 4.2, 4.9, 3.5, 4.0],
        'H.S.C (GPA)': [4.0, 4.7, 3.8, 4.6, 3.2, 3.9],
        'Other Column': ['A', 'B', 'A', 'B', 'C', 'C']}
arts_df = pd.DataFrame(data)
# --- End of dummy DataFrame creation ---

## 📈 Streamlit Plotly Histograms (Faceted)

# 1. Identify the GPA columns
gpa_columns = [col for col in arts_df.columns if 'GPA' in col]

# 2. Reshape the data from Wide to Long using pd.melt()
# This stacks the GPA columns, creating a single column of GPA values and a column
# indicating which type of GPA (e.g., S.S.C or H.S.C) it is.
arts_df_long = pd.melt(arts_df,
                       value_vars=gpa_columns,
                       var_name='GPA Type',
                       value_name='GPA Value')

# 3. Create the Plotly Faceted Histograms
fig = px.histogram(arts_df_long.dropna(), # Drop NA values for clean plotting
                   x='GPA Value',
                   color='GPA Type', # Optional: Color the bars based on GPA Type
                   facet_col='GPA Type', # Create a separate column/plot for each GPA Type
                   title='Distribution of GPA Scores',
                   labels={'GPA Value': 'GPA Score', 'count': 'Frequency'})

# Optional: Customize layout for better appearance
fig.update_layout(showlegend=False) # Legend is redundant since facet_col is used
fig.update_xaxes(matches=None) # Allow x-axes to have independent ranges (if needed)

# 4. Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)



# --- Assume 'arts_df' is your loaded DataFrame ---
# For demonstration, creating a dummy DataFrame that matches the structure:
data = {'H.S.C or Equivalent study medium': ['Bangla', 'English', 'Madrasa', 'Bangla', 'Bangla', 'Bangla', 'Bangla']}
arts_df = pd.DataFrame(data)
# --- End of dummy DataFrame creation ---

## 🥧 Streamlit Plotly Pie Chart

# 1. Count the occurrences and format the data for Plotly
study_medium_counts = arts_df['H.S.C or Equivalent study medium'].value_counts().reset_index()
study_medium_counts.columns = ['Study Medium', 'Count']

# 2. Create the Plotly Pie Chart
fig = px.pie(study_medium_counts,
             values='Count',
             names='Study Medium',
             title='Distribution of H.S.C or Equivalent Study Medium')

# Optional: Customize text formatting
fig.update_traces(textposition='inside', textinfo='percent+label')

# 3. Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# --- 1. Create DataFrame based on the graph values ---
data = {
    'Arts Program': ['B.A. in English', 'M. A. in ELT (1.4 Year)', 'M. A. in ELT (2 Year)', 'M.A. in English'],
    # Approximate values read from the graph
    'Number of Students': [69, 13, 3, 2]
}
df_arts = pd.DataFrame(data)

# --- 2. Create the Plotly Bar Chart ---
fig = px.bar(df_arts,
             x='Arts Program',
             y='Number of Students',
             title='Distribution of Arts Programs',
             # Optional: Set a consistent color for the bars
             color_discrete_sequence=['#1f77b4'])

# Optional: Customize layout to match the rotation of the x-axis labels
fig.update_layout(xaxis_tickangle=45)

# --- 3. Display the chart in Streamlit ---
st.plotly_chart(fig, use_container_width=True)



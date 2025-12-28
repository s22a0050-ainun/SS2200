import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Individual Visualizations")

# Load the main DataFrame
df = pd.read_csv("Exploring Internet Use and Suicidality in Mental Health Populations.csv")

# Step 1: Debugging - Print DataFrame columns
st.write("Dataframe Columns:")
st.write(df.columns)  # Shows all column names

# Step 2: Check for missing values
st.write("Missing Values in Data:")
st.write(df.isna().sum())  # Shows missing values count for each column

# Step 3: Check data types
st.write("Data Types in Data:")
st.write(df.dtypes)  # Shows the data types for each column

# Check if required columns exist in DataFrame
required_columns = ['Year_of_Study', 'Gender', 'Social_Media_Positive_Impact_on_Wellbeing']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"Missing columns: {', '.join(missing_columns)}")
else:
    # If all required columns exist, proceed with handling missing data
    st.write("All required columns are present, proceeding with cleaning and visualizations.")
    df = df.dropna(subset=required_columns)
    df['Year_of_Study'] = df['Year_of_Study'].astype(str)
    df['Gender'] = df['Gender'].astype(str)

    # Now proceed with the visualizations (which you can place below this)

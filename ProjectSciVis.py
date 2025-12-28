import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from GitHub 
url = 'https://raw.githubusercontent.com/s22a0050-ainun/SS2200/refs/heads/main/Exploring%20Internet%20Use%20and%20Suicidality%20in%20Mental%20Health%20Populations.csv'
data = pd.read_csv(url)

# Data Collection Page
st.title('Data Collection')
st.write("/content/Exploring Internet Use and Suicidality in Mental Health Populations.csv")
st.write(data.head())  # Show the first few rows of the dataset

# Visualization Page 1: Group Bar Chart
st.title('Visualization 1: Group Bar Chart')
st.subheader('Gender Distribution Across Year of Study')
plt.figure(figsize=(10,6))
# Assuming 'gender' and 'year_of_study' are the columns
sns.countplot(x='year_of_study', hue='gender', data=data, palette='Set2')
plt.xlabel('Year of Study')
plt.ylabel('Number of Respondents')
st.pyplot()

# Visualization Page 2
st.title('Visualization 2: Correlation Heatmap')
st.subheader('Year of Study vs Current Living Situation')
plt.figure(figsize=(10,6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
st.pyplot()

# Visualization Page 3: Stacked Bar Chart
st.title('Visualization 3: Stacked Bar Chart')
st.subheader('Gender vs Social Media Impact on Wellbeing')
# Assuming 'gender' and 'social_media_impact' are the columns
social_media_impact = pd.crosstab(data['gender'], data['social_media_impact'])
social_media_impact.plot(kind='bar', stacked=True, figsize=(10,6), color=['lightgreen', 'salmon'])
plt.title('Impact of Social Media on Wellbeing by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Respondents')
st.pyplot()

# Visualization Page 4: Group Bar Chart
st.title('Visualization 4: Group Bar Chart')
st.subheader('Race vs Social Media as Part of Daily Routine')
# Assuming 'race' and 'social_media_daily_routine' are the columns
plt.figure(figsize=(10,6))
sns.countplot(x='race', hue='social_media_daily_routine', data=data, palette='Set1')
plt.title('Race vs Social Media as Part of Daily Routine')
plt.xlabel('Race')
plt.ylabel('Number of Respondents')
st.pyplot()

# Visualization Page 5: Bar Chart 
st.title('Visualization 5: Bar Chart')
st.subheader('Gender vs Difficulty Sleeping Due to University Pressure')
# Assuming 'gender' and 'difficulty_sleeping' are the columns
plt.figure(figsize=(10,6))
sns.countplot(x='gender', hue='difficulty_sleeping', data=data, palette='coolwarm')
plt.title('Gender vs Difficulty Sleeping Due to University Pressure')
plt.xlabel('Gender')
plt.ylabel('Number of Respondents')
st.pyplot()

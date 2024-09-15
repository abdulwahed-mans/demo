import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title
st.set_page_config(page_title='Swedish Institute Students Data', page_icon=':school:')

# Load CSV file with utf-16 encoding
file_path = 'data.csv'  # Replace with the correct file path if necessary
try:
    df = pd.read_csv(file_path, encoding='utf-16')
    st.write('Data from data.csv:')
    st.dataframe(df)
except UnicodeDecodeError:
    st.error("Error reading the CSV file due to encoding issues.")

# Display the first few rows of the dataframe
st.write("First five rows of the data:")
st.dataframe(df.head())

# Display basic statistics
st.subheader("Basic Statistics")
st.write(df.describe())

# Age Distribution
st.subheader("Age Distribution")
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=10, kde=True, color='green')
plt.title('Age Distribution with KDE')
plt.xlabel('Age')
plt.ylabel('Frequency')
st.pyplot(plt)

# Gender Distribution
st.subheader("Gender Distribution")
gender_counts = df['gender'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('Gender Distribution')
st.pyplot(plt)

# Nationality Distribution
st.subheader("Nationality Distribution")
nationality_counts = df['nationality'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(nationality_counts, labels=nationality_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2', len(nationality_counts)))
plt.title('Nationality Distribution')
st.pyplot(plt)

# Relationship between Age and Grades
st.subheader("Relationship between Age and Grades")
# Convert grades to numerical values for better visualization
grade_mapping = {'A': 3, 'B': 2, 'C': 1}
df['grade_numeric'] = df['grade'].map(grade_mapping)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='grade_numeric', data=df, hue='grade', palette='coolwarm', s=100)
plt.title('Relationship between Age and Grades')
plt.xlabel('Age')
plt.ylabel('Grades (Numeric)')
st.pyplot(plt)

# Display data summary
st.subheader("Data Summary")
st.write(df.describe())

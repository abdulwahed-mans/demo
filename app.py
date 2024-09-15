import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title
st.set_page_config(page_title='Swedish Institute Students Data', page_icon=':school:')

# Display title and header
st.title('Swedish Institute Students Data')
st.header('CSV File Data with Filtering and Widgets')

# Load CSV file with specified encoding
try:
    df = pd.read_csv('data.csv', encoding='utf-16')  # Adjust encoding if necessary utf-16, utf-8, etc
    st.write('Data from data.csv:')
    st.dataframe(df)
except UnicodeDecodeError:
    st.error("Error reading the CSV file due to encoding issues.")

# Adding a Selectbox widget
st.subheader("Selectbox Example")
choice = st.selectbox("Pick one", ["cats", "dogs", "birds"])
st.write(f"You selected: {choice}")

# Adding a Multiselect widget
st.subheader("Multiselect Example")
choices = st.multiselect("Buy", ["milk", "apples", "potatoes", "bread", "eggs"])
st.write(f"You selected: {choices}")

# Adding a Select Slider widget
st.subheader("Select Slider Example")
size = st.select_slider("Choose a size", options=["Small", "Medium", "Large", "Extra Large"])
st.write(f"You selected: {size}")

# Filter by Nationality and Gender
if 'df' in locals():
    nationality = st.selectbox('Select Nationality', df['nationality'].unique())
    gender = st.selectbox('Select Gender', df['gender'].unique())

    # Filter data
    filtered_data = df[(df['nationality'] == nationality) & (df['gender'] == gender)]
    st.write(f"Showing data for {gender} students from {nationality}")
    st.dataframe(filtered_data)

    # Display a custom bar chart of grades with colors using Matplotlib and Seaborn
    st.subheader("Bar Chart of Grades")

    # Count the grades in the filtered data
    grade_counts = filtered_data['grade'].value_counts()

    # Create a bar plot using Seaborn with custom colors
    fig, ax = plt.subplots()
    sns.barplot(x=grade_counts.index, y=grade_counts.values, palette="coolwarm", ax=ax)

    # Customize the chart with labels and title
    ax.set_title(f'Grade Distribution for {gender} Students from {nationality}', fontsize=16)
    ax.set_xlabel('Grade', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)

    # Display the chart in Streamlit
    st.pyplot(fig)

# Option to upload a CSV file
uploaded_file = st.file_uploader('Upload your own CSV file', type='csv')
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        st.write('Uploaded File Data:')
        st.dataframe(data)

        # Display a bar chart for the uploaded data
        st.subheader("Bar Chart of Grades for Uploaded Data")

        # Count grades from uploaded data
        grade_counts_uploaded = data['grade'].value_counts()

        # Create a bar plot for uploaded data
        fig_uploaded, ax_uploaded = plt.subplots()
        sns.barplot(x=grade_counts_uploaded.index, y=grade_counts_uploaded.values, palette="coolwarm", ax=ax_uploaded)

        # Customize the chart
        ax_uploaded.set_title('Grade Distribution for Uploaded Data', fontsize=16)
        ax_uploaded.set_xlabel('Grade', fontsize=12)
        ax_uploaded.set_ylabel('Count', fontsize=12)

        # Display the chart in Streamlit
        st.pyplot(fig_uploaded)

    except UnicodeDecodeError:
        st.error("Error reading the uploaded CSV file due to encoding issues.")

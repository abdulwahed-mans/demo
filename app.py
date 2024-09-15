import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title='My Streamlit App', page_icon=':rocket:')

# Display title and header
st.title('Welcome to My Streamlit App')
st.header('CSV File Data')

# Load and display CSV file
df = pd.read_csv('data.csv')
st.write('Data from data.csv:')
st.dataframe(df)

# Option to upload a CSV file
uploaded_file = st.file_uploader('Upload your own CSV file', type='csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write('Uploaded File Data:')
    st.dataframe(data)

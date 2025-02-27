import streamlit as st
import requests
import json
from components.sidebar import show_sidebar  # ✅ Import sidebar

selected, sub_selected = show_sidebar()

from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header

def show_user_guide():
    st.title("User Guide - Smart Data Tool")
    st.write("This guide will help you navigate and use the Smart Data Tool efficiently.")

    # Sidebar for sections
    section = st.sidebar.radio("Jump to Section:", ["Introduction", "Navigation", "Data Upload & Import", "Frontend Data Transformation", "Data Cleaning & Processing", "Frontend API Connection", "Data Analysis", "Data Visualization & Charts", "Data Export & Download"])

    # Introduction
    if section == "Introduction":
        st.header("Introduction")
        st.write("The **Smart Data Tool** helps users clean, organize, and analyze their data efficiently.")
        st.write("It offers a **user-friendly interface** with features for both technical and non-technical users.")
        st.button("Go to Backend User Guide", on_click=lambda: st.switch_page("backend_user_guide"))

    # Navigation
    elif section == "Navigation":
        st.header("Navigation")
        st.write("You can navigate through the app using the navigation bar at the top.")
        st.write("Available options:")
        st.markdown("- **Home**: Main landing page of the app.")
        st.markdown("- **Guide**: Access this user guide.")
        st.markdown("- **Featured**: View key features like data cleaning, organization, and more.")

    # Frontend Data Upload Guide
    elif section == "Data Upload & Import":
        st.header("Data Upload & Import - Frontend Users")
        st.write("Frontend users (non-technical users) can upload data using the following methods:")
        st.markdown("- **CSV, Excel, JSON, TXT**: Upload directly from a local device.")
        st.markdown("- **Google Sheets**: Link and fetch data from Google Sheets.")
        st.markdown("- **Dropbox & OneDrive**: Import files stored in these services.")
        st.markdown("- **Clipboard Paste**: Copy-paste data directly into the tool.")
        st.write("To use this feature:")
        st.markdown("1. Select **Frontend Upload** from the dropdown on the landing page.")
        st.markdown("2. Choose your preferred upload method.")
        st.markdown("3. Follow the on-screen instructions to upload and process your data.")
    
    # Frontend Data Transformation Guide
    elif section == "Frontend Data Transformation":
        st.header("Frontend Data Transformation")
        st.write("The **Frontend Data Transformation** feature allows users to clean and modify their data easily.")
        st.write("Available transformations include:")
        st.markdown("- **Date Formatting**: Converts date columns into a standard YYYY-MM-DD format.")
        st.markdown("- **Text Standardization**: Converts text columns to uppercase.")
        st.markdown("- **Character Removal**: Cleans unwanted characters from specific columns.")
        st.markdown("- **Column Splitting**: Splits full names into first and last names.")
        st.markdown("- **Formula Application**: Computes profit by subtracting cost from revenue.")
        st.markdown("- **Category Mapping**: Converts numeric categories into meaningful labels.")
        st.markdown("- **Data Merging**: Combines datasets based on a common column.")
        st.write("To use this feature:")
        st.markdown("1. Upload a CSV or Excel file containing the data to be transformed.")
        st.markdown("2. Select the transformations to apply.")
        st.markdown("3. View the transformed data in the preview section.")
    
    # Data Cleaning & Processing Guide
    elif section == "Data Cleaning & Processing":
        st.header("Data Cleaning & Processing")
        st.write("The **Data Cleaning & Processing** feature ensures that your dataset is structured, consistent, and ready for analysis.")
        st.write("Available cleaning options include:")
        st.markdown("- **Detect and Fix Inconsistent Column Names**: Standardizes column names by removing spaces and formatting them consistently.")
        st.markdown("- **Smart Duplicate Handling**: Identifies and removes duplicate records.")
        st.markdown("- **Intelligent Missing Value Handling**: Fills missing values using methods like mean, median, or predictive imputation.")
        st.markdown("- **Detect and Fix Data Entry Errors**: Uses fuzzy matching to correct inconsistent entries.")
        st.markdown("- **Data Type Auto-Correction**: Converts columns to appropriate data types (numbers, dates, text, etc.).")
        st.markdown("- **Address Cleaning and Standardization**: Validates and formats address data using external APIs.")
        st.markdown("- **Phone Number Formatting and Validation**: Ensures phone numbers follow a standard international format.")
        st.markdown("- **Automated Data Anonymization**: Masks sensitive information such as names and emails.")
        st.markdown("- **Handle Outliers with User Choice**: Detects and processes extreme values using statistical methods.")
    
    # Frontend API Connection Guide
    elif section == "Frontend API Connection":
        st.header("Frontend API Connection")
        st.write("The **Frontend API Connection** feature allows users to connect external APIs to retrieve and process data.")
        st.write("Supported functionalities:")
        st.markdown("- **REST API Requests**: Fetch data from external sources using API endpoints.")
        st.markdown("- **GraphQL Queries**: Query structured data using GraphQL endpoints.")
        st.markdown("- **Custom API Integration**: Configure API keys and authentication for secure access.")
        st.write("To use this feature:")
        st.markdown("1. Enter the API endpoint and necessary authentication details.")
        st.markdown("2. Choose the request type (GET, POST, etc.).")
        st.markdown("3. View the fetched data and process it as needed.")
    
    # Data Analysis Guide
    elif section == "Data Analysis":
        st.header("Data Analysis & Processing")
        st.write("The **Data Analysis** feature helps process and analyze data effectively.")
        st.markdown("- **Clean Data**: Automatically cleans and processes the dataset.")
        st.markdown("- **Generate Table**: Converts data into structured tables.")
        st.markdown("- **Linear Regression**: Performs basic linear regression analysis on the dataset.")
    
    # Data Visualization & Charts Guide
    elif section == "Data Visualization & Charts":
        st.header("Data Visualization & Charts")
        st.write("The **Chart Generator** feature allows users to create different types of charts from their dataset.")
        st.markdown("- **Bar Chart**: Displays categorical data using bars.")
        st.markdown("- **Line Chart**: Shows trends over time with lines.")
        st.markdown("- **Scatter Plot**: Displays relationships between numerical variables.")
    
    # Data Export & Download Guide
    elif section == "Data Export & Download":
        st.header("Data Export & Download")
        st.write("The **Data Export & Download** feature allows users to save and share processed data.")
        st.markdown("- **CSV Export**: Save data as a CSV file.")
        st.markdown("- **Excel Export**: Download data in Excel format.")
        st.markdown("- **JSON Export**: Export data in JSON format.")
        st.markdown("- **Clipboard Copy**: Copy data for quick use in other applications.")

if __name__ == "__main__":
    show_user_guide()

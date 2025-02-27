# pages/frontend_transformation.py
import streamlit as st
import pandas as pd
from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()

from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header

def frontend_transformation(data):
    # Example of transforming date format
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

    # Example of changing text to uppercase
    if 'text_column' in data.columns:
        data['text_column'] = data['text_column'].str.upper()

    # Example of removing unwanted characters
    if 'name' in data.columns:
        data['name'] = data['name'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=False)

    # Column splitting (splitting 'full_name' into 'first_name' and 'last_name')
    if 'full_name' in data.columns:
        data[['first_name', 'last_name']] = data['full_name'].str.split(' ', expand=True)

    # Apply formula (e.g., calculate profit)
    if 'revenue' in data.columns and 'cost' in data.columns:
        data['profit'] = data['revenue'] - data['cost']

    # Category mapping (mapping numeric categories to text)
    category_map = {1: 'Low', 2: 'Medium', 3: 'High'}
    if 'category' in data.columns:
        data['category'] = data['category'].map(category_map)

    # Merge data (example of merging with another dataset)
    if 'merge_column' in data.columns:
        # Assuming you have another dataframe 'other_data' to merge with
        other_data = pd.DataFrame({'merge_column': [1, 2, 3], 'extra_info': ['A', 'B', 'C']})
        data = pd.merge(data, other_data, on='merge_column', how='left')

    return data

def show_transformation_page():
    st.title("Frontend Data Transformation")
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file:
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "csv":
            data = pd.read_csv(uploaded_file)
        elif file_extension == "xlsx":
            data = pd.read_excel(uploaded_file)
        
        st.write("Original Data:")
        st.dataframe(data)

        # Apply transformations
        transformed_data = frontend_transformation(data)

        st.write("Transformed Data:")
        st.dataframe(transformed_data)

# Call the function to display the data transformation page
show_transformation_page()

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from fuzzywuzzy import process
import phonenumbers
import requests
from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()

from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header

# Function to clean data
def clean_data(data, options):
    if "Detect and Fix Inconsistent Column Names" in options:
        data.columns = [col.strip().replace(" ", "_").lower() for col in data.columns]
    
    if "Smart Duplicate Handling" in options:
        data = data.drop_duplicates()
    
    if "Intelligent Missing Value Handling" in options:
        imputer = SimpleImputer(strategy="mean")
        data.iloc[:, :] = imputer.fit_transform(data.select_dtypes(include=[np.number]))
    
    if "Detect and Fix Data Entry Errors" in options:
        for col in data.select_dtypes(include=["object"]):
            data[col] = data[col].apply(
                lambda x: process.extractOne(x, data[col].dropna().unique())[0] if pd.notnull(x) else x
            )
    
    if "Data Type Auto-Correction" in options:
        for col in data.columns:
            try:
                data[col] = pd.to_numeric(data[col])
            except:
                pass
    
    if "Phone Number Formatting and Validation" in options:
        for col in data.columns:
            try:
                data[col] = data[col].apply(
                    lambda x: phonenumbers.format_number(
                        phonenumbers.parse(x, "US"), phonenumbers.PhoneNumberFormat.INTERNATIONAL
                    ) if pd.notnull(x) else x
                )
            except:
                continue
    
    if "Address Cleaning and Standardization" in options:
        for col in data.columns:
            if "address" in col.lower():
                data[col] = data[col].apply(lambda x: validate_address(x) if pd.notnull(x) else x)
    
    if "Automated Data Anonymization" in options:
        for col in data.columns:
            if "name" in col.lower() or "email" in col.lower():
                data[col] = "[REDACTED]"
    
    if "Handle Outliers with User Choice" in options:
        for col in data.select_dtypes(include=[np.number]):
            q1 = data[col].quantile(0.25)
            q3 = data[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            data[col] = np.where((data[col] < lower_bound) | (data[col] > upper_bound), np.nan, data[col])
            data[col].fillna(data[col].median(), inplace=True)
    
    return data

# Function to validate addresses using an external API
def validate_address(address):
    api_url = f"https://elegant-embrace-production.up.railway.app/geocode?address={address}"
    response = requests.get(api_url).json()
    if response["status"] == "OK":
        return response["results"][0]["formatted_address"]
    return address

# Streamlit UI
st.title("Data Cleaning and Processing")
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    cleaning_options = [
        "Detect and Fix Inconsistent Column Names",
        "Smart Duplicate Handling",
        "Intelligent Missing Value Handling",
        "Detect and Fix Data Entry Errors",
        "Data Type Auto-Correction",
        "Address Cleaning and Standardization",
        "Phone Number Formatting and Validation",
        "Automated Data Anonymization",
        "Handle Outliers with User Choice",
        "Apply All Options"
    ]
    
    selected_options = st.multiselect("Select Data Cleaning Options:", cleaning_options)
    
    if "Apply All Options" in selected_options:
        selected_options = cleaning_options[:-1]
    
    if st.button("Clean Data"):
        cleaned_df = clean_data(df, selected_options)
        st.write("### Cleaned Data Preview:")
        st.dataframe(cleaned_df)
        
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Cleaned Data", csv, "cleaned_data.csv", "text/csv")

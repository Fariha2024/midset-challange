import streamlit as st
import pandas as pd
from frontend.download import download_data

def show_export_options():
    st.subheader("Export & Download Processed Data")

    uploaded_file = st.file_uploader("Upload a CSV or Excel file:", type=["csv", "xlsx"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            st.write("### Data Preview:")
            st.dataframe(df.head())

            download_data(df)

        except Exception as e:
            st.error(f"Error loading file: {e}")

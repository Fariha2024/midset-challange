import streamlit as st
import pandas as pd

def handle_missing_values():
    st.subheader("Handle Missing Values")

    uploaded_file = st.file_uploader("Upload a CSV or Excel file:", type=["csv", "xlsx"])
    
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            st.write("### Original Data Preview:")
            st.dataframe(df.head())

            method = st.radio("Choose a method to fill missing values:", ["Mean", "Median", "Mode", "Drop Missing Rows"])

            if st.button("Apply Cleaning"):
                if method == "Mean":
                    df_cleaned = df.fillna(df.mean())
                elif method == "Median":
                    df_cleaned = df.fillna(df.median())
                elif method == "Mode":
                    df_cleaned = df.fillna(df.mode().iloc[0])
                else:
                    df_cleaned = df.dropna()

                st.write("### Cleaned Data Preview:")
                st.dataframe(df_cleaned)
                
                st.download_button("Download Cleaned Data", df_cleaned.to_csv(index=False), "cleaned_data.csv", "text/csv")

        except Exception as e:
            st.error(f"Error processing file: {e}")

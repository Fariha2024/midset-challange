import streamlit as st
import pandas as pd

def remove_duplicates():
    st.subheader("Remove Duplicate Entries")

    uploaded_file = st.file_uploader("Upload a CSV or Excel file:", type=["csv", "xlsx"])
    
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            st.write("### Original Data Preview:")
            st.dataframe(df.head())

            if st.button("Remove Duplicates"):
                df_cleaned = df.drop_duplicates()
                st.write("### Cleaned Data Preview:")
                st.dataframe(df_cleaned)
                
                st.download_button("Download Cleaned Data", df_cleaned.to_csv(index=False), "cleaned_data.csv", "text/csv")

        except Exception as e:
            st.error(f"Error loading file: {e}")



















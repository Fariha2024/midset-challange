import streamlit as st
import pandas as pd
from frontend.search import search_records

def show_filtering_options():
    st.subheader("Filtering & Querying")

    uploaded_file = st.file_uploader("Upload a CSV or Excel file:", type=["csv", "xlsx"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            st.write("### Data Preview:")
            st.dataframe(df.head())

            filter_option = st.selectbox("Select Filtering Method:", ["Search Records", "Filter by Column"])

            if filter_option == "Search Records":
                search_records(df)
            elif filter_option == "Filter by Column":
                column = st.selectbox("Select a column to filter:", df.columns)
                unique_values = df[column].unique()
                selected_value = st.selectbox("Select value:", unique_values)

                if st.button("Apply Filter"):
                    filtered_df = df[df[column] == selected_value]
                    st.write("### Filtered Data:")
                    st.dataframe(filtered_df)
                    st.download_button("Download Filtered Data", filtered_df.to_csv(index=False), "filtered_data.csv", "text/csv")

        except Exception as e:
            st.error(f"Error loading file: {e}")

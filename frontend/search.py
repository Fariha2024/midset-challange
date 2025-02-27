import streamlit as st
import pandas as pd

def search_records(df):
    st.subheader("Search for Specific Records")

    search_column = st.selectbox("Select a column to search:", df.columns)
    search_query = st.text_input("Enter search value:")

    if st.button("Search"):
        if search_query:
            search_results = df[df[search_column].astype(str).str.contains(search_query, case=False, na=False)]
            st.write("### Search Results:")
            st.dataframe(search_results)

            if not search_results.empty:
                st.download_button("Download Search Results", search_results.to_csv(index=False), "search_results.csv", "text/csv")
        else:
            st.warning("Please enter a search query.")

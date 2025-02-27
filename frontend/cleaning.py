import streamlit as st
from frontend.duplicates import remove_duplicates
from frontend.missing_values import handle_missing_values

def show_cleaning_options():
    st.subheader("Data Cleaning Options")

    cleaning_option = st.selectbox("Select Cleaning Method:", [
        "Remove Duplicates",
        "Handle Missing Values"
    ])

    if cleaning_option == "Remove Duplicates":
        remove_duplicates()
    elif cleaning_option == "Handle Missing Values":
        handle_missing_values()

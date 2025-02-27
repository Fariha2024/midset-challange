import streamlit as st
from frontend.upload import show_upload_section
from frontend.column_selection import select_columns
from frontend.cleaning import show_cleaning_options
from frontend.duplicates import remove_duplicates
from frontend.missing_values import handle_missing_values
from frontend.filtering import show_filtering_options
from frontend.search import search_records
from frontend.export import show_export_options  # ✅ Ensure this is included
from frontend.download import download_data  # ✅ Ensure this is included
from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()
from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header


def show_frontend_ui():
    st.title("Smart Data Tool - Frontend Features")

    option = st.selectbox("Select Feature", [
        "Upload Data",
        "Column Selection",
        "Data Cleaning",
        "Remove Duplicates",
        "Handle Missing Values",
        "Filtering & Searching",
        "Data Export & Download"
    ])

    if option == "Data Upload":
        show_upload_section()

    elif option == "Column Selection":
        select_columns()

    elif option == "Data Cleaning":
       show_cleaning_options()

    elif option == "Remove Duplicates":
        remove_duplicates()

    elif option == "Handle Missing Values":
        handle_missing_values()

    elif option == "Filtering & Searching":
        show_filtering_options()
        search_records()

    elif option == "Data Export & Download":  # ✅ Ensure this option is available
        show_export_options()
        download_data()

if __name__ == "__main__":
    show_frontend_ui()

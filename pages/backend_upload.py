import streamlit as st
from backend.api_connect import show_api_options
from backend.database_connect import display_connection_form as show_database_options
from backend.ftp_sftp import main as show_ftp_sftp_options
from backend.bigquery import show_bigquery_options
from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()
from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header

def show_backend_upload():
    st.subheader("Backend Data Upload Options")

    backend_option = st.selectbox("Select a Backend Upload Method:", [
        "Connect via API (REST, GraphQL)",
        "Database Connection (MySQL, PostgreSQL, MongoDB)",
        "Import from Cloud Storage (Google Drive, AWS S3)",
        "FTP/SFTP (Import files from a server)",
        "Big Data (BigQuery, Snowflake, HDFS)",
        "Azure Blob Storage (Fetch from Azure Cloud)"
    ])

    if backend_option == "Connect via API (REST, GraphQL)":
        show_api_options()  # Ensure this function contains Streamlit elements

    elif backend_option == "Database Connection (MySQL, PostgreSQL, MongoDB)":
        show_database_options()

    elif backend_option == "FTP/SFTP (Import files from a server)":
        show_ftp_sftp_options()

    elif backend_option == "Big Data (BigQuery, Snowflake, HDFS)":
        show_bigquery_options()

    elif backend_option == "Azure Blob Storage (Fetch from Azure Cloud)":
        st.write("Azure Blob Storage feature coming soon!")

if __name__ == "__main__":
    show_backend_upload()

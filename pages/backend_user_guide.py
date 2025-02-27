import streamlit as st

from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()
from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header
def show_backend_user_guide():
    st.title("📘 Backend User Guide")
    st.write("This guide will help backend users integrate and import data from various sources efficiently.")

    # Sidebar Navigation for Sections
    section = st.sidebar.radio("Jump to Section:", [
        "Introduction", 
        "API Integration", 
        "Database Connections", 
        "FTP/SFTP", 
        "Google BigQuery", 
        "Snowflake", 
        "Azure Blob Storage", 
        "HDFS"
    ])

    # Introduction
    if section == "Introduction":
        st.header("🔹 Introduction")
        st.write("The **Smart Data Tool** allows backend users to connect and import data from various sources.")
        st.write("Supported backend data import methods include:")
        st.markdown("- API Integration (REST, GraphQL)")
        st.markdown("- Database Connections (MySQL, PostgreSQL, MongoDB)")
        st.markdown("- Cloud Storage (Google BigQuery, Snowflake, Azure Blob Storage)")
        st.markdown("- File Transfer (FTP/SFTP, HDFS)")

    # API Integration Guide
    elif section == "API Integration":
        st.header("🔹 API Integration (REST, GraphQL)")
        st.write("Backend users can connect their data using APIs.")
        st.markdown("### Steps to Use API Integration:")
        st.markdown("1️⃣ Select **Backend Upload** → **Connect via API (REST, GraphQL)**.")
        st.markdown("2️⃣ Enter the **API Endpoint URL**.")
        st.markdown("3️⃣ Choose the API type (REST or GraphQL).")
        st.markdown("4️⃣ Provide authentication credentials (if required).")
        st.markdown("5️⃣ Click **Fetch Data** to import.")

    # Database Connections Guide
    elif section == "Database Connections":
        st.header("🔹 Database Connections (MySQL, PostgreSQL, MongoDB)")
        st.write("Backend users can connect to relational and NoSQL databases.")
        st.markdown("### Steps to Connect:")
        st.markdown("1️⃣ Select **Backend Upload** → **Database Connection**.")
        st.markdown("2️⃣ Choose the database type (MySQL, PostgreSQL, or MongoDB).")
        st.markdown("3️⃣ Enter the database credentials:")
        st.markdown("   - Host")
        st.markdown("   - Username")
        st.markdown("   - Password")
        st.markdown("   - Database Name")
        st.markdown("4️⃣ Click **Connect** to establish the connection.")

    # FTP/SFTP Guide
    elif section == "FTP/SFTP":
        st.header("🔹 FTP/SFTP Data Import")
        st.write("Backend users can fetch files from an FTP or SFTP server.")
        st.markdown("### Steps to Use FTP/SFTP:")
        st.markdown("1️⃣ Select **Backend Upload** → **FTP/SFTP**.")
        st.markdown("2️⃣ Enter your FTP/SFTP server details:")
        st.markdown("   - Host")
        st.markdown("   - Username")
        st.markdown("   - Password")
        st.markdown("3️⃣ Click **Connect** to establish the connection.")
        st.markdown("4️⃣ Browse and **Download** files for processing.")

    # Google BigQuery Guide
    elif section == "Google BigQuery":
        st.header("🔹 Google BigQuery - Large Dataset Import")
        st.write("Backend users can fetch large datasets from Google BigQuery.")
        st.markdown("### Steps to Use BigQuery:")
        st.markdown("1️⃣ Select **Backend Upload** → **Google BigQuery**.")
        st.markdown("2️⃣ Enter your Google Cloud Project details:")
        st.markdown("   - Project ID")
        st.markdown("   - Dataset ID")
        st.markdown("   - Table ID")
        st.markdown("3️⃣ Click **Connect to BigQuery**.")
        st.markdown("4️⃣ Upload a **CSV or Excel file** and click **Upload to BigQuery**.")

    # Snowflake Guide
    elif section == "Snowflake":
        st.header("🔹 Snowflake - Enterprise Data Import")
        st.write("Enterprise users can import data from their Snowflake cloud database.")
        st.markdown("### Steps to Use Snowflake:")
        st.markdown("1️⃣ Select **Backend Upload** → **Snowflake**.")
        st.markdown("2️⃣ Enter your Snowflake credentials:")
        st.markdown("   - Account Name")
        st.markdown("   - Username & Password")
        st.markdown("   - Database & Warehouse Name")
        st.markdown("   - Schema & Table Name")
        st.markdown("3️⃣ Click **Connect to Snowflake**.")
        st.markdown("4️⃣ Upload and import your data.")

    # Azure Blob Storage Guide
    elif section == "Azure Blob Storage":
        st.header("🔹 Azure Blob Storage - Cloud Data Fetch")
        st.write("Backend users can fetch files from **Azure Blob Storage**.")
        st.markdown("### Steps to Use Azure Blob Storage:")
        st.markdown("1️⃣ Select **Backend Upload** → **Azure Blob Storage**.")
        st.markdown("2️⃣ Enter the following details:")
        st.markdown("   - Storage Account Name")
        st.markdown("   - Container Name")
        st.markdown("   - Blob Name")
        st.markdown("3️⃣ Click **Connect to Azure**.")
        st.markdown("4️⃣ Browse and **Download** files from Azure.")

    # HDFS Guide
    elif section == "HDFS":
        st.header("🔹 HDFS - Hadoop Distributed File System")
        st.write("Backend users can import big data files from **HDFS**.")
        st.markdown("### Steps to Use HDFS:")
        st.markdown("1️⃣ Select **Backend Upload** → **HDFS**.")
        st.markdown("2️⃣ Enter the following details:")
        st.markdown("   - HDFS Namenode URL (e.g., `http://localhost:50070`)")
        st.markdown("   - HDFS Username")
        st.markdown("3️⃣ Click **Connect to HDFS**.")
        st.markdown("4️⃣ Click **Show Files in HDFS** to browse files.")
        st.markdown("5️⃣ Upload a **CSV or Excel file** and click **Upload to HDFS**.")
        st.markdown("6️⃣ Enter the **HDFS file path** to download data.")

# Run the user guide
if __name__ == "__main__":
    show_backend_user_guide()


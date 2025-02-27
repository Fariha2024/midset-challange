import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import dropbox
import io

from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()

from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header

def upload_local_file():
    uploaded_file = st.file_uploader("Upload a CSV, Excel, JSON, or TXT file", type=["csv", "xlsx", "json", "txt"])
    if uploaded_file:
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        elif file_extension == "xlsx":
            df = pd.read_excel(uploaded_file)
        elif file_extension == "json":
            df = pd.read_json(uploaded_file)
        elif file_extension == "txt":
            df = pd.read_csv(uploaded_file, delimiter="\t")
        st.write("Uploaded Data Preview:")
        st.dataframe(df)

def import_google_sheets():
    st.write("Google Sheets Integration (Requires Setup)")
    credentials = Credentials.from_service_account_file("path_to_credentials.json", scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
    client = gspread.authorize(credentials)
    sheet_url = st.text_input("Enter Google Sheets URL:")
    if st.button("Fetch Data"):
        sheet = client.open_by_url(sheet_url).sheet1
        data = sheet.get_all_records()
        st.dataframe(pd.DataFrame(data))

def import_from_dropbox():
    st.write("Dropbox File Import")
    dropbox_access_token = "your_dropbox_access_token"
    dbx = dropbox.Dropbox(dropbox_access_token)
    file_path = st.text_input("Enter Dropbox file path (e.g., /data.csv):")
    if st.button("Fetch File"):
        _, res = dbx.files_download(file_path)
        df = pd.read_csv(io.BytesIO(res.content))
        st.dataframe(df)

def show_frontend_upload():
    st.subheader("Frontend Data Upload & Import")
    option = st.selectbox("Choose Upload Method", ["Upload from Local Device", "Google Sheets", "Dropbox", "Clipboard Paste"])

    if option == "Upload from Local Device":
        upload_local_file()
    elif option == "Google Sheets":
        import_google_sheets()
    elif option == "Dropbox":
        import_from_dropbox()
    elif option == "Clipboard Paste":
        clipboard_data = st.text_area("Paste data here:")
        if st.button("Process"):
            df = pd.read_csv(io.StringIO(clipboard_data))
            st.dataframe(df)
if __name__ == "__main__" or "pages" in __file__:
    show_frontend_upload()

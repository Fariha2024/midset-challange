import streamlit as st
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

def show_azure_blob_options():
    st.subheader("Fetch Data from Azure Blob Storage")
    
    # User input fields for Azure Blob Storage
    connection_string = st.text_input("Enter Azure Storage Connection String:")
    container_name = st.text_input("Enter Container Name:")
    blob_name = st.text_input("Enter Blob Name (File Name):")
    
    if st.button("Fetch Data"):
        try:
            blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            
            # Download the blob content
            stream = blob_client.download_blob().readall()
            df = pd.read_csv(io.BytesIO(stream))
            
            st.write("Fetched Data:")
            st.write(df)
            
        except Exception as e:
            st.error(f"Error: {e}")

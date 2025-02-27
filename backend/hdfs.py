import streamlit as st
from hdfs import InsecureClient

def show_hdfs_options():
    st.subheader("Connect to Hadoop Distributed File System (HDFS)")

    # HDFS Connection Details
    hdfs_url = st.text_input("Enter HDFS Namenode URL (e.g., http://localhost:50070)")
    hdfs_user = st.text_input("Enter HDFS Username:")

    if hdfs_url and hdfs_user:
        client = InsecureClient(hdfs_url, user=hdfs_user)
        st.success("Connected to HDFS!")

        # File Listing
        st.subheader("List HDFS Files")
        if st.button("Show Files in HDFS"):
            try:
                files = client.list('/')
                st.write(files)
            except Exception as e:
                st.error(f"Error listing files: {e}")

        # File Upload
        uploaded_file = st.file_uploader("Upload a file to HDFS")
        if uploaded_file and st.button("Upload to HDFS"):
            try:
                with client.write(f'/{uploaded_file.name}', overwrite=True) as writer:
                    writer.write(uploaded_file.getvalue())
                st.success(f"File {uploaded_file.name} uploaded successfully!")
            except Exception as e:
                st.error(f"Error uploading file: {e}")

        # File Download
        hdfs_filepath = st.text_input("Enter HDFS file path to download:")
        if hdfs_filepath and st.button("Download from HDFS"):
            try:
                with client.read(hdfs_filepath) as reader:
                    content = reader.read()
                st.download_button("Download File", content, file_name=hdfs_filepath.split('/')[-1])
            except Exception as e:
                st.error(f"Error downloading file: {e}")

if __name__ == "__main__":
    show_hdfs_options()

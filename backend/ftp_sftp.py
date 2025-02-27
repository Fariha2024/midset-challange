import streamlit as st
import ftplib
import paramiko
import os

def connect_ftp(host, username, password):
    """Establish FTP connection."""
    try:
        ftp = ftplib.FTP(host)
        ftp.login(username, password)
        return ftp
    except Exception as e:
        st.error(f"FTP Connection Error: {e}")
        return None

def connect_sftp(host, username, password):
    """Establish SFTP connection."""
    try:
        transport = paramiko.Transport((host, 22))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp
    except Exception as e:
        st.error(f"SFTP Connection Error: {e}")
        return None

def list_files_ftp(ftp):
    """List files in the current directory on FTP server."""
    try:
        files = ftp.nlst()
        return files
    except Exception as e:
        st.error(f"Error retrieving FTP file list: {e}")
        return []

def list_files_sftp(sftp):
    """List files in the home directory on SFTP server."""
    try:
        files = sftp.listdir(".")
        return files
    except Exception as e:
        st.error(f"Error retrieving SFTP file list: {e}")
        return []

def download_ftp_file(ftp, filename):
    """Download a file from FTP server."""
    try:
        with open(filename, "wb") as file:
            ftp.retrbinary(f"RETR {filename}", file.write)
        st.success(f"Downloaded {filename} successfully!")
    except Exception as e:
        st.error(f"FTP Download Error: {e}")

def download_sftp_file(sftp, filename):
    """Download a file from SFTP server."""
    try:
        sftp.get(filename, filename)
        st.success(f"Downloaded {filename} successfully!")
    except Exception as e:
        st.error(f"SFTP Download Error: {e}")

def main():
    st.title("FTP/SFTP Data Import")

    connection_type = st.radio("Select Connection Type", ["FTP", "SFTP"])

    host = st.text_input("Server Host")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Connect"):
        if connection_type == "FTP":
            ftp = connect_ftp(host, username, password)
            if ftp:
                st.session_state["ftp"] = ftp
                st.success("Connected to FTP server!")

        elif connection_type == "SFTP":
            sftp = connect_sftp(host, username, password)
            if sftp:
                st.session_state["sftp"] = sftp
                st.success("Connected to SFTP server!")

    if "ftp" in st.session_state or "sftp" in st.session_state:
        if connection_type == "FTP":
            ftp = st.session_state["ftp"]
            files = list_files_ftp(ftp)
        else:
            sftp = st.session_state["sftp"]
            files = list_files_sftp(sftp)

        if files:
            st.subheader("Available Files:")
            selected_file = st.selectbox("Select a file to download", files)
            if st.button("Download"):
                if connection_type == "FTP":
                    download_ftp_file(ftp, selected_file)
                else:
                    download_sftp_file(sftp, selected_file)

if __name__ == "__main__":
    main()

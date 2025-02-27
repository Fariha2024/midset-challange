import streamlit as st
from components.sidebar import show_sidebar  # ✅ Import sidebar
from components.header import show_header  # ✅ Import header

def show_hero_section():
    st.markdown("""
    ### Welcome to Smart Data Tool
    This tool allows you to easily manage, clean, and process your data efficiently.
    Select an upload type below to begin.
    """)

def main():
    st.title("Smart Data Tool")
    
    selected, sub_selected = show_sidebar()  # Display sidebar
    show_header()  # Display header
    show_hero_section()
    
    user_choice = st.radio(
        "Choose your mode:",
        ("Online", "Offline")
    )
    
    if user_choice == "Online":
        st.subheader("Choose Method")
        upload_choice = st.selectbox("Select Upload Type:", ["Frontend", "Backend"])
        
        if upload_choice == "Frontend":
            frontend_feature = st.selectbox("Select Frontend Feature:", [
                "File Upload", "Data Cleaning", "Visualization", "Multi-file Processing", "User Roles & Access",
                "Security & Encryption", "Frontend Workflow Automation"])
        elif upload_choice == "Backend":
            backend_feature = st.selectbox("Select Backend Feature:", [
                "API Integration", "Database Connection", "Cloud Storage", "Real-time Processing", 
                "Support & Reporting", "Backend Workflow Automation"])
    
    elif user_choice == "Offline":
        st.write("You are using the app offline. You can install it on your computer.")
        st.write("To install the app, click the link below to download the installer.")
        st.markdown("[Download Smart Data Tool for Offline Use](#)")  # Replace with actual link
        st.write("Follow the instructions to install the app and use it securely on your PC.")
        st.write("Once installed, run the app locally for secure, offline access to all your data tools.")
    
if __name__ == "__main__":
    main()

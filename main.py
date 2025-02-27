import streamlit as st
import os

# Get the Railway-assigned PORT or default to 8501
PORT = int(os.getenv("PORT", "8501"))

# Set page configuration
st.set_page_config(page_title="Smart Data Tool", layout="wide")

# Sidebar Navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Settings"])

# Header
st.title("Smart Data Tool")
st.write(f"Running on port {PORT}")

# Hero Section
def show_hero_section():
    st.markdown("""
    ### Welcome to Smart Data Tool
    This tool allows you to easily manage, clean, and process your data efficiently.
    Select an upload type below to begin.
    """)

# Main Function
def main():
    show_hero_section()
    
    # Select Online or Offline Mode
    user_choice = st.radio(
        "Choose your mode:",
        ("Online", "Offline")
    )

    if user_choice == "Online":
        st.subheader("Choose Method")
        upload_choice = st.selectbox("Select Upload Type:", ["Frontend", "Backend"])

        if upload_choice == "Frontend":
            frontend_feature = st.selectbox("Select Frontend Feature:", [
                "File Upload", "Data Cleaning", "Visualization", "Multi-file Processing",
                "User Roles & Access", "Security & Encryption", "Frontend Workflow Automation"
            ])
            st.write(f"Selected: {frontend_feature}")

        elif upload_choice == "Backend":
            backend_feature = st.selectbox("Select Backend Feature:", [
                "API Integration", "Database Connection", "Cloud Storage",
                "Real-time Processing", "Support & Reporting", "Backend Workflow Automation"
            ])
            st.write(f"Selected: {backend_feature}")

    elif user_choice == "Offline":
        st.write("You are using the app offline. Install it on your computer.")
        st.markdown("[Download Smart Data Tool for Offline Use](#)")  # Replace with actual link

# Run the app
if __name__ == "__main__":
    main()

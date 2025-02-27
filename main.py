import streamlit as st
import os

PORT = int(os.getenv("PORT", 8501))  # Default to 8501 if PORT is not set

st.title("Smart Data Tool")
st.write(f"Running on port {PORT}")

# Add some basic UI
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Settings"])

if page == "Home":
    st.write("Welcome to Smart Data Tool!")
elif page == "Settings":
    st.write("Settings Page")

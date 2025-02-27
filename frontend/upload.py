import streamlit as st
import pandas as pd


def show_upload_section():
    st.subheader("📤 Upload Data")

    uploaded_file = st.file_uploader("Upload a CSV, Excel, or JSON file", type=["csv", "xlsx", "json"])

    if uploaded_file is not None:
        file_type = uploaded_file.name.split('.')[-1]

        try:
            if file_type == "csv":
                df = pd.read_csv(uploaded_file)
            elif file_type == "xlsx":
                df = pd.read_excel(uploaded_file, engine='openpyxl')
            elif file_type == "json":
                df = pd.read_json(uploaded_file)

            st.success("✅ File uploaded successfully!")
            st.write("### Preview of Uploaded Data:")
            st.dataframe(df.head())

            # Store dataframe in session state for access across components
            st.session_state['uploaded_df'] = df

        except Exception as e:
            st.error(f"❌ Error loading file: {e}")


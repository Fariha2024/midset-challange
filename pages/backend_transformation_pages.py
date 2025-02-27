import streamlit as st
import pandas as pd
from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()
from backendd.backend_transformation import backend_transformation
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))


from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header

def preview_backend_transformation():
    st.title("Backend Data Transformation")

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file:
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "csv":
            data = pd.read_csv(uploaded_file)
        elif file_extension == "xlsx":
            data = pd.read_excel(uploaded_file)

        st.write("Original Data:")
        st.dataframe(data)

        # Apply the backend transformation
        transformed_data = backend_transformation(data)

        st.write("Transformed Data (Backend):")
        st.dataframe(transformed_data)

# Call the function to show the backend transformation preview
if __name__ == "__main__":
    preview_backend_transformation()

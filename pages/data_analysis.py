import streamlit as st
import requests
import json
from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()

import streamlit as st
from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header

BACKEND_URL = "http://127.0.0.1:8000"

def show_data_analysis():
    st.title("Data Analysis & Processing")

    option = st.selectbox("Select Feature", ["Clean Data", "Generate Table", "Linear Regression"])

    data_input = st.text_area("Enter Data (JSON format):", "[]")

    if st.button("Process Data"):
        try:
            data_dict = json.loads(data_input)

            if option == "Clean Data":
                response = requests.post(f"{BACKEND_URL}/clean_data/", json={"data": data_dict})
            elif option == "Generate Table":
                response = requests.post(f"{BACKEND_URL}/generate_table/", json={"data": data_dict})
            elif option == "Linear Regression":
                x_col = st.text_input("Enter X Column Name:")
                y_col = st.text_input("Enter Y Column Name:")
                response = requests.post(f"{BACKEND_URL}/linear_regression/", json={"data": data_dict, "x_col": x_col, "y_col": y_col})

            if response.status_code == 200:
                st.subheader("Response:")
                st.json(response.json())
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    show_data_analysis()

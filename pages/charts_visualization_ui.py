import streamlit as st
import requests
import json

from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()
from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header

BACKEND_URL =  "https://elegant-embrace-production.up.railway.app"                                       #"http://127.0.0.1:8000"

def show_chart_generator():
    st.title("Chart Generator")

    chart_type = st.selectbox("Select Chart Type", ["bar", "line", "scatter"])
    data_input = st.text_area("Enter Data (JSON format):", "[]")
    x_col = st.text_input("Enter X Column Name:")
    y_col = st.text_input("Enter Y Column Name:")

    if st.button("Generate Chart"):
        try:
            data_dict = json.loads(data_input)
            request_data = {"data": data_dict, "chart_type": chart_type, "x_col": x_col, "y_col": y_col}
            response = requests.post(f"{BACKEND_URL}/generate_chart/", json=request_data)

            if response.status_code == 200:
                st.subheader("Response:")
                st.json(response.json())
                # Handle displaying the chart based on response
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    show_chart_generator()

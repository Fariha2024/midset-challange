import streamlit as st
import requests
import pandas as pd
from components.sidebar import show_sidebar  # ✅ Import sidebar
from streamlit_option_menu import option_menu
selected, sub_selected = show_sidebar()
from components.header import show_header  # ✅ Import the reusable header

show_header()  # ✅ Call the function to display the header
# Backend API URL (update if running on a server)
API_BASE_URL = "http://127.0.0.1:8000"

st.title("📊 Data Analysis & Visualization")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data:")
    st.dataframe(df)

    # Convert DataFrame to JSON for API requests
    data_json = df.to_dict(orient="records")

    # Data Cleaning
    if st.button("🧹 Clean Data"):
        response = requests.post(f"{API_BASE_URL}/clean_data/", json={"data": data_json})
        if response.status_code == 200:
            cleaned_data = pd.DataFrame(response.json())
            st.write("### Cleaned Data:")
            st.dataframe(cleaned_data)
        else:
            st.error("Error in data cleaning!")

    # Data Table
    if st.button("📋 Generate Table"):
        response = requests.post(f"{API_BASE_URL}/generate_table/", json={"data": data_json})
        if response.status_code == 200:
            table_data = pd.DataFrame(response.json())
            st.write("### Data Table:")
            st.dataframe(table_data)
        else:
            st.error("Error generating table!")

    # Pivot Table
    st.write("### Pivot Table Options")
    index_col = st.selectbox("Select Index Column", df.columns)
    column_col = st.selectbox("Select Column", df.columns)
    value_col = st.selectbox("Select Values Column", df.columns)

    if st.button("📊 Generate Pivot Table"):
        response = requests.post(
            f"{API_BASE_URL}/generate_pivot/",
            json={"data": data_json, "index": index_col, "columns": column_col, "values": value_col},
        )
        if response.status_code == 200:
            pivot_data = pd.read_json(response.text)
            st.write("### Pivot Table:")
            st.dataframe(pivot_data)
        else:
            st.error("Error generating pivot table!")

    # Linear Regression
    st.write("### Linear Regression")
    x_col = st.selectbox("Select X Column", df.columns)
    y_col = st.selectbox("Select Y Column", df.columns)

    if st.button("📈 Perform Linear Regression"):
        response = requests.post(
            f"{API_BASE_URL}/linear_regression/",
            json={"data": data_json, "x_col": x_col, "y_col": y_col},
        )
        if response.status_code == 200:
            regression_result = response.json()
            st.write(f"**Slope:** {regression_result['slope']}")
            st.write(f"**Intercept:** {regression_result['intercept']}")
        else:
            st.error("Error performing linear regression!")

    # Charts
    st.write("### Chart Visualization")
    chart_type = st.selectbox("Select Chart Type", ["bar", "line", "scatter"])
    x_chart_col = st.selectbox("Select X Column for Chart", df.columns)
    y_chart_col = st.selectbox("Select Y Column for Chart", df.columns)

    if st.button("📊 Generate Chart"):
        response = requests.post(
            f"{API_BASE_URL}/generate_chart/",
            json={"data": data_json, "chart_type": chart_type, "x_col": x_chart_col, "y_col": y_chart_col},
        )
        if response.status_code == 200:
            st.image(response.content)
        else:
            st.error("Error generating chart!")

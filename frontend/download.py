import streamlit as st
import pandas as pd

def download_data(df):
    st.subheader("Download Processed Data")

    file_format = st.radio("Select file format for download:", ["CSV", "Excel", "JSON"])

    if file_format == "CSV":
        csv_data = df.to_csv(index=False)
        st.download_button("Download CSV", csv_data, "processed_data.csv", "text/csv")

    elif file_format == "Excel":
        import io
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Processed Data")
        st.download_button("Download Excel", output.getvalue(), "processed_data.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    elif file_format == "JSON":
        json_data = df.to_json(orient="records", indent=4)
        st.download_button("Download JSON", json_data, "processed_data.json", "application/json")

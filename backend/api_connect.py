import streamlit as st
import requests
import json

BACKEND_URL = "http://127.0.0.1:8000/api_request/"  # Update if needed

def show_api_options():
    st.title("API Connection - Smart Data Tool")
    st.subheader("Connect via API (REST, GraphQL)")

    api_type = st.radio("Select API Type:", ["REST API", "GraphQL API"])

    url = st.text_input("Enter API Endpoint (URL):")
    headers = st.text_area("Enter Headers (JSON format):", "{}")
    method = st.selectbox("Select HTTP Method:", ["GET", "POST", "PUT", "DELETE"])

    if api_type == "REST API":
        body = st.text_area("Enter Request Body (JSON format, if applicable):", "{}")
    elif api_type == "GraphQL API":
        body = st.text_area("Enter GraphQL Query:", "{}")

    if st.button("Send Request"):
        try:
            headers_dict = json.loads(headers)
            body_dict = json.loads(body) if body.strip() else None

            request_data = {
                "url": url,
                "headers": headers_dict,
                "body": body_dict,
                "method": method
            }

            response = requests.post(BACKEND_URL, json=request_data, timeout=10)  # Timeout handling

            if response.status_code == 200:
                st.subheader("Response:")
                try:
                    st.json(response.json())  # Show response in JSON format
                except json.JSONDecodeError:
                    st.text("Received response is not in JSON format.")
                    st.write(response.text)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

        except json.JSONDecodeError:
            st.error("Invalid JSON format in headers or body.")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

if __name__ == "__main__":
    show_api_options()

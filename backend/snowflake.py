import streamlit as st
import snowflake.connector
import pandas as pd

def show_snowflake_options():
    st.subheader("Connect to Snowflake Database")
    
    # User input fields for Snowflake connection
    account = st.text_input("Enter Snowflake Account:")
    user = st.text_input("Enter Snowflake Username:")
    password = st.text_input("Enter Snowflake Password:", type="password")
    warehouse = st.text_input("Enter Warehouse:")
    database = st.text_input("Enter Database:")
    schema = st.text_input("Enter Schema:")
    table = st.text_input("Enter Table Name:")
    
    if st.button("Connect & Fetch Data"):
        try:
            conn = snowflake.connector.connect(
                account=account,
                user=user,
                password=password,
                warehouse=warehouse,
                database=database,
                schema=schema
            )
            
            query = f"SELECT * FROM {table} LIMIT 10"
            df = pd.read_sql(query, conn)
            st.write("Fetched Data:")
            st.write(df)
            
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")

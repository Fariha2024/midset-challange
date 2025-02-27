import streamlit as st
import mysql.connector
import psycopg2
from pymongo import MongoClient
from mysql.connector import Error
from psycopg2 import OperationalError


# Database Connection Function
def connect_to_mysql(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            return connection
    except Error as e:
        return f"Error: {e}"


def connect_to_postgresql(host, user, password, database):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=database
        )
        return connection
    except OperationalError as e:
        return f"Error: {e}"


def connect_to_mongodb(uri, database):
    try:
        client = MongoClient(uri)
        db = client[database]
        return db
    except Exception as e:
        return f"Error: {e}"


# Streamlit UI to Select Database
def display_connection_form():
    st.title("Database Connection Setup")

    # Dropdown for database selection
    db_type = st.selectbox("Select Database Type", ["MySQL", "PostgreSQL", "MongoDB"])

    # Connection details input fields
    if db_type == "MySQL":
        host = st.text_input("MySQL Host")
        user = st.text_input("MySQL User")
        password = st.text_input("MySQL Password", type="password")
        database = st.text_input("MySQL Database Name")
        if st.button("Connect to MySQL"):
            result = connect_to_mysql(host, user, password, database)
            if isinstance(result, mysql.connector.connection.MySQLConnection):
                st.success("Successfully connected to MySQL!")
            else:
                st.error(result)

    elif db_type == "PostgreSQL":
        host = st.text_input("PostgreSQL Host")
        user = st.text_input("PostgreSQL User")
        password = st.text_input("PostgreSQL Password", type="password")
        database = st.text_input("PostgreSQL Database Name")
        if st.button("Connect to PostgreSQL"):
            result = connect_to_postgresql(host, user, password, database)
            if isinstance(result, psycopg2.extensions.connection):
                st.success("Successfully connected to PostgreSQL!")
            else:
                st.error(result)

    elif db_type == "MongoDB":
        uri = st.text_input("MongoDB URI")
        database = st.text_input("MongoDB Database Name")
        if st.button("Connect to MongoDB"):
            result = connect_to_mongodb(uri, database)
            if isinstance(result, MongoClient):
                st.success("Successfully connected to MongoDB!")
            else:
                st.error(result)


# Run the display function to show the UI
if __name__ == "__main__":
    display_connection_form()

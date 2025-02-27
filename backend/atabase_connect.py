import streamlit as st
import pymysql
import psycopg2
from pymongo import MongoClient
import pandas as pd

def connect_mysql(host, user, password, database):
    try:
        conn = pymysql.connect(host=host, user=user, password=password, database=database)
        st.success("✅ Connected to MySQL!")
        return conn
    except Exception as e:
        st.error(f"❌ MySQL Connection Failed: {e}")
        return None

def connect_postgres(host, user, password, database):
    try:
        conn = psycopg2.connect(host=host, user=user, password=password, dbname=database)
        st.success("✅ Connected to PostgreSQL!")
        return conn
    except Exception as e:
        st.error(f"❌ PostgreSQL Connection Failed: {e}")
        return None

def connect_mongodb(uri, database):
    try:
        client = MongoClient(uri)
        db = client[database]
        st.success("✅ Connected to MongoDB!")
        return db
    except Exception as e:
        st.error(f"❌ MongoDB Connection Failed: {e}")
        return None

def show_database_options():
    st.title("Database Connection - Smart Data Tool")
    db_type = st.radio("Select Database Type:", ["MySQL", "PostgreSQL", "MongoDB"])

    if db_type == "MySQL" or db_type == "PostgreSQL":
        host = st.text_input("Host (e.g., localhost or IP):")
        user = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        database = st.text_input("Database Name:")

        if st.button("Connect"):
            if db_type == "MySQL":
                conn = connect_mysql(host, user, password, database)
            else:
                conn = connect_postgres(host, user, password, database)

            if conn:
                st.success(f"🎉 Successfully connected to {db_type}!")

    elif db_type == "MongoDB":
        uri = st.text_input("MongoDB URI (e.g., mongodb://localhost:27017):")
        database = st.text_input("Database Name:")

        if st.button("Connect"):
            db = connect_mongodb(uri, database)
            if db:
                st.success("🎉 Successfully connected to MongoDB!")

if __name__ == "__main__":
    show_database_options()


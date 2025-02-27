import streamlit as st
from google.cloud import bigquery

# Function to query public datasets from Google BigQuery
def show_bigquery_options():
    st.subheader("Query Google BigQuery Public Datasets")
    
    # Allow users to enter a custom SQL query
    query = st.text_area("Enter your SQL query (for public datasets):", 
                         "SELECT name, SUM(number) as total_births FROM `bigquery-public-data.usa_names.usa_1910_2013` GROUP BY name ORDER BY total_births DESC LIMIT 10")
    
    if st.button("Run Query"):
        try:
            # Create a BigQuery client without authentication
            client = bigquery.Client.create_anonymous_client()
            
            # Run the query
            query_job = client.query(query)
            df = query_job.to_dataframe()
            
            # Display results
            st.write("### Query Results:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error running query: {e}")

# Call function to display BigQuery options
if __name__ == "__main__":
    show_bigquery_options()

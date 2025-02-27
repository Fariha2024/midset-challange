import pandas as pd
import numpy as np

# Placeholder for the enrichment function (for demonstration purposes)
def fetch_enrichment_data(external_id):
    # Implement logic to fetch enrichment data based on external_id
    # Example: returning a dummy value for demonstration
    return f"Enriched data for {external_id}"

def backend_transformation(data):
    # Example of aggregation (e.g., summing up values)
    if 'category' in data.columns and 'amount' in data.columns:
        data_agg = data.groupby('category').agg({'amount': 'sum'}).reset_index()
        return data_agg

    # Normalization example (scaling values to a range between 0 and 1)
    if 'amount' in data.columns:
        data['normalized_amount'] = (data['amount'] - data['amount'].min()) / (data['amount'].max() - data['amount'].min())

    # Handling missing values with mean or median
    if 'amount' in data.columns and data['amount'].isnull().any():
        data['amount'].fillna(data['amount'].mean(), inplace=True)

    # Example of data enrichment via API (e.g., adding external info)
    # Assuming a function `fetch_enrichment_data` is implemented elsewhere for external enrichment
    if 'external_id' in data.columns:
        data['enriched_data'] = data['external_id'].apply(lambda x: fetch_enrichment_data(x))

    # Column merging example (combine 'address' and 'city' into 'full_address')
    if 'address' in data.columns and 'city' in data.columns:
        data['full_address'] = data['address'] + ', ' + data['city']

    # Apply formula for advanced calculation
    if 'quantity' in data.columns and 'unit_price' in data.columns:
        data['total_cost'] = data['quantity'] * data['unit_price']

    # Category mapping (for mapping numeric categories to textual labels)
    category_map = {1: 'Beginner', 2: 'Intermediate', 3: 'Expert'}
    if 'level' in data.columns:
        data['level'] = data['level'].map(category_map)

    return data

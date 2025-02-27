import pandas as pd

def frontend_transformation(data):
    # Example of transforming date format
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

    # Example of changing text to uppercase
    if 'text_column' in data.columns:
        data['text_column'] = data['text_column'].str.upper()

    # Example of removing unwanted characters (updated to avoid deprecation warning)
    if 'name' in data.columns:
        data['name'] = data['name'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=False)

    # Column splitting (splitting 'full_name' into 'first_name' and 'last_name')
    if 'full_name' in data.columns:
        data[['first_name', 'last_name']] = data['full_name'].str.split(' ', expand=True)

    # Apply formula (e.g., calculate profit)
    if 'revenue' in data.columns and 'cost' in data.columns:
        data['profit'] = data['revenue'] - data['cost']

    # Category mapping (mapping numeric categories to text)
    category_map = {1: 'Low', 2: 'Medium', 3: 'High'}
    if 'category' in data.columns:
        data['category'] = data['category'].map(category_map)

    # Merge data (example of merging with another dataset)
    if 'merge_column' in data.columns:
        # Assuming you have another dataframe 'other_data' to merge with
        other_data = pd.DataFrame({'merge_column': [1, 2, 3], 'extra_info': ['A', 'B', 'C']})
        data = pd.merge(data, other_data, on='merge_column', how='left')

    return data

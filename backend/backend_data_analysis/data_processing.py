import pandas as pd
import json

def clean_data(data):
    """Cleans data by dropping rows with missing values."""
    try:
        df = pd.DataFrame(data)
        df = df.dropna()
        return df.to_dict(orient='records')
    except Exception as e:
        return {"error": str(e)}

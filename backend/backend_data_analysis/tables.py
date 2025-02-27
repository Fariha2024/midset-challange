import pandas as pd

def generate_data_table(data):
    """Generates JSON representation of a data table."""
    try:
        df = pd.DataFrame(data)
        return df.to_dict(orient='records')
    except Exception as e:
        return {"error": str(e)}

def generate_pivot_table(data, index, columns, values):
    """Generates a pivot table."""
    try:
        df = pd.DataFrame(data)
        pivot_table = pd.pivot_table(df, values=values, index=index, columns=columns, aggfunc='sum')
        return pivot_table.to_dict()
    except Exception as e:
        return {"error": str(e)}

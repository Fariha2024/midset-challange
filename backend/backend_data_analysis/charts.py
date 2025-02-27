import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def generate_chart(data, chart_type, x_col, y_col=None):
    """Generates a chart image encoded in base64 format."""
    try:
        df = pd.DataFrame(data)

        if x_col not in df.columns or (y_col and y_col not in df.columns):
            return {"error": "Invalid column names provided."}

        plt.figure(figsize=(8, 5))
        img = io.BytesIO()  # Buffer to store image

        if chart_type == "bar":
            sns.barplot(x=df[x_col], y=df[y_col])
        elif chart_type == "line":
            sns.lineplot(x=df[x_col], y=df[y_col])
        elif chart_type == "scatter":
            sns.scatterplot(x=df[x_col], y=df[y_col])
        elif chart_type == "histogram":
            sns.histplot(df[x_col], kde=True)
        else:
            return {"error": "Invalid chart type."}

        plt.xlabel(x_col)
        if y_col:
            plt.ylabel(y_col)
        plt.title(f"{chart_type.capitalize()} Chart")

        plt.savefig(img, format="png")  # Save the chart to buffer
        plt.close()
        img.seek(0)
        
        # Convert image to base64 encoding
        encoded_img = base64.b64encode(img.read()).decode("utf-8")
        return {"chart": encoded_img}

    except Exception as e:
        return {"error": str(e)}

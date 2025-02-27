import pandas as pd
from sklearn.linear_model import LinearRegression

def linear_regression(data, x_col, y_col):
    """Performs linear regression and returns slope & intercept."""
    try:
        df = pd.DataFrame(data)
        X = df[[x_col]].values.reshape(-1, 1)
        y = df[y_col].values.reshape(-1, 1)
        model = LinearRegression()
        model.fit(X, y)
        return {"slope": model.coef_[0][0], "intercept": model.intercept_[0]}
    except Exception as e:
        return {"error": str(e)}

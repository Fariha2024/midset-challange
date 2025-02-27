from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional


from backend.backend_data_analysis.charts import generate_chart
from backend.backend_data_analysis.data_processing import clean_data
from backend.backend_data_analysis.tables import generate_data_table, generate_pivot_table
from backend.backend_data_analysis.trends import linear_regression


app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Data Model for Validation
class DataRequest(BaseModel):
    data: List[dict]

class ChartRequest(DataRequest):
    chart_type: str
    x_col: str
    y_col: Optional[str] = None

class PivotRequest(DataRequest):
    index: str
    columns: str
    values: str

class RegressionRequest(DataRequest):
    x_col: str
    y_col: str

@app.get("/")
def home():
    return {"message": "Welcome to Data Analysis API"}

@app.post("/clean_data/")
def api_clean_data(request: DataRequest):
    try:
        return clean_data(request.data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_table/")
def api_generate_data_table(request: DataRequest):
    try:
        return generate_data_table(request.data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_pivot/")
def api_generate_pivot(request: PivotRequest):
    try:
        return generate_pivot_table(request.data, request.index, request.columns, request.values)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/linear_regression/")
def api_linear_regression(request: RegressionRequest):
    try:
        return linear_regression(request.data, request.x_col, request.y_col)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_chart/")
def api_generate_chart(request: ChartRequest):
    try:
        return generate_chart(request.data, request.chart_type, request.x_col, request.y_col)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

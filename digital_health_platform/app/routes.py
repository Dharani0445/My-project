from fastapi import APIRouter, UploadFile, File
import pandas as pd
from fastapi.responses import JSONResponse
from io import BytesIO

router = APIRouter()

@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        return JSONResponse(status_code=400, content={"message": "Only CSV files are accepted."})

    contents = await file.read()
    df = pd.read_csv(BytesIO(contents))
    return {"preview": df.head().to_dict(orient="records")}

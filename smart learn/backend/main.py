from fastapi import FastAPI
from pydantic import BaseModel
from backend.nlp_engine import get_adaptive_response

app = FastAPI()

class RequestData(BaseModel):
    question: str
    context: str

@app.post("/get_response/")
def get_response(data: RequestData):
    answer = get_adaptive_response(data.question, data.context)
    return {"response": answer}

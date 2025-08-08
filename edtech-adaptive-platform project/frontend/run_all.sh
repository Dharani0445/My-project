#!/bin/bash

# Run FastAPI backend
cd backend
uvicorn main:app --reload --port 8000 &
cd ..

# Run Streamlit frontend
cd frontend
streamlit run app.py

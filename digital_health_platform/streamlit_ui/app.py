import streamlit as st
import pandas as pd
import requests

st.title("Upload CSV and Get Preview from FastAPI")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Show local preview immediately (optional)
    df = pd.read_csv(uploaded_file)
    st.write("Local Preview (first 5 rows):")
    st.write(df.head())

    # Reset file pointer to start (so it can be read again)
    uploaded_file.seek(0)

    if st.button("Send to FastAPI"):
        files = {"file": (uploaded_file.name, uploaded_file, "text/csv")}
        try:
            response = requests.post("http://127.0.0.1:8000/upload-csv/", files=files)
            if response.status_code == 200:
                data = response.json()
                st.write("FastAPI Preview (first 5 rows):")
                st.write(pd.DataFrame(data["preview"]))
            else:
                st.error(f"Error from FastAPI: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to FastAPI: {e}")

import streamlit as st
import requests

st.title("📚 SmartLearn - Adaptive Learning Assistant")

context = st.text_area("Enter your study material:")
user_input = st.text_input("Ask a question:")

if st.button("Get Answer") and context and user_input:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "http://localhost:8000/get_response/",
                json={"question": user_input, "context": context}
            )
            if response.status_code == 200:
                st.success("Answer: " + response.json()['response'])
            else:
                st.error("❌ Error from backend: " + response.text)
        except Exception as e:
            st.error(f"❌ Request failed: {str(e)}")

def get_adaptive_response(user_input: str, context: str) -> str:
    if not context.strip():
        context = "This is a smart learning assistant. Please provide study material."
    result = qa_pipeline(question=user_input, context=context)
    return result['answer']

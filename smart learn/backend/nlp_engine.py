from backend.model import get_answer

def get_adaptive_response(user_input: str, context: str) -> str:
    if not context.strip():
        context = "Please provide study material or context for the question."
    return get_answer(context, user_input)

from config import MODEL_NAME, TEMPERATURE


class LLMService:
    def __init__(self):
        self.model = MODEL_NAME
        self.temperature = TEMPERATURE

    def generate_response(self, prompt):
        """
        Placeholder function for LLM response.
        Will connect to OpenAI later.
        """
        return f"Generated response for: {prompt}"
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Generates embeddings using sentence-transformers.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        return self.model.encode(texts)
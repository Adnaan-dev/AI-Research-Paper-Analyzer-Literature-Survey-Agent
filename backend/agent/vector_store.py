import chromadb


class VectorStore:
    """
    Stores embeddings using ChromaDB.
    """

    def __init__(self, collection_name="research_papers"):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(collection_name)

    def add_documents(self, ids, embeddings, documents):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents
        )

    def query(self, query_embedding, n_results=5):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
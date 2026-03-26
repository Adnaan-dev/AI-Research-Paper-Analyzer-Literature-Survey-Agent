import chromadb
import hashlib


class VectorStore:
    """
    Stores embeddings using ChromaDB with idempotent indexing.
    Prevents duplicate storage of the same chunks across runs.
    """

    def __init__(self, collection_name="research_papers"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(collection_name)

    def _generate_chunk_id(self, text):
        """
        Generate unique ID for each chunk using MD5 hash.
        Ensures duplicate chunks are not indexed twice.
        """
        return hashlib.md5(text.encode()).hexdigest()

    def add_documents(self, embeddings, documents):
        ids = [self._generate_chunk_id(doc) for doc in documents]

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
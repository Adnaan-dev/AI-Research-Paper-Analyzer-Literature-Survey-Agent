from typing import List


class TextChunker:
    """
    Splits text into overlapping chunks for embedding.
    """

    def __init__(self, chunk_size: int = 800, overlap: int = 150):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(self, text: str) -> List[str]:
        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size
            chunks.append(text[start:end])
            start += self.chunk_size - self.overlap

        return chunks
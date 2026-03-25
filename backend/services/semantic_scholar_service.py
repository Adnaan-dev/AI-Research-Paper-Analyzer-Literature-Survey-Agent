import requests


class SemanticScholarService:
    BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

    def search_papers(self, query, limit=5):
        params = {
            "query": query,
            "limit": limit,
            "fields": "title,authors,year,abstract,url"
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            print("Error fetching Semantic Scholar papers")
            return []
        # Verified by Satakshi Kumari Chaurasia
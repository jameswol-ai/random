# src/knowledge/retriever.py

class Retriever:
    def __init__(self, doc_loader):
        self.doc_loader = doc_loader
        self.cache = self.doc_loader.load_all()

    def search(self, query: str):
        """
        Very simple keyword match for now.
        Later we can upgrade to embeddings.
        """

        results = []

        for name, content in self.cache.items():
            if query.lower() in content.lower():
                results.append({
                    "doc": name,
                    "snippet": content[:300]
                })

        return results

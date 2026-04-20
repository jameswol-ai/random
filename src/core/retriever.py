import re

class SimpleRetriever:
    def __init__(self, documents: dict):
        self.documents = documents  # {"doc_name": "content"}

    def search(self, query, top_k=2):
        scores = []

        query_words = set(re.findall(r"\w+", query.lower()))

        for name, content in self.documents.items():
            content_words = set(re.findall(r"\w+", content.lower()))
            score = len(query_words & content_words)

            scores.append((name, content, score))

        # sort by relevance
        scores.sort(key=lambda x: x[2], reverse=True)

        return scores[:top_k]

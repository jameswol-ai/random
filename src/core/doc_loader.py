import os

class DocLoader:
    def __init__(self, base_path="docs"):
        self.base_path = base_path
        self.cache = {}

    def load_doc(self, relative_path):
        full_path = os.path.join(self.base_path, relative_path)

        if full_path in self.cache:
            return self.cache[full_path]

        try:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.cache[full_path] = content
                return content
        except FileNotFoundError:
            return ""

    def load_category(self, category_path):
        folder = os.path.join(self.base_path, category_path)
        combined = ""

        for file in os.listdir(folder):
            if file.endswith(".md"):
                combined += self.load_doc(f"{category_path}/{file}") + "\n\n"

        return combined

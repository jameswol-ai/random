# src/core/context.py

class Context:
    def __init__(self):
        self.data = {
            "project_history": []
        }

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def add_history(self, entry):
        self.data["project_history"].append(entry)

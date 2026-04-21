# src/core/memory.py

class Memory:
    def __init__(self):
        self.history = []

    def record(self, entry):
        self.history.append(entry)

    def get_all(self):
        return self.history

    def summarize(self):
        return {
            "total_runs": len(self.history),
            "last": self.history[-1] if self.history else None
        }

# src/core/system_variant.py

class SystemVariant:
    def __init__(self, name, config, score=0.5):
        self.name = name
        self.config = config
        self.score = score

    def update_score(self, new_score):
        self.score = (self.score + new_score) / 2

    def snapshot(self):
        return {
            "name": self.name,
            "config": self.config,
            "score": self.score
        }

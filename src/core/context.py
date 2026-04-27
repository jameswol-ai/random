# src/core/context.py

from dataclasses import dataclass, field

@dataclass
class Context:
    data: dict = field(default_factory=dict)
    history: list = field(default_factory=list)

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def remember_run(self, summary):
        self.history.append(summary)

# src/core/universe.py

class Universe:
    def __init__(self, name, ecosystem):
        self.name = name
        self.ecosystem = ecosystem
        self.history = []

    def step(self):
        result = self.ecosystem.run_cycle()
        self.history.append(result)
        return result

    def snapshot(self):
        return {
            "name": self.name,
            "cycles": len(self.history),
            "latest": self.history[-1] if self.history else None
        }

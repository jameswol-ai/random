# src/core/architecture_memory.py

class ArchitectureMemory:
    def __init__(self):
        self.snapshots = []

    def record(self, system_state):
        self.snapshots.append(system_state)

    def latest(self):
        return self.snapshots[-1] if self.snapshots else None

    def analyze_trends(self):
        return {
            "total_snapshots": len(self.snapshots),
            "growth": "increasing" if len(self.snapshots) > 3 else "initial"
        }

# src/core/meta_observer.py

class MetaObserver:
    def __init__(self):
        self.universes = []

    def register(self, universe):
        self.universes.append(universe)

    def observe_all(self):
        return [
            u.snapshot() for u in self.universes
        ]

    def detect_emergence(self):
        return {
            "active_universes": len(self.universes),
            "status": "expanding" if len(self.universes) > 2 else "seed_stage"
        }

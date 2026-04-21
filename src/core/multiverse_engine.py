# src/core/multiverse_engine.py

from src.core.universe_generator import UniverseGenerator
from src.core.meta_observer import MetaObserver
from src.core.migration_engine import MigrationEngine

class MultiverseEngine:
    def __init__(self):
        self.generator = UniverseGenerator()
        self.observer = MetaObserver()
        self.migrator = MigrationEngine()

        # 🌌 create initial universes
        for _ in range(2):
            u = self.generator.create_universe()
            self.observer.register(u)

    def step(self):
        results = []

        # 🌱 evolve each universe independently
        for u in self.observer.universes:
            results.append(u.step())

        # 🔀 cross-universe interaction
        if len(self.observer.universes) >= 2:
            migration = self.migrator.migrate(
                self.observer.universes[0],
                self.observer.universes[1]
            )
            results.append(migration)

        return {
            "universes": self.observer.observe_all(),
            "interaction": results,
            "meta": self.observer.detect_emergence()
        }

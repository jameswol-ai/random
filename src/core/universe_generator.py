# src/core/universe_generator.py

from src.core.ecosystem_engine import EcosystemEngine
from src.core.universe import Universe

class UniverseGenerator:
    def __init__(self):
        self.count = 0

    def create_universe(self):
        self.count += 1

        ecosystem = EcosystemEngine()

        return Universe(
            name=f"RANDOM-UNIVERSE-{self.count}",
            ecosystem=ecosystem
        )

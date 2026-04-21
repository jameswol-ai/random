# src/core/evolution_manager.py

import random
from src.core.system_variant import SystemVariant


class EvolutionManager:
    def __init__(self):
        self.population = [
            SystemVariant("RANDOM-A", {"complexity": 1}),
            SystemVariant("RANDOM-B", {"complexity": 2})
        ]

    def evaluate(self):
        for variant in self.population:
            # 🧠 fake evaluation signal (replace with real metrics later)
            variant.update_score(random.uniform(0.4, 0.95))

    def select_top(self):
        return sorted(self.population, key=lambda v: v.score, reverse=True)[:2]

    def breed(self, parent_a, parent_b):
        new_config = {
            "complexity": (parent_a.config["complexity"] + parent_b.config["complexity"]) // 2 + 1
        }

        child = SystemVariant(
            name=f"{parent_a.name}-{parent_b.name}-child",
            config=new_config,
            score=0.5
        )

        self.population.append(child)
        return child

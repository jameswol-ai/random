# src/core/ecosystem_engine.py

from src.core.evolution_manager import EvolutionManager
from src.core.system_mutator import SystemMutator


class EcosystemEngine:
    def __init__(self):
        self.evolver = EvolutionManager()
        self.mutator = SystemMutator()

    def run_cycle(self):
        # 🧠 evaluate all systems
        self.evolver.evaluate()

        # 🏆 select best performers
        top = self.evolver.select_top()

        # 🔀 breed new system
        child = self.evolver.breed(top[0], top[1])

        # 🧬 mutate child
        mutated = self.mutator.mutate(child)

        return {
            "population": [v.snapshot() for v in self.evolver.population],
            "new_variant": mutated.snapshot()
        }

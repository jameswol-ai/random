# src/core/genetic_crossover.py

class GeneticCrossover:
    def combine(self, system_a, system_b):
        return {
            "architecture_type": f"{system_a.config['architecture_type']} ⊕ {system_b.config['architecture_type']}",
            "reasoning_depth": max(
                system_a.config["reasoning_depth"],
                system_b.config["reasoning_depth"]
            ) + 1,
            "agent_structure": "hybrid_emergent"
        }

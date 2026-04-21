# src/core/idea_explorer.py

import random

class IdeaExplorer:
    def __init__(self):
        self.concepts = [
            "hierarchical reasoning",
            "parallel debate",
            "constraint relaxation",
            "self-reflection loop",
            "probabilistic architecture",
            "emergent agent behavior"
        ]

    def explore(self):
        # 🧠 combine unrelated concepts into new structures
        a = random.choice(self.concepts)
        b = random.choice(self.concepts)

        return f"{a} + {b} hybrid reasoning model"

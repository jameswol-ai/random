# src/core/council_engine.py

class CouncilEngine:
    def __init__(self, agent):
        self.agent = agent

    def deliberate(self, context):
        roles = [
            "architect",
            "structural_engineer",
            "climate_specialist",
            "compliance_officer"
        ]

        opinions = []

        # 🧠 parallel-style reasoning (simulated loop)
        for role in roles:
            opinion = self.agent.run(role, context)
            opinions.append(opinion)

        return self._resolve(opinions)

    def _resolve(self, opinions):
        # ⚖️ weighted voting system
        best = max(opinions, key=lambda x: x["score"])

        return {
            "final_decision": best["proposal"],
            "winner": best["agent"],
            "all_opinions": opinions
        }

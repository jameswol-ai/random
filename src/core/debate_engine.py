# src/core/debate_engine.py

from src.core.mutation_engine import MutationEngine


class DebateEngine:
    def __init__(self, agent):
        self.agent = agent
        self.mutator = MutationEngine()

    def run_debate(self, context):
        roles = [
            "architect",
            "structural_engineer",
            "climate_specialist",
            "compliance_officer"
        ]

        idea = self.agent.debate("architect", context, [])

        conversation = [idea]

        # 🔁 debate + mutation cycle
        for i in range(2):
            for role in roles[1:]:
                response = self.agent.debate(role, context, conversation)
                conversation.append(response)

                # 🧬 idea evolves after critique
                idea["message"] = self.mutator.mutate(
                    idea["message"],
                    response["message"]
                )

        return {
            "evolution_trace": conversation,
            "final_design": idea
        }

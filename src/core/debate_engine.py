# src/core/debate_engine.py
from src.core.agent_metrics import AgentMetrics
from src.core.memory import Memory


class DebateEngine:
    def __init__(self, agent):
        self.agent = agent
        self.metrics = AgentMetrics()
        self.memory = Memory()

    def run_debate(self, context):
        roles = list(self.metrics.scores.keys())

        conversation = []

        # 🧠 debate phase
        for role in roles:
            response = self.agent.debate(role, context, conversation)
            conversation.append(response)

        # 📊 evaluation phase
        self._evaluate(conversation)

        # 🧠 store memory
        self.memory.record({
            "input": context.get("input"),
            "conversation": conversation
        })

        return {
            "conversation": conversation,
            "metrics": self.metrics.scores
        }

    def _evaluate(self, conversation):
        for item in conversation:
            score = item.get("score", 0.5)

            self.metrics.update(
                item["speaker"],
                score
            )

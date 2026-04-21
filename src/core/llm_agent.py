# src/core/llm_agent.py

class LLMAgent:
    def __init__(self, llm_client):
        self.llm = llm_client

    def run(self, role, context):
        response = self.llm.generate(role, context)

        # 🧠 convert into council opinion format
        return {
            "agent": role,
            "proposal": response.get("output"),
            "score": response.get("confidence", 0.5),
            "reasoning": response.get("critique", "No critique provided")
        }

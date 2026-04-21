# src/core/mock_llm.py

class MockLLM:
    def generate(self, system, user):
        return {
            "output": f"[LLM RESPONSE BASED ON ROLE]\n{user[:200]}...",
            "confidence": 0.8,
            "critique": "Mock critique generated",
            "signals": {
                "source": "mock_llm"
            }
        }

# src/core/llm_agent.py

from src.models.prompt_models import AGENT_PROMPTS

class LLMAgent:
    def __init__(self, llm_client):
        self.llm = llm_client

    def run(self, role, context):
        prompt = AGENT_PROMPTS.get(role, "")

        input_text = context.get("input", "")
        knowledge = context.get("knowledge", [])

        system_message = prompt

        user_message = f"""
Project Input:
{input_text}

Relevant Knowledge:
{knowledge}

Last Output:
{context.get('last_output')}
"""

        response = self.llm.generate(system_message, user_message)

        return response

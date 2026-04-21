# src/core/engine.py

from src.core.mock_llm import MockLLM
from src.core.llm_agent import LLMAgent
from src.core.debate_engine import DebateEngine


class WorkflowEngine:
    def __init__(self):
        self.llm = MockLLM()
        self.agent = LLMAgent(self.llm)
        self.debate = DebateEngine(self.agent)

        self.context = {}

    def set_context(self, key, value):
        self.context[key] = value

    def run_workflow(self, workflow_name=None):
        return self.debate.run_debate(self.context)

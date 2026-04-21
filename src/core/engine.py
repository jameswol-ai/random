# src/core/engine.py

from src.core.mock_llm import MockLLM
from src.core.llm_agent import LLMAgent
from src.core.firm_engine import FirmEngine


class WorkflowEngine:
    def __init__(self):
        self.llm = MockLLM()
        self.agent = LLMAgent(self.llm)
        self.firm = FirmEngine(self.agent)

        self.context = {}

    def set_context(self, key, value):
        self.context[key] = value

    def run_workflow(self, workflow_name=None):
        # 🏛️ ignore linear workflows for now
        # we run “firm intelligence mode”

        return self.firm.run_firm_cycle(self.context)

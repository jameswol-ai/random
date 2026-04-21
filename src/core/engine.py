# src/core/engine.py

from src.core.workflow_loader import WorkflowLoader
from src.core.mock_llm import MockLLM
from src.core.llm_agent import LLMAgent
from src.core.debate_engine import DebateEngine


class WorkflowEngine:
    def __init__(self):
        self.loader = WorkflowLoader()

        self.llm = MockLLM()
        self.agent = LLMAgent(self.llm)
        self.debate = DebateEngine(self.agent)

        self.context = {}

    def set_context(self, key, value):
        self.context[key] = value

    def run_workflow(self, workflow_name):

        workflow = self.loader.load(workflow_name)

        # 🧠 inject agent into context
        self.context["agent"] = self.agent

        # 🔥 run debate-based reasoning instead of simple pipeline
        result = self.debate.run_debate(self.context)

        return result

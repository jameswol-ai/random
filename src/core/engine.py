# src/core/engine.py

from src.core.meta_controller import MetaController
from src.core.workflow_evolver import WorkflowEvolver
from src.core.debate_engine import DebateEngine
from src.core.llm_agent import LLMAgent
from src.core.mock_llm import MockLLM
from src.core.agent_metrics import AgentMetrics


class WorkflowEngine:
    def __init__(self):
        self.llm = MockLLM()
        self.metrics = AgentMetrics()
        self.agent = LLMAgent(self.llm, self.metrics)

        self.debate = DebateEngine(self.agent)

        self.meta = MetaController()
        self.evolver = WorkflowEvolver()

        self.context = {}

    def set_context(self, key, value):
        self.context[key] = value

    def run_workflow(self, workflow_name=None):

        result = self.debate.run_debate(self.context)

        # 🧠 meta observation
        self.meta.observe(result)

        avg = self.meta.evaluate()
        decision = self.meta.suggest_changes(avg)

        # 🔁 self-rewrite step
        if decision["action"] != "maintain":
            self.evolver.evolve(decision)

        return {
            "result": result,
            "system_decision": decision,
            "avg_performance": avg
        }

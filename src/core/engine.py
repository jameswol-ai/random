# src/core/engine.py

from src.core.multiverse_engine import MultiverseEngine


class WorkflowEngine:
    def __init__(self):
        self.multiverse = MultiverseEngine()

    def run_workflow(self, workflow_name=None):
        return self.multiverse.step()


class WorkflowEngine:
    def __init__(self):
        self.ecosystem = EcosystemEngine()
        self.context = {}

    def set_context(self, key, value):
        self.context[key] = value

    def run_workflow(self, workflow_name=None):
        # 🌱 run evolutionary cycle instead of single system execution
        return self.ecosystem.run_cycle()

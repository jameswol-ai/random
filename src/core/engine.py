# src/core/engine.py

from src.core.workflow_loader import WorkflowLoader
from src.core.dispatcher import Dispatcher
from src.knowledge.doc_loader import DocLoader
from src.knowledge.retriever import Retriever


class WorkflowEngine:
    def __init__(self):
        self.loader = WorkflowLoader()
        self.dispatcher = Dispatcher()

        self.doc_loader = DocLoader()
        self.retriever = Retriever(self.doc_loader)

        self.context = {}

    def set_context(self, key, value):
        self.context[key] = value

    def run_workflow(self, workflow_name: str):

        # 🧠 inject knowledge (context-aware memory)
        input_text = self.context.get("input", "")
        self.context["knowledge"] = self.retriever.search(input_text)

        workflow = self.loader.load(workflow_name)

        results = self.dispatcher.execute(
            workflow,
            self.context
        )

        return {
            "workflow": workflow["name"],
            "trace": results,
            "final": results[-1] if results else None
        }

from src.core.context import WorkflowContext
from src.core.dispatcher import StageDispatcher


class WorkflowEngine:
    """
    The central engine that runs architectural workflows step-by-step.
    Think of it as the project manager of the AI architecture system.
    """

    def __init__(self, workflow_definition):
        self.workflow = workflow_definition
        self.context = WorkflowContext()
        self.dispatcher = StageDispatcher()

    def set_context(self, key, value):
        """Inject initial input into workflow context."""
        self.context.set(key, value)

    def run_workflow(self, workflow_name: str):
        """
        Execute a full workflow (e.g., basic_design, eco_building).
        """

        if workflow_name not in self.workflow:
            raise ValueError(f"Workflow '{workflow_name}' not found")

        steps = self.workflow[workflow_name]

        print(f"\n🚧 Starting workflow: {workflow_name}\n")

        for step in steps:
            stage_name = step["name"]

            print(f"➡️ Running stage: {stage_name}")

            # Dispatch execution to correct stage
            result = self.dispatcher.run_stage(
                stage_name,
                self.context
            )

            # Store result back into shared context
            self.context.set(stage_name, result)

            print(f"✔ Completed: {stage_name}\n")

        print("🏁 Workflow completed.\n")

        return self.context.data

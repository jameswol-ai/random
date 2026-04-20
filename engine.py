# src/core/engine.py

class WorkflowEngine:
    def __init__(self, context):
        self.context = context

    def run_stage(self, stage):
        return stage(self.context)

    def run(self, workflow):
        result = None

        for stage in workflow:
            self.context.set("last_stage", stage.__name__)
            result = self.run_stage(stage)
            self.context.set(stage.__name__, result)

        return result

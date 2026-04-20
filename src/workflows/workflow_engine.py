class WorkflowEngine:
    def __init__(self, workflows: dict):
        self.workflows = workflows
        self.context = {}

    def set_context(self, key, value):
        self.context[key] = value

    def get_context(self, key, default=None):
        return self.context.get(key, default)

    def run_workflow(self, name):
        if name not in self.workflows:
            raise ValueError(f"Workflow '{name}' not found")

        steps = self.workflows[name]

        for step in steps:
            print(f"Running step: {step['name']}")
            result = step["action"](self.context)
            self.context[step["name"]] = result

        return self.context

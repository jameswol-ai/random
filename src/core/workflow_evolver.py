# src/core/workflow_evolver.py

import json

class WorkflowEvolver:
    def __init__(self, path="workflows/basic_design.json"):
        self.path = path

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def save(self, workflow):
        with open(self.path, "w") as f:
            json.dump(workflow, f, indent=2)

    def evolve(self, suggestion):
        workflow = self.load()

        if suggestion["action"] == "simplify_pipeline":
            workflow["graph"] = {
                "architect": {"next": "compliance"},
                "compliance": {"next": "output"},
                "output": {"next": None}
            }

        elif suggestion["action"] == "add_complexity":
            workflow["graph"]["analysis"] = {"next": "output"}

        self.save(workflow)

        return workflow

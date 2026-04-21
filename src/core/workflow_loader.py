# src/core/workflow_loader.py

import json
from src.stages.registry import get_stage


class WorkflowLoader:
    def __init__(self, workflows_path="workflows"):
        self.workflows_path = workflows_path

    def load(self, workflow_name: str):
        path = f"{self.workflows_path}/{workflow_name}.json"

        with open(path, "r") as f:
            raw_workflow = json.load(f)

        return self._build_pipeline(raw_workflow)

    def _build_pipeline(self, raw_workflow):
        """
        Converts:
        ["concept", "analysis", "output"]
        into real callable functions
        """

        pipeline = []

        for stage_name in raw_workflow["stages"]:
            stage_fn = get_stage(stage_name)
            pipeline.append(stage_fn)

        return {
            "name": raw_workflow["name"],
            "pipeline": pipeline
        }

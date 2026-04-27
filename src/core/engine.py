# src/core/engine.py

from typing import Dict, List, Callable, Any

class WorkflowEngine:
    def __init__(self, workflow: Dict, function_registry: Dict[str, Callable]):
        self.workflow = workflow
        self.function_registry = function_registry
        self.context = {}

    def set_context(self, key: str, value: Any):
        self.context[key] = value

    def get_context(self, key: str):
        return self.context.get(key)

    def run_workflow(self, workflow_name: str):
        stages = self.workflow.get(workflow_name, [])
        current_index = 0

        while current_index < len(stages):
            stage = stages[current_index]

            # 🧠 Conditional execution
            if "condition" in stage:
                condition_fn = self.function_registry.get(stage["condition"])
                if condition_fn and not condition_fn(self.context):
                    current_index += 1
                    continue

            # ⚙️ Execute stage
            func = self.function_registry.get(stage["name"])
            if not func:
                raise ValueError(f"Stage function '{stage['name']}' not found")

            result = func(self.context)

            # 🧬 Store result
            if "output_key" in stage:
                self.context[stage["output_key"]] = result

            # 🔀 Dynamic routing
            if "next" in stage:
                next_stage_name = stage["next"]
                current_index = self._find_stage_index(stages, next_stage_name)
                continue

            current_index += 1

        return self.context

    def _find_stage_index(self, stages: List[Dict], name: str):
        for i, stage in enumerate(stages):
            if stage["name"] == name:
                return i
        raise ValueError(f"Stage '{name}' not found")

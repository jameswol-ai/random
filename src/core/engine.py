# src/core/engine.py

from core.conditions import evaluate_condition

from stages import (
    concept_stage,
    climate_check,
    eco_design,
    final_output
)

STAGE_MAP = {
    "concept_stage": concept_stage,
    "climate_check": climate_check,
    "eco_design": eco_design,
    "final_output": final_output
}

class WorkflowEngine:
    def __init__(self, workflow):
        self.workflow = workflow["adaptive_design"]

    def run_workflow(self, ctx):
        results = {}

        for step in self.workflow:
            name = step["name"]

            # 🧠 condition gate
            if "condition" in step:
                if not evaluate_condition(step["condition"], ctx):
                    continue

            func = STAGE_MAP[name]
            output = func(ctx)

            results[step["output_key"]] = output
            ctx[step["output_key"]] = output

        return results

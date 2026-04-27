# src/core/engine.py

from core.context import Context
import core.stages as stages

class WorkflowEngine:
    def __init__(self):
        self.context = Context()

        self.workflow = [
            ("concept_stage", stages.concept_stage),
            ("climate_check", stages.climate_check),
            ("eco_design", stages.eco_design),
        ]

    def run(self):
        log = []

        for name, stage_fn in self.workflow:
            result = stage_fn(self.context)

            if result:
                for k, v in result.items():
                    self.context.set(k, v)

            log.append({
                "stage": name,
                "output": result
            })

        return {
            "final_context": self.context.data,
            "log": log
        }

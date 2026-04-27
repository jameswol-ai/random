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
            try:
                result = stage_fn(self.context)

                if not isinstance(result, dict):
                    result = {"output": result}

                for k, v in result.items():
                    self.context.set(k, v)

                log.append({
                    "stage": name,
                    "output": result,
                    "status": "ok"
                })

            except Exception as e:
                log.append({
                    "stage": name,
                    "error": str(e),
                    "status": "failed"
                })

        return {
            "final_context": self.context.data,
            "log": log
        }

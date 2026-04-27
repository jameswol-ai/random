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
        summary_points = []

        for name, stage_fn in self.workflow:
            try:
                result = stage_fn(self.context)

                if not isinstance(result, dict):
                    result = {"output": result}

                for k, v in result.items():
                    self.context.set(k, v)

                summary_points.append(name)

                log.append({
                    "stage": name,
                    "status": "ok",
                    "output": result
                })

            except Exception as e:
                summary_points.append(f"{name}_failed")

                log.append({
                    "stage": name,
                    "status": "failed",
                    "error": str(e)
                })

        # 🧠 SELF-REFLECTION (this is the “alive” part)
        reflection = self._reflect(summary_points)

        run_summary = {
            "completed_stages": summary_points,
            "reflection": reflection
        }

        self.context.remember_run(run_summary)

        return {
            "summary": run_summary,
            "timeline": log,
            "memory_depth": len(self.context.history),
            "final_context": self.context.data
        }

    def _reflect(self, points):
        success = len([p for p in points if "failed" not in p])
        failed = len(points) - success

        if failed == 0:
            return "System flow is stable. Patterns are consistent."

        if success > failed:
            return "Mostly stable execution with minor turbulence."

        return "System instability detected. Workflow coherence degraded."

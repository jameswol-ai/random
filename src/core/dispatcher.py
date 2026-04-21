# src/core/dispatcher.py

from src.stages.registry import get_stage


class Dispatcher:
    def execute(self, workflow, context):
        graph = workflow["graph"]
        current = workflow["entry"]

        results = []

        while current is not None:
            stage_fn = get_stage(current)

            output = stage_fn(context)
            context["last_output"] = output

            results.append({
                "stage": current,
                "output": output
            })

            # 🧠 refinement loop trigger
            if self._needs_refinement(output):
                current = "refiner"
                continue

            current = graph.get(current, {}).get("next")

        return results

    def _needs_refinement(self, output):
        confidence = output.get("confidence", 1.0)
        return confidence < 0.75

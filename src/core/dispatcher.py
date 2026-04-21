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

            # 🔁 decide next step
            current = self._resolve_next(graph, current, context)

        return results

    def _resolve_next(self, graph, current, context):
        node = graph.get(current, {})

        # 🧠 future upgrade hook: conditional branching
        return node.get("next")


def _resolve_next(self, graph, current, context):
    node = graph.get(current, {})

    last_output = context.get("last_output", "")

    # 🧠 future AI logic hook (rule-based for now)
    if isinstance(last_output, dict):
        if "error" in last_output:
            return "compliance"

    return node.get("next")

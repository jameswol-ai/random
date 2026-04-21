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

            current = self._resolve_next(graph, current, context, output)

        return results

    def _resolve_next(self, graph, current, context, last_output):
        node = graph.get(current, {})

        signals = last_output.get("signals", {})

        # 🧠 intelligent reroute hook
        if signals.get("risk_level") == "unknown":
            return "compliance"

        return node.get("next")

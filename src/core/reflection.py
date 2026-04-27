# src/core/reflection.py

class ReflectionEngine:

    def analyze(self, trace):
        insights = []

        for step in trace:
            if not step["output"]:
                insights.append(f"Stage {step['stage']} produced no output")

        return insights

    def suggest_changes(self, insights):
        changes = []

        for i in insights:
            if "no output" in i:
                stage = i.split(" ")[1]
                changes.append({
                    "action": "remove",
                    "stage": stage
                })

        return changes

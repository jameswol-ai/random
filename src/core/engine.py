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
        story = []
        summary_points = []

        story.append("🧠 Random wakes up. Workflow sequence begins.\n")

        for name, stage_fn in self.workflow:
            try:
                result = stage_fn(self.context)

                if not isinstance(result, dict):
                    result = {"output": result}

                for k, v in result.items():
                    self.context.set(k, v)

                summary_points.append(name)

                line = self._narrate_success(name, result)
                story.append(line)

                log.append({
                    "stage": name,
                    "status": "ok",
                    "output": result
                })

            except Exception as e:
                line = self._narrate_failure(name, str(e))
                story.append(line)

                log.append({
                    "stage": name,
                    "status": "failed",
                    "error": str(e)
                })

        reflection = self._reflect(summary_points)

        story.append("\n🧠 System reflection: " + reflection)
        story.append("📦 Workflow complete. Random returns to idle state.")

        return {
            "story": story,
            "summary": {
                "reflection": reflection
            },
            "timeline": log,
            "final_context": self.context.data
        }

    # 🎭 NARRATION LAYER
    def _narrate_success(self, stage, result):
        if stage == "concept_stage":
            return f"📐 Concept phase stabilized: foundational architecture ideas formed."

        if stage == "climate_check":
            return f"🌍 Climate analysis completed: environmental compatibility assessed."

        if stage == "eco_design":
            return f"🌱 Eco-design resolved: sustainability metrics integrated into structure."

        return f"⚙️ {stage} completed successfully."

    def _narrate_failure(self, stage, error):
        return f"⚠️ {stage} encountered turbulence: {error}"

    # 🧠 REFLECTION ENGINE
    def _reflect(self, points):
        success = len(points)

        if success == len(self.workflow):
            return "System coherence maintained. No structural instability detected."

        return "Partial instability detected. Workflow adapted but not fully optimized."

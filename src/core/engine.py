# src/core/engine.py

from src.core.reflection import ReflectionEngine
from src.core.evolver import WorkflowEvolver

class WorkflowEngine:
    def __init__(self, registry, memory):
        self.registry = registry
        self.memory = memory
        self.reflector = ReflectionEngine()
        self.evolver = WorkflowEvolver()

    def run(self, workflow, context):
        trace = []

        for stage_name in workflow["stages"]:
            stage = self.registry.get_stage(stage_name)

            try:
                context = stage.run(context, self.memory)
            except Exception as e:
                context.add_error(e)

            trace.append({
                "stage": stage_name,
                "output": context.data.copy()
            })

        # 🧠 REFLECTION PHASE
        insights = self.reflector.analyze(trace)

        # 🔁 EVOLUTION PHASE
        changes = self.reflector.suggest_changes(insights)
        workflow = self.evolver.apply(workflow, changes)

        # 💾 SAVE LEARNING
        self.memory.update("last_insights", insights)
        self.memory.update("last_workflow", workflow)

        return context, trace, insights

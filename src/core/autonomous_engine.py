# src/core/autonomous_py

from core.intent import analyze_intent
from core.planner import generate_workflow
from core.engine import WorkflowEngine

class AutonomousArchitect:
    def run(self, ctx):
        # 1. Understand request
        intent = analyze_intent(ctx)
        ctx.update("intent", intent)

        # 2. Generate workflow dynamically
        workflow = generate_workflow(intent)

        # 3. Execute generated workflow
        engine = WorkflowEngine(workflow)

        return engine.run_workflow(ctx)

from src.core.context import Context
from src.core.engine import WorkflowEngine

def stage_one(ctx):
    ctx.set("concept", "Eco-friendly school")
    return "Concept created"

def stage_two(ctx):
    return f"Checked: {ctx.get('concept')}"

context = Context()
engine = WorkflowEngine(context)

workflow = [stage_one, stage_two]

print(engine.run(workflow))
print(context.all())

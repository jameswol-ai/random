from src.core.engine import WorkflowEngine

engine = WorkflowEngine()

engine.set_context(
    "input",
    "Eco-friendly school in tropical climate"
)

result = engine.run_workflow("basic_design")

print("\n".join(result["results"]))
print("\nFINAL OUTPUT:")
print(result["final"])

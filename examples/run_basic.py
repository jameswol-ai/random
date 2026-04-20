from core.engine import WorkflowEngine
from workflows.basic_workflow import architectural_workflow

def run_basic():
    engine = WorkflowEngine(architectural_workflow)

    engine.set_context("input", "Eco-friendly primary school in tropical climate")

    result = engine.run_workflow("basic_design")

    print("\n🏗️ BASIC DESIGN OUTPUT")
    print("======================")
    print(result)


if __name__ == "__main__":
    run_basic()

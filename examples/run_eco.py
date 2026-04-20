from core.engine import WorkflowEngine
from workflows.eco_building import eco_workflow

def run_eco():
    engine = WorkflowEngine(eco_workflow)

    engine.set_context("input", "Off-grid eco housing cluster for tropical region")
    engine.set_context("climate", "tropical")
    engine.set_context("energy_mode", "solar_offgrid")

    result = engine.run_workflow("eco_design")

    print("\n🌿 ECO ARCHITECTURE OUTPUT")
    print("==========================")
    print(result)


if __name__ == "__main__":
    run_eco()

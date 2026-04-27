# src/core/planner.py

def generate_workflow(intent):
    workflow = []

    # always start with concept
    workflow.append({
        "name": "concept_stage",
        "output_key": "concept"
    })

    # adaptive branching
    if intent["is_tropical"]:
        workflow.append({
            "name": "climate_check",
            "output_key": "climate_result"
        })

    if intent["needs_sustainability"]:
        workflow.append({
            "name": "eco_design",
            "output_key": "eco_plan"
        })

    # scale-based logic
    if intent["scale"] == "urban":
        workflow.append({
            "name": "urban_planning",
            "output_key": "urban_result"
        })

    workflow.append({
        "name": "final_output",
        "output_key": "result"
    })

    return {
        "adaptive_design": workflow
    }

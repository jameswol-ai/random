# src/stages

def concept_stage(ctx):
    return {
        "concept": f"Designing: {ctx.get('input')}"
    }


def climate_check(ctx):
    return {
        "climate_result": "Applied tropical climate adaptations"
    }


def eco_design(ctx):
    return {
        "eco_plan": "Added solar + rainwater systems"
    }


def final_output(ctx):
    return {
        "result": f"""
FINAL DESIGN
Concept: {ctx.get('concept')}
Climate: {ctx.get('climate_result')}
Eco: {ctx.get('eco_plan')}
"""
    }

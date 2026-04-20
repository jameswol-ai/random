from core.helpers import (
    get_from_context,
    detect_climate,
    suggest_materials,
    log_stage
)

def concept_stage(ctx):
    idea = get_from_context(ctx, "input")

    climate = detect_climate(idea)
    materials = suggest_materials(climate)

    log_stage("Concept", f"Detected climate: {climate}")

    return {
        "concept": f"Sustainable design for {climate} climate",
        "materials": materials,
        "climate": climate
    }

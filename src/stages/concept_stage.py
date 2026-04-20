def concept_stage(ctx):
    input_text = ctx.get("input")
    climate_rules = ctx.get("building_codes")

    if "tropical" in input_text.lower():
        ctx.set("optimize_required", True)

    return f"Concept based on input: {input_text}\nUsing climate logic:\n{climate_rules[:150]}..."

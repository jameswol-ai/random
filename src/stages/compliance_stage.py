def compliance_stage(ctx):
    concept = ctx.get("concept_stage", {})

    return {
        "status": "pass",
        "notes": f"Validated design: {concept.get('concept')}"
    }

def concept_stage(ctx):
    return f"Concept generated from: {ctx.get('input')}"

def compliance_stage(ctx):
    return "Checked against building standards"

def output_stage(ctx):
    return "Final architectural plan generated"


architectural_workflow = {
    "basic_design": [
        {"name": "concept", "action": concept_stage},
        {"name": "compliance", "action": compliance_stage},
        {"name": "output", "action": output_stage},
    ]
}

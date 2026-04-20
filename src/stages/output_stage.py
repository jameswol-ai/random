from core.design_schema import FinalDesign, WorkflowResult

def output_stage(ctx):
    concept = ctx.get("concept")
    compliance = ctx.get("compliance")

    final = FinalDesign(
        concept=concept,
        compliance=compliance,
        drawings={"site_plan": "generated_placeholder"},
        notes="Design optimized for tropical climate"
    )

    result = WorkflowResult(
        success=True,
        design=final,
        metadata={"version": "v1"}
    )

    return result

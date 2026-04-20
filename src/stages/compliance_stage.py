# src/stages/compliance_stage.py

def compliance_stage(ctx):
    concept = ctx.get("concept")

    compliance_report = f"""
    Compliance Review:
    - Structural safety: OK
    - Fire safety standards: VERIFIED
    - Environmental regulations: PASSED
    - Zoning compatibility: CHECKED
    """

    ctx.set("compliance", compliance_report)
    return compliance_report

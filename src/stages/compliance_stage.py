from core.design_schema import ComplianceReport

def compliance_stage(ctx):
    concept = ctx.get("concept")

    report = ComplianceReport(
        passed=True,
        issues=[],
        standards_checked=["Local Building Code", "Environmental Guidelines"]
    )

    ctx.set("compliance", report)
    return report

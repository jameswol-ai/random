# src/stages/compliance_stage.py

from src.models.stage_contract import StageResult, stage_input

def compliance_stage(ctx):
    data = stage_input(ctx)

    knowledge = data["knowledge"]

    rules_used = [doc["doc"] for doc in knowledge] if knowledge else []

    # 🧠 simple rule logic (future AI replacement point)
    if not rules_used:
        status = "warning"
    else:
        status = "validated"

    return StageResult(
        output="Compliance check completed",
        status=status,
        signals={
            "rules_used": rules_used,
            "risk_level": "low" if rules_used else "unknown"
        }
    ).to_dict()

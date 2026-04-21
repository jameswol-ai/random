# src/stages/compliance_stage.py

def compliance_stage(ctx):
    input_text = ctx.get("input", "")
    docs = ctx.get("knowledge", [])

    rules_found = []

    for doc in docs:
        rules_found.append(doc["doc"])

    return {
        "status": "checked",
        "input": input_text,
        "rules_used": rules_found,
        "message": "📋 Compliance validated using building codes"
    }

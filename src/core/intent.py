# src/core/intent.py

def analyze_intent(ctx):
    text = ctx.get("input", "").lower()

    intent = {
        "is_tropical": "tropical" in text or "hot" in text,
        "needs_sustainability": "eco" in text or "sustainable" in text,
        "scale": "urban" if "city" in text else "building"
    }

    return intent

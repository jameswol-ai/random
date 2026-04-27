# src/core/city_intent.py

def analyze_city_intent(ctx):
    text = ctx.get("input", "").lower()

    return {
        "population_scale": "urban" if "city" in text else "town",
        "climate": "tropical" if "tropical" in text or "juba" in text else "generic",
        "focus": {
            "transport_heavy": "traffic" in text or "mobility" in text,
            "eco_priority": "eco" in text or "sustainable" in text,
            "high_density": "dense" in text or "vertical" in text
        }
    }

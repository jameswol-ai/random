import datetime

def get_from_context(ctx, key, default=None):
    """Safely fetch from context"""
    return ctx.get(key, default)


def update_context(ctx, key, value):
    """Update context with a new value"""
    ctx[key] = value
    return ctx


def log_stage(stage_name, message):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] 🏗️ {stage_name}: {message}")


def validate_input(ctx):
    if "input" not in ctx or not ctx["input"]:
        raise ValueError("Missing 'input' in context")
    return True


def detect_climate(input_text):
    input_text = input_text.lower()

    if "tropical" in input_text:
        return "tropical"
    elif "desert" in input_text:
        return "arid"
    elif "cold" in input_text:
        return "cold"
    
    return "temperate"


def suggest_materials(climate):
    materials_map = {
        "tropical": ["bamboo", "vent blocks", "lightweight concrete"],
        "arid": ["rammed earth", "stone", "thermal mass brick"],
        "cold": ["insulated panels", "triple-glazed glass"],
        "temperate": ["brick", "wood", "concrete"]
    }

    return materials_map.get(climate, [])


def format_output(title, data):
    return {
        "title": title,
        "generated_at": datetime.datetime.now().isoformat(),
        "data": data
    }

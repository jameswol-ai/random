# src/stages/analysis_stage.py

def analysis_stage(ctx):
    input_data = ctx.get("input")

    analysis = f"""
    Feasibility Analysis:
    - Climate suitability: High (tropical adaptation recommended)
    - Cost estimate: Medium range
    - Material availability: Local + sustainable options viable
    - Energy efficiency potential: Strong (solar + ventilation)
    """

    ctx.set("analysis", analysis)
    return analysis

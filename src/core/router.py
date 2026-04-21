def choose_next_steps(context):
    """
    Decides extra steps dynamically based on context.
    """

    steps = []

    climate = context.get("climate")
    budget = context.get("budget")

    # 🌴 tropical environments need ventilation thinking
    if climate == "tropical":
        steps.append("ventilation_stage")

    # 💰 low budget forces optimization thinking
    if budget == "low":
        steps.append("cost_optimization_stage")

    return steps

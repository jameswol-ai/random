from src.core.memory import MemoryStore

memory = MemoryStore()

def choose_next_steps(context):
    steps = []

    climate = context.get("climate")
    budget = context.get("budget")

    # 🌴 learned preference weighting
    ventilation_score = memory.score("ventilation_stage")
    cost_score = memory.score("cost_optimization_stage")

    if climate == "tropical":
        # bias toward stages that historically worked well
        if ventilation_score >= 0.5:
            steps.append("ventilation_stage")

    if budget == "low":
        if cost_score >= 0.5:
            steps.append("cost_optimization_stage")

    return steps

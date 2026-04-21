#src/stages/concept_stage.py

from src.models.agent import AgentResponse


def concept_stage(ctx):
    user_input = ctx.get("input", "")

    # 🎨 Generator
    idea = f"Architectural concept for: {user_input}"

    # 🔍 Critic (internal review simulation)
    critique = ""

    confidence = 0.75

    if "school" in user_input.lower():
        critique = "Good functional scope, but needs climate adaptation detail."
        confidence = 0.8
    else:
        critique = "Concept is general; requires more specificity."

    return AgentResponse(
        output=idea,
        critique=critique,
        confidence=confidence,
        signals={
            "creativity": confidence,
            "type": "concept"
        }
    ).to_dict()

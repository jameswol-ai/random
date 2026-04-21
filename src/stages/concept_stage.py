#src/stages/concept_stage.py

from src.core.llm_agent import LLMAgent


def concept_stage(ctx):
    agent = ctx["agent"]

    result = agent.run("concept", ctx)

    return {
        "output": result["output"],
        "confidence": result.get("confidence", 0.8),
        "critique": result.get("critique", ""),
        "signals": result.get("signals", {})
    }

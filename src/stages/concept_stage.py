from core.design_schema import DesignConcept

def concept_stage(ctx):
    idea = ctx.get("input")

    concept = DesignConcept(
        title="Eco School Concept",
        description=f"Design based on: {idea}",
        climate_strategy="Natural ventilation, shaded courtyards",
        materials=["bamboo", "compressed earth blocks", "recycled metal"]
    )

    ctx.set("concept", concept)
    return concept

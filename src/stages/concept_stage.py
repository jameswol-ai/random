# src/stages/concept_stage.py

class ConceptStage:
    def run(self, context):
        idea = context.get("input")

        concept = f"Eco-friendly tropical house based on: {idea}"

        context.update_design("concept", concept)
        return context

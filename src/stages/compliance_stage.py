# src/stages/compliance_stage.py

class ComplianceStage:
    def run(self, context):
        compliance = {
            "fire_safety": "2 exits, fire-resistant materials",
            "climate": "elevated foundation, rain protection"
        }

        context.update_design("compliance", compliance)
        return context

# src/core/dispatcher.py

from stages.concept_stage import ConceptStage
from stages.analysis_stage import AnalysisStage
from stages.compliance_stage import ComplianceStage
from stages.output_stage import OutputStage

class Dispatcher:
    def __init__(self, config):
        self.config = config

    def get_stages(self):
        stage_map = {
            "concept": ConceptStage(),
            "analysis": AnalysisStage(),
            "compliance": ComplianceStage(),
            "output": OutputStage(),
        }

        return [stage_map[name] for name in self.config["stages"]]

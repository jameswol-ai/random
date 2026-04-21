# src/models/agent.py

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class AgentResponse:
    output: Any
    critique: str = ""
    confidence: float = 0.0
    signals: Dict[str, Any] = None

    def to_dict(self):
        return {
            "output": self.output,
            "critique": self.critique,
            "confidence": self.confidence,
            "signals": self.signals or {}
        }

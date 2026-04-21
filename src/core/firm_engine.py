# src/core/firm_engine.py

class FirmEngine:
    def __init__(self, agent):
        self.agent = agent

    def run_firm_cycle(self, context):
        history = []

        # 🏗️ Step 1: Architect
        architect = self.agent.run("architect", context)
        history.append(("architect", architect))

        # 🧱 Step 2: Structural check
        structural = self.agent.run("structural_engineer", {
            **context,
            "last_output": architect
        })
        history.append(("structural_engineer", structural))

        # 🌍 Step 3: Climate review
        climate = self.agent.run("climate_specialist", {
            **context,
            "last_output": architect
        })
        history.append(("climate_specialist", climate))

        # 📋 Step 4: Compliance
        compliance = self.agent.run("compliance_officer", {
            **context,
            "last_output": architect
        })
        history.append(("compliance_officer", compliance))

        # 🧠 Step 5: Senior critic resolves everything
        final = self.agent.run("critic", {
            **context,
            "last_outputs": history
        })

        return {
            "cycle": history,
            "final": final
        }

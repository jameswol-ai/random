from workflows.floor_plan import generate_floor_plan
from workflows.building_codes import apply_building_rules

def run_design_team(user_input):

    designer_output = generate_floor_plan(user_input)
    reviewer_output = apply_building_rules(designer_output)

    final_report = f"""
🏢 DESIGN OUTPUT:
{designer_output}

📜 COMPLIANCE REVIEW:
{reviewer_output}

🧠 FINAL NOTE:
Refine design based on compliance feedback.
"""
    return final_report

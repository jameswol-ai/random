def run_checks(text):
    issues = []

    if "basement" in text.lower():
        issues.append("Check waterproofing standards required")

    if "high rise" in text.lower():
        issues.append("Ensure fire evacuation compliance")

    if not issues:
        return "No major compliance risks detected."

    return "\n".join([f"- {i}" for i in issues])

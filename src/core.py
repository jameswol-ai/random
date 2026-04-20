from src.prompts import get_system_prompt
from src.compliance import run_checks

def process_request(user_input, workflow):
    prompt = get_system_prompt(workflow)

    # simulate reasoning layer (later can connect OpenAI / local LLM)
    draft = f"""
    [ARCHITECT AI ANALYSIS]
    Mode: {workflow}

    Input:
    {user_input}

    Step 1: Interpreting architectural intent...
    Step 2: Applying structural logic...
    Step 3: Evaluating space efficiency...
    """

    compliance_report = run_checks(user_input)

    return draft + "\n\n📋 Compliance Report:\n" + compliance_report

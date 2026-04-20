import streamlit as st
from src.core import generate_response
from workflows.design_workflow import design_concept
from  import compliance_check

st.set_page_config("RANDOM Architectural AI", layout="wide")

st.title("🏗️ RANDOM Architectural AI Assistant")

mode = st.selectbox("Choose Mode", [
    "General Chat",
    "Floor Plan + Code Review (Full AI Team",
    "Compliance Check"
])

user_input = st.text_area("Describe your project")

if st.button("Run"):
    if user_input:
        if mode == "Floor Plan + Code Review (Full AI Team":
            prompt = design_concept(user_input)
        elif mode == "Compliance Check":
            prompt = compliance_check(user_input)
        else:
            prompt = user_input

        response = generate_response(prompt)

        st.subheader("Result")
        st.write(response)

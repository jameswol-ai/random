import streamlit as st
from src.core import generate_response
from workflows.design_workflow import design_concept
from workflows.compliance_workflow import compliance_check

st.set_page_config(page_title="Architectural AI", layout="wide")

st.title("🏗️ Architectural AI Assistant")

mode = st.selectbox("Choose Mode", [
    "General",
    "Design Concept",
    "Compliance Check"
])

user_input = st.text_area("Describe your project")

if st.button("Generate"):
    if user_input:
        if mode == "Design Concept":
            prompt = design_concept(user_input)
        elif mode == "Compliance Check":
            prompt = compliance_check(user_input)
        else:
            prompt = user_input

        response = generate_response(prompt)

        st.subheader("Result")
        st.write(response)

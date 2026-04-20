import streamlit as st
from src.core import generate_response
from src.agents import run_design_team

st.set_page_config(page_title="RANDOM Architectural AI", layout="wide")

st.title("🏗️ RANDOM — Architectural Intelligence System")

mode = st.selectbox("Mode", [
    "General Chat",
    "Floor Plan + Code Review (Full AI Team)"
])

user_input = st.text_area("Describe your project")

if st.button("Run"):
    if mode == "Floor Plan + Code Review (Full AI Team)":
        output = run_design_team(user_input)
    else:
        output = generate_response(user_input)

    st.subheader("Result")
    st.write(output)

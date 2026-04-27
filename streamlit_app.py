#random/streamlit_app.py 

import streamlit as st
from core.engine import WorkflowEngine

st.set_page_config(page_title="Random Engine", layout="centered")

st.title("🧠 Random Autonomous Architect")

st.write("A self-evolving workflow brain for architecture decisions.")

if st.button("Run Random Engine 🚀"):
    engine = WorkflowEngine()
    result = engine.run()

    st.subheader("📦 Final Context")
    st.json(result["final_context"])

    st.subheader("🧾 Execution Log")

    for step in result["log"]:
        st.markdown(f"**{step['stage']}**")
        st.json(step["output"])

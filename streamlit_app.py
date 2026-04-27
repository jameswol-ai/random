# random/streamlit_app.py 

import streamlit as st
from core.engine import WorkflowEngine

st.title("📖 Random Narrative Mode")

if st.button("Run Story Engine"):
    engine = WorkflowEngine()
    result = engine.run()

    st.subheader("📖 Execution Story")

    for line in result["story"]:
        st.write(line)

    st.subheader("🧠 Reflection")
    st.info(result["summary"]["reflection"])

    st.subheader("📦 Final State")
    st.json(result["final_context"])

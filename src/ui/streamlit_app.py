# src/ui/streamlit_app.py

import streamlit as st
from core.engine import WorkflowEngine

st.title("🧬 Random Dual-Layer Mode")

if st.button("Run Engine"):
    engine = WorkflowEngine()
    result = engine.run()

    # 📖 Narrative Layer (human)
    st.subheader("📖 Narrative Layer")
    for line in result["narrative_layer"]["story"]:
        st.write(line)

    st.info(result["narrative_layer"]["reflection"])

    # ⚙️ Machine Layer (system truth)
    st.subheader("⚙️ Machine Layer")
    st.json(result["machine_layer"]["log"])

    st.subheader("📦 Final Context")
    st.json(result["machine_layer"]["context"])

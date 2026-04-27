# random/streamlit_app.py 

import streamlit as st
import traceback

# -----------------------------
# SAFE IMPORT LAYER
# -----------------------------

try:
    # preferred import path (your project version)
    from src.core.engine import WorkflowEngine
except Exception:
    WorkflowEngine = None


# -----------------------------
# FALLBACK ENGINE (CRASH-PROOF)
# -----------------------------

class FallbackWorkflowEngine:
    def __init__(self):
        self.state = {
            "status": "fallback_active",
            "memory": [],
            "ticks": 0
        }

    def run(self, input_data=None):
        self.state["ticks"] += 1

        result = {
            "message": "Fallback engine is running",
            "input": input_data,
            "tick": self.state["ticks"]
        }

        self.state["memory"].append(result)
        return result

    def tick(self):
        self.state["ticks"] += 1
        return self.state["ticks"]


# -----------------------------
# ENGINE INITIALIZATION
# -----------------------------

if WorkflowEngine:
    try:
        engine = WorkflowEngine()
        engine_mode = "primary"
    except Exception:
        engine = FallbackWorkflowEngine()
        engine_mode = "fallback_due_to_init_error"
else:
    engine = FallbackWorkflowEngine()
    engine_mode = "fallback_missing_engine"


# -----------------------------
# STREAMLIT UI
# -----------------------------

st.set_page_config(page_title="Random Engine", layout="wide")

st.title("Random Engine Control Center")

st.caption(f"Engine mode: {engine_mode}")


# -----------------------------
# INPUT PANEL
# -----------------------------

user_input = st.text_input("Enter workflow input", "")

col1, col2 = st.columns(2)

with col1:
    run_button = st.button("Run Engine")

with col2:
    tick_button = st.button("Alive Tick")


# -----------------------------
# EXECUTION AREA
# -----------------------------

if run_button:
    try:
        if hasattr(engine, "run"):
            result = engine.run(user_input)
        else:
            result = {"error": "Engine has no run() method"}

        st.success("Execution complete")
        st.json(result)

    except Exception as e:
        st.error("Engine execution failed")
        st.code(traceback.format_exc())


if tick_button:
    try:
        if hasattr(engine, "tick"):
            t = engine.tick()
            st.info(f"Alive tick: {t}")
        else:
            st.warning("Tick not supported in this engine")

    except Exception:
        st.error("Tick system failed")
        st.code(traceback.format_exc())


# -----------------------------
# STATE VIEWER
# -----------------------------

st.divider()

st.subheader("Engine State")

if hasattr(engine, "state"):
    st.json(engine.state)
else:
    st.write("No state available")


# -----------------------------
# DEBUG PANEL
# -----------------------------

with st.expander("Debug Panel"):
    st.write("Engine Type:", type(engine).__name__)
    st.write("Engine Mode:", engine_mode)
    st.write("Has run():", hasattr(engine, "run"))
    st.write("Has tick():", hasattr(engine, "tick"))

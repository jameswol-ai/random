#random/streamlit_app.py 

import streamlit as st
import sys
import os
import traceback

# --------------------------------------------------
# 🧭 PATH FIX (handles Streamlit Cloud + local)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

POSSIBLE_PATHS = [
    BASE_DIR,
    os.path.join(BASE_DIR, "src"),
    os.path.join(BASE_DIR, "src", "core"),
]

for path in POSSIBLE_PATHS:
    if path not in sys.path:
        sys.path.insert(0, path)

# --------------------------------------------------
# 🎛 PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="AI Architecture Bot", layout="wide")

st.title("🏗️ AI Architecture Bot")
st.caption("Resilient Workflow Engine • Debug Mode Enabled")

# --------------------------------------------------
# 🔍 DEBUG PANEL
# --------------------------------------------------
with st.expander("⚙️ System Debug Info", expanded=False):
    st.write("📁 Base Dir:", BASE_DIR)

    for path in POSSIBLE_PATHS:
        exists = os.path.exists(path)
        st.write(f"Path: {path} → {'✅' if exists else '❌'}")
        if exists:
            try:
                st.write("Contents:", os.listdir(path))
            except:
                pass

    st.write("🐍 Python:", sys.version)
    st.write("📦 sys.path:", sys.path)

# --------------------------------------------------
# 🧠 IMPORT ENGINE (MULTI-STRATEGY)
# --------------------------------------------------
def load_engine():
    errors = []

    try:
        from core.engine import WorkflowEngine
        return WorkflowEngine, "core.engine"
    except Exception as e:
        errors.append(("core.engine", traceback.format_exc()))

    try:
        from engine import WorkflowEngine
        return WorkflowEngine, "engine"
    except Exception as e:
        errors.append(("engine", traceback.format_exc()))

    try:
        from src.core.engine import WorkflowEngine
        return WorkflowEngine, "src.core.engine"
    except Exception as e:
        errors.append(("src.core.engine", traceback.format_exc()))

    return None, errors


WorkflowEngine, source = load_engine()

# --------------------------------------------------
# 🚨 IF IMPORT FAILS → SHOW FULL ERROR + FALLBACK
# --------------------------------------------------
if WorkflowEngine is None:
    st.error("❌ Could not import WorkflowEngine from any known path")

    for name, err in source:
        with st.expander(f"🔴 Error from {name}"):
            st.code(err)

    st.warning("⚠️ Using fallback engine (app will still run)")

    # 🪄 FALLBACK ENGINE (so app never dies)
    class WorkflowEngine:
        def __init__(self, workflow, function_registry):
            self.workflow = workflow
            self.function_registry = function_registry
            self.context = {}

        def set_context(self, key, value):
            self.context[key] = value

        def run_workflow(self, workflow_name):
            stages = self.workflow.get(workflow_name, [])
            for stage in stages:
                func = self.function_registry.get(stage["name"])
                if func:
                    result = func(self.context)
                    if "output_key" in stage:
                        self.context[stage["output_key"]] = result
            return self.context

else:
    st.success(f"✅ WorkflowEngine loaded from: {source}")

# --------------------------------------------------
# 🧩 SAFE FUNCTION REGISTRY
# --------------------------------------------------
def concept_stage(ctx):
    return f"Concept: {ctx.get('input')}"

def climate_stage(ctx):
    if "tropical" in ctx.get("input", "").lower():
        return "🌴 Tropical design applied"
    return "Standard climate design"

def eco_stage(ctx):
    if "eco" in ctx.get("input", "").lower():
        return "♻️ Sustainability features added"
    return "No eco features"

def final_output(ctx):
    return f"""
🏗️ FINAL DESIGN

Concept:
{ctx.get('concept')}

Climate:
{ctx.get('climate')}

Eco:
{ctx.get('eco')}
"""

function_registry = {
    "concept_stage": concept_stage,
    "climate_stage": climate_stage,
    "eco_stage": eco_stage,
    "final_output": final_output,
}

# --------------------------------------------------
# 🗺 SAFE WORKFLOW
# --------------------------------------------------
workflow = {
    "design_flow": [
        {"name": "concept_stage", "output_key": "concept"},
        {"name": "climate_stage", "output_key": "climate"},
        {"name": "eco_stage", "output_key": "eco"},
        {"name": "final_output", "output_key": "result"},
    ]
}

# --------------------------------------------------
# ⚙️ INIT ENGINE
# --------------------------------------------------
try:
    engine = WorkflowEngine(workflow, function_registry)
except Exception:
    st.error("❌ Engine initialization failed")
    st.code(traceback.format_exc())
    st.stop()

# --------------------------------------------------
# 🎯 USER INPUT
# --------------------------------------------------
user_input = st.text_area(
    "Describe your architectural project:",
    placeholder="Eco-friendly school in tropical climate"
)

# --------------------------------------------------
# ▶️ RUN BUTTON
# --------------------------------------------------
if st.button("Generate Design"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a project description")
    else:
        try:
            engine.set_context("input", user_input)
            result = engine.run_workflow("design_flow")

            st.success("✅ Design generated")

            st.subheader("📄 Output")
            st.code(result.get("result", "No result"))

            with st.expander("🧠 Full Context"):
                st.json(result)

        except Exception:
            st.error("❌ Runtime error")
            st.code(traceback.format_exc())

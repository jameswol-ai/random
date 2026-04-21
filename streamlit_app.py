import streamlit as st
import sys
import os

# Ensure src/ is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from core.engine import WorkflowEngine
from workflows.loader import load_workflow  # assuming you created this

# -----------------------------
# App UI Setup
# -----------------------------
st.set_page_config(page_title="AI Architecture Bot", layout="wide")

st.title("🏗️ AI Architecture Bot")
st.caption("Design smart buildings with AI workflows")

# -----------------------------
# Load Workflow
# -----------------------------
@st.cache_resource
def get_engine():
    workflow = load_workflow("basic_design")  # or eco_building.json
    engine = WorkflowEngine(workflow)
    return engine

engine = get_engine()

# -----------------------------
# User Input
# -----------------------------
user_input = st.text_area(
    "Describe your project:",
    placeholder="Example: Eco-friendly school in tropical climate..."
)

workflow_type = st.selectbox(
    "Select Workflow",
    ["basic_design", "eco_building", "urban_plan"]
)

# -----------------------------
# Run Button
# -----------------------------
if st.button("Generate Design 🚀"):
    if not user_input.strip():
        st.warning("Please enter a project description.")
    else:
        with st.spinner("Designing..."):
            engine.set_context("input", user_input)

            try:
                result = engine.run_workflow(workflow_type)

                st.success("✅ Design Generated!")

                # Display results
                st.subheader("📐 Output")
                if isinstance(result, dict):
                    for key, value in result.items():
                        st.markdown(f"**{key}:** {value}")
                else:
                    st.write(result)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# -----------------------------
# Sidebar Info
# -----------------------------
with st.sidebar:
    st.header("ℹ️ About")
    st.write(
        "This AI bot generates architectural concepts, checks compliance, "
        "and produces structured designs using modular workflows."
    )

    st.subheader("⚙️ Tips")
    st.write("- Be specific with your project")
    st.write("- Try different workflows")
    st.write("- Use climate or location context")

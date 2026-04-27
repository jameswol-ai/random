# random/streamlit_app.py 

import streamlit as st
from dataclasses import dataclass, field
from typing import Callable, Dict, Any, List


# =========================================================
# 🧠 CORE STATE
# =========================================================

@dataclass
class State:
    data: Dict[str, Any] = field(default_factory=dict)
    logs: List[str] = field(default_factory=list)

    def log(self, message: str):
        self.logs.append(message)


# =========================================================
# ⚙️ NODE SYSTEM
# =========================================================

@dataclass
class Node:
    name: str
    func: Callable[[State], State]

    def run(self, state: State) -> State:
        state.log(f"▶ Running node: {self.name}")
        return self.func(state)


# =========================================================
# 🧠 WORKFLOW ENGINE
# =========================================================

class WorkflowEngine:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.graph: Dict[str, str] = {}

    def add_node(self, node: Node):
        self.nodes[node.name] = node

    def connect(self, from_node: str, to_node: str):
        self.graph[from_node] = to_node

    def run(self, start_node: str, state: State) -> State:
        current = start_node

        state.log("🚀 Workflow started")

        visited = set()

        while current:
            if current in visited:
                state.log("⚠ Loop detected, stopping execution")
                break

            visited.add(current)

            node = self.nodes.get(current)
            if not node:
                state.log(f"❌ Missing node: {current}")
                break

            state = node.run(state)

            current = self.graph.get(current)

        state.log("🏁 Workflow completed")
        return state


# =========================================================
# 🌿 SAMPLE NODES (MINIMAL BUT REAL)
# =========================================================

def input_node(state: State):
    state.data["input"] = "raw signal detected"
    state.log("Input captured")
    return state


def analyze_node(state: State):
    inp = state.data.get("input", "")
    state.data["analysis"] = f"processed({inp})"
    state.log("Analysis complete")
    return state


def decision_node(state: State):
    analysis = state.data.get("analysis", "")
    state.data["decision"] = "proceed" if "processed" in analysis else "halt"
    state.log(f"Decision made: {state.data['decision']}")
    return state


# =========================================================
# 🏗️ ENGINE BUILD
# =========================================================

def build_engine():
    engine = WorkflowEngine()

    engine.add_node(Node("input", input_node))
    engine.add_node(Node("analyze", analyze_node))
    engine.add_node(Node("decide", decision_node))

    engine.connect("input", "analyze")
    engine.connect("analyze", "decide")

    return engine


# =========================================================
# 🌐 STREAMLIT UI
# =========================================================

st.set_page_config(page_title="Random Engine v1", layout="wide")

st.title("🌱 RANDOM — CORE ENGINE v1")

engine = build_engine()

if st.button("Run Workflow"):
    state = State()
    result = engine.run("input", state)

    st.subheader("📦 State Data")
    st.json(result.data)

    st.subheader("📜 Execution Log")
    st.text("\n".join(result.logs))


# Live view panel
st.sidebar.title("🧠 System Status")
st.sidebar.write("Nodes:", list(engine.nodes.keys()))
st.sidebar.write("Connections:", engine.graph)

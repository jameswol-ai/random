import streamlit as st
import random
import time
import numpy as np

# ---------------------------
# MUST be first Streamlit call
# ---------------------------
st.set_page_config(page_title="Random City Brain", layout="wide")

# ---------------------------
# SAFE MATPLOTLIB IMPORT
# ---------------------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MPL = True
except Exception as e:
    HAS_MPL = False
    st.warning(f"Matplotlib unavailable: {e}")

# ---------------------------
# SAFE NETWORKX IMPORT
# ---------------------------
try:
    import networkx as nx
    HAS_NX = True
except Exception as e:
    HAS_NX = False
    st.warning(f"NetworkX unavailable: {e}")

# ---------------------------
# HEADER
# ---------------------------
st.title("🏙️ Random City Brain")
st.caption("A living, evolving AI city simulation")

# ---------------------------
# SAFE DATA GENERATOR
# ---------------------------
def generate_data(n=50):
    x = np.linspace(0, 10, n)
    y = np.sin(x) + np.random.normal(0, 0.1, n)
    return x, y

# ---------------------------
# SMALL DASHBOARD CHART
# ---------------------------
st.subheader("Random System Dashboard")

if HAS_MPL:
    x, y = generate_data()
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Evolving Signal (Random Flow)")
    ax.set_xlabel("Time")
    ax.set_ylabel("State")
    st.pyplot(fig)
else:
    st.info("Plot system offline (matplotlib missing)")

# ---------------------------
# SYSTEM STATE PANEL
# ---------------------------
st.subheader("System State")

state_block = {
    "nodes": 12,
    "connections": 34,
    "entropy": round(np.random.random(), 3)
}

st.json(state_block)

if st.button("Evolve system"):
    st.rerun()

# ---------------------------
# INITIAL STATE
# ---------------------------
if "city_state" not in st.session_state:
    st.session_state.city_state = {
        "cycle": 0,
        "energy": 100,
        "population": 10,
        "mood": "stable",
        "history": []
    }

if "agents" not in st.session_state:
    st.session_state.agents = {
        "builder": {"bias": 1.2},
        "energy": {"bias": 1.0},
        "nature": {"bias": 0.8},
        "governor": {"bias": 1.0}
    }

if "meta" not in st.session_state:
    st.session_state.meta = {
        "awareness": 0,
        "last_thought": "Initializing consciousness..."
    }

if "mutation_log" not in st.session_state:
    st.session_state.mutation_log = []

# ---------------------------
# EVOLUTION ENGINE
# ---------------------------
def evolve_city(state, agents):
    state["cycle"] += 1

    growth = int(random.randint(0, 4) * agents["builder"]["bias"])
    energy_use = int(random.randint(1, 5) * max(growth, 1) * agents["energy"]["bias"])
    recovery = int(random.randint(0, 3) * agents["nature"]["bias"])

    state["population"] += growth
    state["energy"] += recovery - energy_use

    if state["energy"] < 20:
        agents["builder"]["bias"] *= 0.9
        agents["energy"]["bias"] *= 1.1

    if state["population"] > 60:
        agents["nature"]["bias"] *= 1.1

    if state["energy"] < 20:
        state["mood"] = "critical"
    elif state["population"] > 80:
        state["mood"] = "overflowing"
    else:
        state["mood"] = "adaptive"

    state["history"].append({
        "cycle": state["cycle"],
        "population": state["population"],
        "energy": state["energy"],
        "mood": state["mood"]
    })

    return state

# ---------------------------
# REFLECTION ENGINE
# ---------------------------
def reflect(state, meta):
    energy = state["energy"]
    population = state["population"]

    meta["awareness"] += int((population + energy) / 50)

    if energy < 20:
        meta["last_thought"] = "Energy collapsing. Survival mode active."
    elif population > 80:
        meta["last_thought"] = "Expansion surge detected. Stability fragile."
    elif meta["awareness"] > 50:
        meta["last_thought"] = "Patterns emerging across cycles..."
    else:
        meta["last_thought"] = "Systems stable. Growth continues."

    return meta

# ---------------------------
# MUTATION ENGINE
# ---------------------------
def mutate_agents(state, agents, log):
    for name, agent in agents.items():
        old = agent["bias"]

        if state["energy"] < 20:
            delta = random.uniform(0.05, 0.2)
        elif state["population"] > 80:
            delta = random.uniform(-0.2, -0.05)
        else:
            delta = random.uniform(-0.05, 0.05)

        agent["bias"] = max(0.1, min(2.0, agent["bias"] + delta))

        if abs(old - agent["bias"]) > 0.05:
            log.append(f"{name}: {round(old,2)} → {round(agent['bias'],2)}")

    return agents, log

# ---------------------------
# GRAPH BUILDER
# ---------------------------
def build_graph(agents):
    G = nx.DiGraph()

    for name, data in agents.items():
        G.add_node(name, weight=round(data["bias"], 2))

    G.add_edge("builder", "population", weight=agents["builder"]["bias"])
    G.add_edge("energy", "population", weight=-agents["energy"]["bias"])
    G.add_edge("nature", "energy", weight=agents["nature"]["bias"])
    G.add_edge("governor", "builder", weight=agents["governor"]["bias"])
    G.add_edge("governor", "energy", weight=agents["governor"]["bias"])

    return G

def draw_graph(G):
    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots()

    nx.draw(G, pos, ax=ax, with_labels=True, node_size=2000, font_size=10)

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels={(u, v): round(w, 2) for (u, v, w) in G.edges(data="weight")},
        ax=ax
    )

    return fig

# ---------------------------
# CONTROLS
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Run Evolution Cycle"):
        st.session_state.city_state = evolve_city(
            st.session_state.city_state,
            st.session_state.agents
        )
        st.session_state.meta = reflect(
            st.session_state.city_state,
            st.session_state.meta
        )
        st.session_state.agents, st.session_state.mutation_log = mutate_agents(
            st.session_state.city_state,
            st.session_state.agents,
            st.session_state.mutation_log
        )

with col2:
    auto = st.checkbox("∞ Autonomous Mode")

# ---------------------------
# AUTO LOOP
# ---------------------------
if auto:
    for _ in range(10):
        st.session_state.city_state = evolve_city(
            st.session_state.city_state,
            st.session_state.agents
        )
        st.session_state.meta = reflect(
            st.session_state.city_state,
            st.session_state.meta
        )
        st.session_state.agents, st.session_state.mutation_log = mutate_agents(
            st.session_state.city_state,
            st.session_state.agents,
            st.session_state.mutation_log
        )
        time.sleep(0.2)
        st.rerun()

# ---------------------------
# DISPLAY STATE
# ---------------------------
state = st.session_state.city_state

st.subheader("📊 City State")
c1, c2, c3, c4 = st.columns(4)

c1.metric("Cycle", state["cycle"])
c2.metric("Population", state["population"])
c3.metric("Energy", state["energy"])
c4.metric("Mood", state["mood"])

# ---------------------------
# THOUGHT
# ---------------------------
st.subheader("🧠 City Thought")
st.info(st.session_state.meta["last_thought"])
st.metric("Awareness", st.session_state.meta["awareness"])

# ---------------------------
# HISTORY
# ---------------------------
if state["history"]:
    st.line_chart([h["population"] for h in state["history"]])

# ---------------------------
# MUTATION LOG
# ---------------------------
st.subheader("🧬 Mutation Log")
for entry in st.session_state.mutation_log[-5:]:
    st.write(entry)

# ---------------------------
# GRAPH VIEW
# ---------------------------
st.subheader("🕸️ City Brain Network")

if HAS_MPL and HAS_NX:
    G = build_graph(st.session_state.agents)
    fig = draw_graph(G)
    st.pyplot(fig)
else:
    st.info("Graph system offline")

# ---------------------------
# GOD MODE
# ---------------------------
st.subheader("🎮 God Mode")

agent_choice = st.selectbox(
    "Select Agent",
    list(st.session_state.agents.keys())
)

if st.button("Boost Agent"):
    st.session_state.agents[agent_choice]["bias"] *= 1.2

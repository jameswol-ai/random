import streamlit as st import random import time from datetime import datetime

-----------------------------

🧠 Session Memory

-----------------------------

if "history" not in st.session_state: st.session_state.history = []

if "best" not in st.session_state: st.session_state.best = None

City state

if "city_nodes" not in st.session_state: st.session_state.city_nodes = []  # list of dicts: {id, label, score, layer}

if "city_edges" not in st.session_state: st.session_state.city_edges = []  # list of dicts: {source, target}

-----------------------------

⚙️ Evolution Functions

-----------------------------

def generate_workflow(): steps = ["concept", "climate", "structure", "energy", "aesthetic"] random.shuffle(steps) return steps

def mutate(workflow): new = workflow.copy() if random.random() < 0.5 and len(new) > 1: i, j = random.sample(range(len(new)), 2) new[i], new[j] = new[j], new[i] if random.random() < 0.3: new.append("experimental") return new

def fitness(workflow): base = len(workflow) creativity = workflow.count("experimental") * 2 randomness = random.uniform(0, 2) return round(base + creativity + randomness, 2)

-----------------------------

🏙️ City Brain Builder

-----------------------------

def update_city(workflow, score): nodes = st.session_state.city_nodes edges = st.session_state.city_edges

# create nodes
for idx, step in enumerate(workflow):
    node_id = f"{step}_{idx}"
    nodes.append({
        "id": node_id,
        "label": step,
        "score": score,
        "layer": idx
    })

# create edges
for i in range(len(workflow) - 1):
    edges.append({
        "source": f"{workflow[i]}_{i}",
        "target": f"{workflow[i+1]}_{i+1}"
    })

-----------------------------

🎛️ UI Controls

-----------------------------

st.title("🏙️ Random City Brain")

mode = st.selectbox("Evolution Mode", ["Conservative", "Exploration", "Chaos"]) run_button = st.button("Run Evolution Cycle")

Mode tuning

if mode == "Conservative": variants_n = 2 elif mode == "Exploration": variants_n = 4 else: variants_n = 8

-----------------------------

🔁 Evolution Cycle

-----------------------------

if run_button: base = st.session_state.best or generate_workflow()

variants = []
for _ in range(variants_n):
    v = mutate(base)
    score = fitness(v)
    variants.append((v, score))

best_variant = max(variants, key=lambda x: x[1])

st.session_state.best = best_variant[0]

record = {
    "time": datetime.now().strftime("%H:%M:%S"),
    "best_score": best_variant[1],
    "workflow": best_variant[0]
}

st.session_state.history.append(record)

# update city brain
update_city(best_variant[0], best_variant[1])

-----------------------------

📊 Evolution Timeline

-----------------------------

if st.session_state.history: st.subheader("📈 Evolution Timeline")

scores = [h["best_score"] for h in st.session_state.history]
st.line_chart(scores)

st.subheader("🏆 Current Best Workflow")
st.write(st.session_state.best)

-----------------------------

🏙️ City Brain Visualization

-----------------------------

st.subheader("🏙️ City Brain Map")

if st.session_state.city_nodes: for node in st.session_state.city_nodes[-20:]: st.write(f"🧱 {node['label']} (Layer {node['layer']}) | Score Influence: {node['score']}")

st.subheader("🔗 Connections")
for edge in st.session_state.city_edges[-20:]:
    st.write(f"{edge['source']} → {edge['target']}")

else: st.info("City has not formed yet. Run evolution.")

-----------------------------

⏱️ Auto Evolution

-----------------------------

auto = st.checkbox("Enable Auto Evolution")

if auto: time.sleep(1) st.experimental_rerun()

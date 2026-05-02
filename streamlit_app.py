import streamlit as st
import random
import json
import os
from uuid import uuid4

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(page_title="Random Zero Civilization", layout="wide")

st.title("🧬 RANDOM — Zero Dependency Civilization")
st.caption("Pure Python. Persistent. Evolving. Alive.")

SAVE_FILE = "civilization_memory.json"

# =========================================================
# MEMORY
# =========================================================

def load_memory():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {
        "generation": 0,
        "population": [],
        "history": [],
        "events": []
    }

def save_memory(mem):
    with open(SAVE_FILE, "w") as f:
        json.dump(mem, f)

memory = load_memory()

# =========================================================
# GENOME
# =========================================================

def create_genome():
    return {
        "id": uuid4().hex[:8],
        "height": random.uniform(10, 200),
        "density": random.uniform(0.1, 1.0),
        "complexity": random.uniform(0, 10),
        "fitness": 0
    }

# =========================================================
# ENVIRONMENT (GOD CONTROL)
# =========================================================

st.sidebar.header("🌍 World")

env = {
    "wind": st.sidebar.slider("Wind", 0.1, 3.0, 1.0),
    "resources": st.sidebar.slider("Resources", 0.1, 3.0, 1.0),
    "innovation": st.sidebar.slider("Innovation", 0.1, 3.0, 1.0),
}

# =========================================================
# FITNESS
# =========================================================

def fitness(g):
    return (
        g["height"] * env["wind"]
        - g["density"] * env["resources"]
        + g["complexity"] * env["innovation"]
    )

# =========================================================
# EVOLUTION ENGINE
# =========================================================

def evolve(mem):
    pop = mem["population"]

    if not pop:
        pop = [create_genome() for _ in range(20)]

    # Evaluate
    for g in pop:
        g["fitness"] = fitness(g)

    # Sort by fitness
    pop.sort(key=lambda x: x["fitness"], reverse=True)

    survivors = pop[:10]

    # Reproduce
    new_pop = survivors[:]

    while len(new_pop) < 20:
        p1, p2 = random.sample(survivors, 2)
        child = {}

        for k in ["height", "density", "complexity"]:
            val = random.choice([p1[k], p2[k]])

            # mutation
            if random.random() < 0.2:
                val *= random.uniform(0.8, 1.2)

            child[k] = val

        child["id"] = uuid4().hex[:8]
        child["fitness"] = 0

        new_pop.append(child)

    mem["population"] = new_pop
    mem["generation"] += 1

    best = new_pop[0]

    mem["history"].append({
        "generation": mem["generation"],
        "fitness": best["fitness"]
    })

    # Narrative
    if best["fitness"] > 150:
        event = f"Gen {mem['generation']}: A towering dominant form emerged."
    elif best["fitness"] < 20:
        event = f"Gen {mem['generation']}: Collapse. Weak designs failed."
    else:
        event = f"Gen {mem['generation']}: Slow adaptation continues."

    mem["events"].append(event)

    return mem

# =========================================================
# GOD CONSOLE
# =========================================================

st.sidebar.header("👁️ Control")

if st.sidebar.button("⚡ Evolve"):
    memory = evolve(memory)

if st.sidebar.button("🌋 Catastrophe"):
    for g in memory["population"]:
        g["fitness"] *= random.uniform(0.1, 0.5)
    memory["events"].append("A catastrophe reshaped the world.")

if st.sidebar.button("🧬 Inject"):
    memory["population"].append({
        "id": uuid4().hex[:8],
        "height": 300,
        "density": 0.2,
        "complexity": 15,
        "fitness": 0
    })
    memory["events"].append("A powerful entity entered the world.")

if st.sidebar.button("☠️ Purge"):
    memory["population"].sort(key=lambda x: x["fitness"])
    memory["population"] = memory["population"][5:]
    memory["events"].append("The weakest were erased.")

# =========================================================
# SIMPLE VISUALIZATION (ASCII STYLE)
# =========================================================

st.subheader("🌆 Civilization View (Text Mode)")

for g in memory["population"]:
    bar = "█" * int(g["height"] / 5)
    st.text(f"{g['id']} | {bar}")

# =========================================================
# METRICS
# =========================================================

st.subheader("📊 Evolution Trend")

if memory["history"]:
    for h in memory["history"][-10:]:
        st.write(f"Gen {h['generation']} → Fitness: {round(h['fitness'],2)}")

# =========================================================
# POPULATION TABLE
# =========================================================

st.subheader("🧬 Population")

st.write(memory["population"])

# =========================================================
# LOG
# =========================================================

st.subheader("📖 Civilization Log")

for e in reversed(memory["events"][-10:]):
    st.write(e)

# =========================================================
# SAVE
# =========================================================

save_memory(memory)

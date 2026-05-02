import streamlit as st
import random
import math

# -----------------------------
# RANDOM ARCHITECTURE AI
# -----------------------------

st.set_page_config(page_title="Random Architecture AI", layout="wide")

st.title("🏗️ Random AI — Architecture Evolution Engine")
st.caption("Structures evolve. Blueprints compete. Cities self-organize.")

# -----------------------------
# INIT STATE
# -----------------------------
if "buildings" not in st.session_state:
    st.session_state.buildings = [
        {"id": 1, "height": 10, "width": 5, "stability": 8, "efficiency": 7},
        {"id": 2, "height": 14, "width": 6, "stability": 6, "efficiency": 9},
    ]
    st.session_state.next_id = 3
    st.session_state.tick = 0

# -----------------------------
# SCORING FUNCTION
# -----------------------------
def score(b):
    # balanced architecture fitness
    return (b["stability"] * 0.5 +
            b["efficiency"] * 0.3 +
            (10 - abs(b["height"] - b["width"])) * 0.2)

# -----------------------------
# MUTATION ENGINE
# -----------------------------
def mutate(b):
    return {
        "id": st.session_state.next_id,
        "height": max(1, b["height"] + random.randint(-3, 4)),
        "width": max(1, b["width"] + random.randint(-2, 3)),
        "stability": min(10, max(1, b["stability"] + random.randint(-2, 2))),
        "efficiency": min(10, max(1, b["efficiency"] + random.randint(-2, 2))),
    }

# -----------------------------
# EVOLUTION STEP
# -----------------------------
def evolve():
    new_gen = []

    for b in st.session_state.buildings:
        s = score(b)

        # survival rule
        if s > 7 or random.random() > 0.4:
            new_gen.append(b)

            # reproduction
            if s > 8:
                child = mutate(b)
                st.session_state.next_id += 1
                new_gen.append(child)

    # always inject novelty
    if random.random() > 0.5:
        seed = random.choice(st.session_state.buildings)
        new_gen.append(mutate(seed))
        st.session_state.next_id += 1

    st.session_state.buildings = new_gen
    st.session_state.tick += 1

# -----------------------------
# CONTROLS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶ Evolve Architecture"):
        evolve()

with col2:
    if st.button("⚡ Fast Forward x10"):
        for _ in range(10):
            evolve()

with col3:
    if st.button("🧱 Reset City"):
        st.session_state.buildings = [
            {"id": 1, "height": 10, "width": 5, "stability": 8, "efficiency": 7},
            {"id": 2, "height": 14, "width": 6, "stability": 6, "efficiency": 9},
        ]
        st.session_state.next_id = 3
        st.session_state.tick = 0

# -----------------------------
# DISPLAY CITY STATE
# -----------------------------
st.subheader(f"City Tick: {st.session_state.tick}")

buildings = st.session_state.buildings

if not buildings:
    st.error("🏚️ City collapsed — no surviving structures")
else:
    for b in buildings:
        s = score(b)

        st.write(
            f"🏢 Building {b['id']} | "
            f"H:{b['height']} W:{b['width']} | "
            f"S:{b['stability']} E:{b['efficiency']} | "
            f"Score: {round(s,2)}"
        )

# -----------------------------
# CITY STATUS
# -----------------------------
avg_score = sum(score(b) for b in buildings) / len(buildings) if buildings else 0

if avg_score > 8:
    st.success("🌆 Highly optimized architectural ecosystem")
elif avg_score < 5:
    st.warning("⚠ Structural instability spreading through the city")

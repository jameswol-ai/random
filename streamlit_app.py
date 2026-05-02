import streamlit as st
import random
import json

# =========================================================
# 🏗️ RANDOM — PARAMETRIC ARCHITECTURE AI
# =========================================================

st.set_page_config(page_title="Random Parametric Architecture AI", layout="wide")

st.title("🏗️ Random AI — Parametric Architecture Generator")
st.caption("User-driven + AI-driven structural design with realistic floorplans")

# =========================================================
# SIDEBAR — USER PARAMETERS
# =========================================================

st.sidebar.header("⚙️ Building Parameters")

user_span = st.sidebar.slider("Building Width (span)", 4, 30, 10)
user_depth = st.sidebar.slider("Building Depth", 4, 30, 10)
user_floors = st.sidebar.slider("Floors", 1, 10, 3)
user_load = st.sidebar.slider("Live Load Intensity", 1, 10, 5)

material = st.sidebar.selectbox("Material", ["RC", "Steel"])
style = st.sidebar.selectbox("Design Style", ["efficiency", "brutalist", "organic"])

grid_density = st.sidebar.slider("Structural Grid Density", 2, 8, 4)

# =========================================================
# STATE
# =========================================================

if "buildings" not in st.session_state:
    st.session_state.buildings = []
    st.session_state.tick = 0
    st.session_state.next_id = 1

# =========================================================
# ARCHITECT AGENTS
# =========================================================

def apply_style(style, b):
    if style == "efficiency":
        return {
            "span": max(4, b["span"] - 1),
            "depth": max(4, b["depth"] - 1),
            "load": max(1, b["load"] - 1),
        }

    if style == "brutalist":
        return {
            "span": b["span"] + 2,
            "depth": b["depth"] + 1,
            "load": b["load"] + 2,
        }

    if style == "organic":
        return {
            "span": b["span"] + random.randint(-2, 2),
            "depth": b["depth"] + random.randint(-2, 2),
            "load": b["load"] + random.randint(-1, 2),
        }

# =========================================================
# STRUCTURAL ENGINE (SIMPLIFIED)
# =========================================================

def stability(span, depth, load):
    ratio = (span + depth) / 2
    if load > ratio:
        return 3
    elif load > ratio * 0.7:
        return 6
    return 9

def efficiency(span, depth):
    return 10 - abs(span - depth)

def score(b):
    return (
        stability(b["span"], b["depth"], b["load"]) * 0.5 +
        efficiency(b["span"], b["depth"]) * 0.5
    )

# =========================================================
# FLOORPLAN GENERATOR (REALISTIC GRID)
# =========================================================

def generate_floorplan(span, depth, floors, grid):
    plan = []

    for y in range(depth):
        row = ""
        for x in range(span):

            # boundary walls
            if x == 0 or y == 0 or x == span - 1 or y == depth - 1:
                row += "█"

            # structural grid columns
            elif x % grid == 0 and y % grid == 0:
                row += "●"

            # core (stairs/elevator zone)
            elif span//2 - 1 <= x <= span//2 + 1 and depth//2 - 1 <= y <= depth//2 + 1:
                row += "■"

            # beams / structure
            elif x % grid == 0 or y % grid == 0:
                row += "╬"

            else:
                row += " "

        plan.append(row)

    return "\n".join(plan)

# =========================================================
# DESIGN GENERATION
# =========================================================

def generate_building():
    base = {
        "id": st.session_state.next_id,
        "span": user_span,
        "depth": user_depth,
        "floors": user_floors,
        "load": user_load,
        "material": material,
        "style": style
    }

    modified = apply_style(style, base)
    base.update(modified)

    st.session_state.next_id += 1
    return base

# =========================================================
# EVOLUTION ENGINE
# =========================================================

def evolve():
    new_set = []

    for b in st.session_state.buildings:
        s = score(b)

        if s > 6:
            new_set.append(b)

            if s > 8:
                child = b.copy()
                child["id"] = st.session_state.next_id
                child["span"] += random.randint(-1, 2)
                child["depth"] += random.randint(-1, 2)
                child["load"] += random.randint(-1, 1)
                st.session_state.next_id += 1
                new_set.append(child)
        else:
            new_set.append(generate_building())

    st.session_state.buildings = new_set
    st.session_state.tick += 1

# =========================================================
# UI CONTROLS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏗️ Generate Building"):
        st.session_state.buildings.append(generate_building())

with col2:
    if st.button("▶ Evolve City"):
        evolve()

with col3:
    if st.button("🧱 Reset City"):
        st.session_state.buildings = []
        st.session_state.tick = 0
        st.session_state.next_id = 1

# =========================================================
# DISPLAY
# =========================================================

st.subheader(f"🏙️ City Tick {st.session_state.tick}")

for b in st.session_state.buildings:
    s = score(b)

    status = "🟢 OK"
    if s < 5:
        status = "🔴 FAIL"
    elif s < 7:
        status = "🟡 MARGINAL"

    st.markdown(f"### 🏗️ Building {b['id']} — {status}")
    st.write(
        f"Span {b['span']} | Depth {b['depth']} | Floors {b['floors']} | "
        f"Load {b['load']} | Score {round(s,2)}"
    )

    with st.expander("📐 Floorplan"):
        st.text(generate_floorplan(
            b["span"],
            b["depth"],
            b["floors"],
            grid_density
        ))

# =========================================================
# BIM EXPORT
# =========================================================

st.download_button(
    "📦 Export BIM JSON",
    json.dumps(st.session_state.buildings, indent=2),
    file_name="parametric_buildings.json",
    mime="application/json"
)

# =========================================================
# SYSTEM STATUS
# =========================================================

if st.session_state.buildings:
    avg = sum(score(b) for b in st.session_state.buildings) / len(st.session_state.buildings)

    if avg > 7.5:
        st.success("🏛️ Stable parametric architectural system")
    elif avg < 5:
        st.warning("⚠ Structural instability across generated designs")
    else:
        st.info("🧠 Design system balancing between efficiency and chaos")

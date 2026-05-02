import streamlit as st
import random
import json
import math

# =========================================================
# 🏗️ RANDOM ARCHITECTURE ECOSYSTEM AI
# =========================================================

st.set_page_config(page_title="Random Architecture Ecosystem", layout="wide")

st.title("🏗️ Random AI — Architecture Ecosystem Engine")
st.caption("Competing architects, structural heuristics, evolving cities, BIM export")

# =========================================================
# ARCHITECT TYPES (MULTI-AGENT SYSTEM)
# =========================================================

ARCHITECTS = [
    "efficiency",
    "brutalist",
    "organic"
]

def architect_modifier(style, b):
    if style == "efficiency":
        return {
            "span": max(2, b["span"] - 1),
            "height": b["height"],
            "live_load": max(1, b["live_load"] - 1),
        }

    if style == "brutalist":
        return {
            "span": b["span"] + 1,
            "height": b["height"] + 1,
            "live_load": b["live_load"] + 2,
        }

    if style == "organic":
        return {
            "span": b["span"] + random.randint(-2, 3),
            "height": b["height"] + random.randint(-1, 2),
            "live_load": b["live_load"] + random.randint(-2, 2),
        }

# =========================================================
# STATE
# =========================================================

if "city" not in st.session_state:
    st.session_state.city = [
        {"id": 1, "span": 6, "height": 3, "floors": 2, "material": "RC", "live_load": 4},
        {"id": 2, "span": 8, "height": 4, "floors": 3, "material": "Steel", "live_load": 5},
    ]
    st.session_state.next_id = 3
    st.session_state.tick = 0

# =========================================================
# STRUCTURAL ENGINE (SIMPLIFIED EUROCODE LOGIC)
# =========================================================

def dead_load(b):
    return 5 if b["material"] == "RC" else 3

def wind_load(b):
    return b["span"] * 0.25

def total_load(b):
    return b["live_load"] + dead_load(b) + wind_load(b)

def slenderness(b):
    return b["height"] / max(b["span"], 0.1)

def stability(b):
    r = slenderness(b)
    if r > 0.9:
        return 2
    elif r > 0.6:
        return 5
    return 9

def span_efficiency(b):
    return 4 if b["span"] > b["height"] * 3 else 8

def load_score(b):
    tl = total_load(b)
    if tl > 15:
        return 3
    elif tl > 10:
        return 6
    return 9

def compliance(b):
    return (
        stability(b) * 0.4 +
        span_efficiency(b) * 0.3 +
        load_score(b) * 0.3
    )

def risk_index(b):
    return total_load(b) * (1 / max(slenderness(b), 0.1))

# =========================================================
# FLOOR PLAN GENERATOR
# =========================================================

def floorplan(b):
    size = min(12, max(4, b["span"]))
    grid = []

    for y in range(size):
        row = ""
        for x in range(size):
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                row += "█"
            elif (x + y) % 4 == 0:
                row += "╬"
            else:
                row += " "
        grid.append(row)

    return "\n".join(grid)

# =========================================================
# MUTATION (EVOLUTION)
# =========================================================

def mutate(b):
    return {
        "id": st.session_state.next_id,
        "span": max(2, b["span"] + random.randint(-2, 3)),
        "height": max(2, b["height"] + random.randint(-1, 2)),
        "floors": max(1, b["floors"] + random.randint(-1, 2)),
        "material": random.choice(["RC", "Steel"]),
        "live_load": max(1, b["live_load"] + random.randint(-2, 3)),
    }

# =========================================================
# MULTI-ARCHITECT DESIGN GENERATION
# =========================================================

def generate_design(b):
    style = random.choice(ARCHITECTS)

    mod = architect_modifier(style, b)

    new_b = {
        "id": st.session_state.next_id,
        "span": max(2, mod.get("span", b["span"])),
        "height": max(2, mod.get("height", b["height"])),
        "floors": b["floors"],
        "material": b["material"],
        "live_load": max(1, mod.get("live_load", b["live_load"])),
        "style": style
    }

    return new_b

# =========================================================
# EVOLUTION ENGINE
# =========================================================

def evolve():
    new_city = []

    for b in st.session_state.city:
        score = compliance(b)

        if score > 6:
            new_city.append(b)

            # reproduction
            if score > 7.5:
                child = generate_design(b)
                child["id"] = st.session_state.next_id
                st.session_state.next_id += 1
                new_city.append(child)

        else:
            # redesign weak structures
            child = generate_design(b)
            child["id"] = st.session_state.next_id
            st.session_state.next_id += 1
            new_city.append(child)

    st.session_state.city = new_city
    st.session_state.tick += 1

# =========================================================
# BIM EXPORT
# =========================================================

def export_bim():
    return json.dumps(st.session_state.city, indent=2)

# =========================================================
# UI
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("▶ Evolve City"):
        evolve()

with col2:
    if st.button("⚡ Fast Forward x10"):
        for _ in range(10):
            evolve()

with col3:
    if st.button("🧱 Reset City"):
        st.session_state.city = [
            {"id": 1, "span": 6, "height": 3, "floors": 2, "material": "RC", "live_load": 4},
            {"id": 2, "span": 8, "height": 4, "floors": 3, "material": "Steel", "live_load": 5},
        ]
        st.session_state.next_id = 3
        st.session_state.tick = 0

with col4:
    st.download_button(
        "📦 Export BIM JSON",
        export_bim(),
        file_name="random_city_bim.json",
        mime="application/json"
    )

# =========================================================
# DISPLAY CITY
# =========================================================

st.subheader(f"🏙️ City Tick {st.session_state.tick}")

city = st.session_state.city

if not city:
    st.error("🏚️ City collapsed")
else:
    for b in city:
        c = compliance(b)
        r = risk_index(b)

        status = "🟢 SAFE"
        if c < 5:
            status = "🔴 FAIL"
        elif c < 7:
            status = "🟡 MARGINAL"

        st.markdown(f"### 🏗️ Building {b['id']} ({b.get('style','base')}) — {status}")
        st.write(
            f"Span {b['span']}m | Height {b['height']}m | Floors {b['floors']} | "
            f"Load {b['live_load']} | Compliance {round(c,2)} | Risk {round(r,2)}"
        )

        with st.expander("📐 Floor Plan"):
            st.text(floorplan(b))

# =========================================================
# SYSTEM STATE
# =========================================================

avg = sum(compliance(b) for b in city) / len(city)

if avg > 7.5:
    st.success("🏛️ Stable architectural ecosystem emerging")
elif avg < 5:
    st.warning("⚠ Structural instability propagating")
else:
    st.info("🧠 Transitional design phase — competing architectural intelligence active")

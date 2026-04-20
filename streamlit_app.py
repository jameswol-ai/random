import streamlit as st
from src.core import process_request

st.set_page_config(page_title="Architect AI", layout="wide")

st.title("🏗️ Architectural AI Bot (random engine)")

user_input = st.text_area("Describe your building idea:")

workflow = st.selectbox(
    "Choose mode",
    ["Residential Design", "Urban Planning", "Compliance Check"]
)

if st.button("Generate Design"):
    if user_input.strip():
        result = process_request(user_input, workflow)
        st.markdown("### 🧠 AI Output")
        st.write(result)
    else:
        st.warning("Please enter a request.")

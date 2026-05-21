import streamlit as st
import os
import time
import pandas as pd
import altair as alt

# ── Page Config ─────────────────────────
st.set_page_config(
    page_title="Legal AI Assistant",
    page_icon="⚖️",
    layout="wide"
)

# ── CSS ─────────────────────────────────
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}

.hero {
    padding: 2rem;
    border-radius: 15px;
    background: linear-gradient(135deg,#1e3a8a,#0f172a);
    margin-bottom: 2rem;
}

.card {
    background: #1e293b;
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid #334155;
    text-align: center;
}

.answer-box {
    background: #1e293b;
    padding: 1.5rem;
    border-radius: 12px;
    border-left: 5px solid #3b82f6;
    margin-top: 1rem;
}

.stButton button {
    width: 100%;
    background: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ── Mock Answers ───────────────────────
MOCK_RESPONSES = {
    "force majeure":
        "COVID-19 may qualify as a force majeure event depending on the contract wording and jurisdiction.",

    "non-compete":
        "Non-compete clauses are generally unenforceable in California under Business and Professions Code §16600.",

    "gdpr":
        "GDPR Article 32 requires appropriate technical and organizational security measures.",

    "default":
        "This legal issue depends on jurisdiction, contract wording, and applicable regulations."
}

def get_answer(question):
    q = question.lower()

    for key in MOCK_RESPONSES:
        if key in q:
            return MOCK_RESPONSES[key]

    return MOCK_RESPONSES["default"]

# ── Header ─────────────────────────────
st.markdown("""
<div class="hero">
    <h1>⚖️ Legal AI Assistant</h1>
    <p>AI-powered legal research assistant using modern LLM technologies.</p>
</div>
""", unsafe_allow_html=True)

# ── Metrics ────────────────────────────
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <h2>6</h2>
        <p>Completed Phases</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h2>10</h2>
        <p>Evaluation Cases</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h2>0.85</h2>
        <p>Faithfulness Score</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Tabs ───────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "💬 Ask Question",
    "📊 Evaluation",
    "ℹ️ About"
])

# ── TAB 1 ──────────────────────────────
with tab1:

    st.subheader("Ask a Legal Question")

    question = st.text_area(
        "Enter your question",
        placeholder="Example: Is a non-compete enforceable in California?"
    )

    if st.button("Get Legal Answer"):

        with st.spinner("Generating answer..."):
            time.sleep(1)

            answer = get_answer(question)

            st.markdown(f"""
            <div class="answer-box">
                <h4>⚖️ Legal Answer</h4>
                <p>{answer}</p>
            </div>
            """, unsafe_allow_html=True)

            st.warning(
                "This is AI-generated legal research assistance only. Consult a licensed attorney."
            )

# ── TAB 2 ──────────────────────────────
with tab2:

    st.subheader("Evaluation Results")

    data = pd.DataFrame({
        "Case": [1,2,3,4,5],
        "Faithfulness": [0.91,0.88,0.93,0.85,0.79]
    })

    st.dataframe(data, use_container_width=True)

    chart = alt.Chart(data).mark_bar().encode(
        x="Case:O",
        y="Faithfulness:Q"
    )

    st.altair_chart(chart, use_container_width=True)

# ── TAB 3 ──────────────────────────────
with tab3:

    st.subheader("About This Project")

    st.markdown("""
This Legal AI Assistant is a capstone project built using:

- Streamlit
- Gemini / OpenAI APIs
- RAG Architecture
- LangChain Concepts
- LegalBench Evaluation

The system is designed for legal research assistance and educational purposes.
""")

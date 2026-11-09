"""Streamlit UI. Never embeds API credentials in source control."""
from __future__ import annotations
import hashlib
import io
import os
import pandas as pd
import plotly.express as px
import streamlit as st
from google import genai
from analyst_engine import answer_question, autonomous_analysis, columns_profile

st.set_page_config(page_title="Autonomous AI Data Analyst", page_icon="📊", layout="wide")
st.title("📊 Autonomous AI Data Analyst")
st.caption("Gemini + LangGraph + Pandas + Plotly — tabular data analysis prototype")


def api_key() -> str | None:
    try:
        return st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    except (FileNotFoundError, KeyError):
        return os.environ.get("GEMINI_API_KEY")


def load_file(upload) -> pd.DataFrame:
    raw = upload.getvalue()
    if len(raw) > 15 * 1024 * 1024:
        raise ValueError("Maximum file size is 15 MB")
    if upload.name.lower().endswith(".csv"):
        try:
            df = pd.read_csv(io.BytesIO(raw))
        except UnicodeDecodeError:
            df = pd.read_csv(io.BytesIO(raw), encoding="latin-1")
    elif upload.name.lower().endswith(".xlsx"):
        df = pd.read_excel(io.BytesIO(raw))
    else:
        raise ValueError("Upload CSV or XLSX")
    if df.empty or df.columns.duplicated().any() or len(df.columns) > 150:
        raise ValueError("Empty datasets, duplicate headers and over 150 columns are unsupported")
    return df


def show_visual(df: pd.DataFrame, results: list[dict]) -> None:
    for item in results:
        if "result" not in item:
            continue
        result = item["result"]
        if item["tool"] == "grouped_analysis":
            cat, num, op = result["category_col"], result["numeric_col"], result["operation"]
            if cat in df and num in df:
                grouped = df.groupby(cat, dropna=False)[num].agg(op).sort_values(ascending=False).head(20).reset_index()
                st.plotly_chart(px.bar(grouped, x=cat, y=num, title=f"{op.title()} of {num} by {cat}"), use_container_width=True)
                return
        if item["tool"] == "time_series":
            st.line_chart(pd.Series(result["values"], name=result["numeric_col"]))
            return

key = api_key()
if not key:
    st.warning("Gemini API key missing. Set GEMINI_API_KEY in host Secrets or an environment variable.")
upload = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])
if upload is None:
    st.info("Upload CSV or XLSX to get started. Do not upload sensitive information without permission.")
    st.stop()
try:
    df = load_file(upload)
except Exception as exc:
    st.error(f"Unable to read file: {exc}")
    st.stop()
hash_value = hashlib.sha256(upload.getvalue()).hexdigest()
if st.session_state.get("file_hash") != hash_value:
    st.session_state["file_hash"] = hash_value
    st.session_state["report"] = None
    st.session_state["messages"] = []
profile = columns_profile(df)
a,b,c = st.columns(3)
a.metric("Rows", f"{len(df):,}")
b.metric("Columns", len(df.columns))
c.metric("Missing cells", profile["missing_cells"])
with st.expander("Dataset preview", expanded=True):
    st.dataframe(df.head(20), use_container_width=True)
    st.json(profile, expanded=False)
mode = st.radio("Analysis mode", ["Autonomous Analysis", "Ask Your Data"], horizontal=True)
if mode == "Autonomous Analysis":
    if st.button("Run autonomous analysis", disabled=not bool(key), type="primary"):
        try:
            with st.spinner("Running AI-guided analysis..."):
                st.session_state["report"] = autonomous_analysis(df, genai.Client(api_key=key))
        except Exception as exc:
            st.error(f"Analysis error: {exc}")
    result = st.session_state.get("report")
    if result:
        show_visual(df, result["results"])
        with st.expander("Calculated evidence"):
            st.json(result["results"])
        st.markdown(result["report"])
        st.download_button("Download report", result["report"], file_name="analysis_report.md")
else:
    st.subheader("Ask a question about your data")
    for item in st.session_state["messages"]:
        with st.chat_message(item["role"]):
            st.markdown(item["content"])
    question = st.chat_input("Example: Which category has the highest average profit?", disabled=not bool(key))
    if question:
        st.session_state["messages"].append({"role": "user", "content": question})
        try:
            with st.spinner("Planning and calculating..."):
                output = answer_question(df, genai.Client(api_key=key), question)
            st.session_state["messages"].append({"role": "assistant", "content": output["answer"]})
            with st.chat_message("assistant"):
                st.markdown(output["answer"])
                with st.expander("Calculation evidence"):
                    st.json(output["results"])
                show_visual(df, output["results"])
        except Exception as exc:
            st.error(f"Question failed: {exc}")
st.caption("Prototype. Model explanations may be wrong; independently verify important calculations.")

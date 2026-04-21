import streamlit as st
import pandas as pd
from analyzer_llm import analyze_with_llm

st.set_page_config(page_title="Defect Summarizer", layout="centered")

st.title("🛠 Defect Report Summarizer")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data")
    st.dataframe(df)

    # ✅ STEP 1: Pandas summary
    summary = {
        "total_defects": len(df),
        "defect_summary": df["Defect_Type"].value_counts().to_dict(),
        "severity_summary": df["Severity"].value_counts().to_dict()
    }

    # ✅ CLEAN TEXT DISPLAY (instead of JSON)
    st.subheader("📊 Summary")

    st.write(f"**Total Defects:** {summary['total_defects']}")

    st.write("**Defect Breakdown:**")
    for defect, count in summary["defect_summary"].items():
        st.write(f"- {defect}: {count}")

    st.write("**Severity Breakdown:**")
    for sev, count in summary["severity_summary"].items():
        st.write(f"- {sev}: {count}")

    # ✅ STEP 2: LLM Insights
    if st.button("Generate Insights"):
        result = analyze_with_llm(summary)

        st.subheader("🤖 AI Insights")
        st.write(result)
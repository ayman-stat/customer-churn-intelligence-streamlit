import streamlit as st


st.set_page_config(page_title="AI Leadership & Governance", layout="wide")
st.title("AI Leadership & Governance")
st.caption("How this churn model would be governed, measured, and operationalized beyond a notebook demo.")

left, right = st.columns([1, 1])

with left:
    st.subheader("Decision Architecture")
    st.markdown(
        """
- Define the business objective: retained revenue, churn reduction, or campaign ROI.
- Score eligible customers, not the full population blindly.
- Combine churn risk with value, offer cost, contact policy, and intervention capacity.
- Use model output as decision support, not uncontrolled automation.
- Track outcomes through target/control design before claiming uplift.
"""
    )

    st.subheader("Executive Questions")
    st.markdown(
        """
- Which segment is most exposed?
- What is the revenue at risk?
- How many customers can the team realistically contact?
- Which threshold creates the best tradeoff between value and cost?
- How will we know the model improved retention rather than just selected obvious cases?
"""
    )

with right:
    st.subheader("Governance Controls")
    st.markdown(
        """
- Approved feature definitions and data lineage.
- Privacy review before using real customer data.
- Human review for high-value or sensitive interventions.
- Drift monitoring across features, scores, and outcomes.
- Model card and retraining cadence before production rollout.
"""
    )

    st.subheader("MLOps Roadmap")
    st.markdown(
        """
- Add MLflow experiment tracking and model registry.
- Add scheduled scoring and batch output tables.
- Add monitoring dashboard for drift and campaign uplift.
- Add CI checks for data generation, model training, and app startup.
- Add stakeholder-facing KPI dashboard connected to campaign outcomes.
"""
    )

st.divider()

st.subheader("AI Lead Interpretation")
st.info(
    "The senior value of this project is not the classifier alone. It is the full decision system: "
    "business framing, risk scoring, prioritization, financial assumptions, experimentation, governance, "
    "and deployment readiness."
)

import streamlit as st


st.set_page_config(page_title="Model Governance & Rollout", layout="wide")
st.title("Model Governance & Rollout")
st.caption("A practical checklist for moving churn scores from demo output into campaign operations.")

left, right = st.columns([1, 1])

with left:
    st.subheader("Operating Model")
    st.markdown(
        """
- Define the business objective: retained revenue, churn reduction, or campaign ROI.
- Score eligible customers rather than the full population by default.
- Combine churn risk with value, offer cost, contact policy, and intervention capacity.
- Use model output as decision support, with business rules around activation.
- Track outcomes through target/control design before claiming uplift.
"""
    )

    st.subheader("Questions Before Launch")
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
    st.subheader("Controls Before Activation")
    st.markdown(
        """
- Approved feature definitions and data lineage.
- Privacy review before using real customer data.
- Human review for high-value or sensitive interventions.
- Drift monitoring across features, scores, and outcomes.
- Model card and retraining cadence before production rollout.
"""
    )

    st.subheader("Rollout Roadmap")
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

st.subheader("Delivery Readiness")
st.info(
    "At production level, the model is only one part of the work. The important part is connecting "
    "risk scores to campaign capacity, financial assumptions, measurement design, and monitored rollout."
)

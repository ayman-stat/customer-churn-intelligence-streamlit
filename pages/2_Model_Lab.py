import streamlit as st
import plotly.express as px

from src.data import generate_customer_churn_data
from src.features import build_feature_matrix
from src.modeling import train_candidate_models


st.set_page_config(page_title="Model Lab", layout="wide")
st.title("Model Lab")
st.caption("Train candidate churn models and compare them with business-oriented metrics.")

sample_size = st.sidebar.slider("Customer sample size", 500, 10000, 2500, step=500)
random_seed = st.sidebar.number_input("Random seed", value=42, step=1)

df = generate_customer_churn_data(n_customers=sample_size, random_seed=random_seed)
X, y, feature_names = build_feature_matrix(df)
result = train_candidate_models(X, y, feature_names)

st.subheader("Model Leaderboard")
st.dataframe(result.leaderboard, hide_index=True, use_container_width=True)

st.subheader("Feature Importance")
importance = result.feature_importance.sort_values("importance", ascending=False).head(15)
fig = px.bar(
    importance,
    y="feature",
    x="importance",
    orientation="h",
    labels={"importance": "Importance", "feature": "Feature"},
)
fig.update_layout(height=520, yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig, use_container_width=True)

st.subheader("Business Interpretation")
st.markdown(
    """
The goal is not only to maximize AUC. A useful churn model should help teams:

- Prioritize customers with high predicted churn probability and meaningful revenue exposure.
- Understand which behavioral signals are moving risk.
- Create measurable target/control retention tests.
- Track uplift after campaigns.
"""
)

st.subheader("Senior DS / AI Lead Review Checklist")
st.markdown(
    """
- **Problem framing:** define whether the objective is churn reduction, retained revenue, or campaign ROI.
- **Threshold strategy:** select thresholds by intervention capacity and expected marginal value, not only model accuracy.
- **Experiment design:** reserve a control group so uplift is measured rather than assumed.
- **Monitoring:** track drift, score stability, campaign fatigue, false positives, and retention outcome windows.
- **Governance:** document data lineage, feature definitions, privacy constraints, retraining cadence, and human override paths.
"""
)

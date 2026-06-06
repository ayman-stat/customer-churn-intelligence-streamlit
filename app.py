import streamlit as st
import plotly.express as px

from src.data import generate_customer_churn_data
from src.features import build_feature_matrix
from src.modeling import train_candidate_models
from src.utils import format_pct


st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon=":bar_chart:",
    layout="wide",
)


@st.cache_data(show_spinner=False)
def load_data(sample_size: int, random_seed: int):
    return generate_customer_churn_data(n_customers=sample_size, random_seed=random_seed)


@st.cache_resource(show_spinner=False)
def train_models(sample_size: int, random_seed: int):
    df = load_data(sample_size, random_seed)
    X, y, feature_names = build_feature_matrix(df)
    return train_candidate_models(X, y, feature_names)


def main():
    st.title("Customer Churn Intelligence")
    st.caption(
        "A senior-level ML product demo for churn prediction, retention prioritization, and executive decision support."
    )

    with st.sidebar:
        st.header("Controls")
        sample_size = st.slider("Customer sample size", 500, 5000, 1500, step=500)
        random_seed = st.number_input("Random seed", value=42, step=1)
        risk_threshold = st.slider("High-risk threshold", 0.30, 0.90, 0.60, step=0.05)
        st.header("Decision Assumptions")
        intervention_capacity = st.slider("Targetable member share", 0.05, 0.40, 0.15, step=0.05)
        expected_save_rate = st.slider("Assumed save rate", 0.02, 0.25, 0.18, step=0.01)
        monthly_offer_cost = st.slider("Offer cost per target", 5, 100, 15, step=5)

    # Load data and models inside the UI lifecycle so exceptions can be caught
    df = load_data(sample_size, random_seed)
    model_result = train_models(sample_size, random_seed)
    scored = model_result.scored_data.copy()
    scored["risk_band"] = scored["churn_probability"].apply(
        lambda p: "High Risk" if p >= risk_threshold else ("Medium Risk" if p >= 0.35 else "Low Risk")
    )

    total_customers = len(scored)
    churn_rate = scored["churned"].mean()
    high_risk_share = (scored["risk_band"] == "High Risk").mean()
    expected_at_risk_revenue = scored.loc[scored["risk_band"] == "High Risk", "monthly_revenue"].sum()
    target_count = max(1, int(total_customers * intervention_capacity))
    target_segment = scored.sort_values("churn_probability", ascending=False).head(target_count)
    target_revenue = target_segment["monthly_revenue"].sum()
    estimated_retained_revenue = target_revenue * expected_save_rate
    estimated_offer_cost = target_count * monthly_offer_cost
    estimated_net_value = estimated_retained_revenue - estimated_offer_cost

    kpi_cols = st.columns(4)
    kpi_cols[0].metric("Customers", f"{total_customers:,}")
    kpi_cols[1].metric("Observed Churn Rate", format_pct(churn_rate))
    kpi_cols[2].metric("High-Risk Share", format_pct(high_risk_share))
    kpi_cols[3].metric("High-Risk Monthly Revenue", f"${expected_at_risk_revenue:,.0f}")

    st.divider()
    st.subheader("Executive Decision Layer")
    decision_cols = st.columns(4)
    decision_cols[0].metric("Recommended Target Segment", f"{target_count:,}")
    decision_cols[1].metric("Target Revenue Exposure", f"${target_revenue:,.0f}")
    decision_cols[2].metric("Estimated Retained Revenue", f"${estimated_retained_revenue:,.0f}")
    decision_cols[3].metric("Net Value Scenario", f"${estimated_net_value:,.0f}")

    st.markdown(
        """
This layer converts model scores into an operating decision: who to target, how much revenue is exposed,
what intervention cost is assumed, and how the campaign should be evaluated through target/control measurement.
All values are synthetic and scenario-based for portfolio demonstration.
"""
    )

    st.divider()

    left, right = st.columns([1.15, 0.85])

    with left:
        st.subheader("Churn Risk by Segment")
        segment_summary = (
            scored.groupby("customer_segment", as_index=False)
            .agg(
                customers=("customer_id", "count"),
                churn_rate=("churned", "mean"),
                avg_probability=("churn_probability", "mean"),
                monthly_revenue=("monthly_revenue", "sum"),
            )
            .sort_values("avg_probability", ascending=False)
        )
        fig = px.bar(
            segment_summary,
            x="customer_segment",
            y="avg_probability",
            color="monthly_revenue",
            text=segment_summary["avg_probability"].map(format_pct),
            labels={
                "customer_segment": "Customer Segment",
                "avg_probability": "Average Predicted Churn Risk",
                "monthly_revenue": "Monthly Revenue",
            },
        )
        fig.update_layout(height=430, coloraxis_colorbar_title="Revenue")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Model Leaderboard")
        leaderboard = model_result.leaderboard.copy()
        leaderboard["roc_auc"] = leaderboard["roc_auc"].round(3)
        leaderboard["average_precision"] = leaderboard["average_precision"].round(3)
        leaderboard["recall_at_threshold"] = leaderboard["recall_at_threshold"].round(3)
        st.dataframe(leaderboard, hide_index=True, use_container_width=True)

        st.subheader("Recommended Retention Plays")
        st.markdown(
            """
- **High engagement drop:** trigger proactive outreach and personalized reactivation offer.
- **High value and high risk:** route to premium retention queue.
- **Low visits but long tenure:** propose habit-building plan and next-best activity.
- **Price sensitivity:** test lower-cost renewal bundle or targeted discount.
"""
        )

        st.subheader("Production & Governance Notes")
        st.markdown(
            """
- Keep model training data separate from campaign execution data.
- Use target/control groups before claiming business uplift.
- Monitor drift in visit frequency, support tickets, tenure, and offer response.
- Review fairness and policy constraints before automated offers.
- Publish a model card before operational rollout.
"""
        )

    st.divider()
    st.subheader("High-Risk Customer Watchlist")
    watchlist = (
        scored.sort_values("churn_probability", ascending=False)
        .loc[
            :,
            [
                "customer_id",
                "customer_segment",
                "tenure_months",
                "monthly_revenue",
                "visits_last_30d",
                "support_tickets_90d",
                "churn_probability",
                "risk_band",
            ],
        ]
        .head(25)
    )
    watchlist["churn_probability"] = watchlist["churn_probability"].map(format_pct)
    st.dataframe(watchlist, hide_index=True, use_container_width=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # capture unexpected startup errors for debugging on Streamlit Cloud
        import traceback

        tb = traceback.format_exc()
        try:
            st.error("The app failed to start — captured the exception below.")
            st.text(tb)
        except Exception:
            # If Streamlit itself is unstable, still write an error file to help remote debugging
            with open("streamlit_startup_error.log", "w") as fh:
                fh.write(tb)


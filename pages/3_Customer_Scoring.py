import streamlit as st

from src.data import generate_customer_churn_data
from src.features import build_feature_matrix
from src.modeling import train_candidate_models
from src.utils import format_pct


st.set_page_config(page_title="Customer Scoring", layout="wide")
st.title("Customer Scoring")
st.caption("Score an individual customer profile and recommend a retention action.")

df = generate_customer_churn_data(n_customers=2500, random_seed=42)
X, y, feature_names = build_feature_matrix(df)
result = train_candidate_models(X, y, feature_names)

st.sidebar.header("Customer Profile")
tenure_months = st.sidebar.slider("Tenure months", 1, 72, 18)
monthly_revenue = st.sidebar.slider("Monthly revenue", 10, 500, 95)
visits_last_30d = st.sidebar.slider("Visits last 30 days", 0, 30, 5)
days_since_last_visit = st.sidebar.slider("Days since last visit", 0, 90, 14)
support_tickets_90d = st.sidebar.slider("Support tickets last 90 days", 0, 12, 1)
discount_usage_rate = st.sidebar.slider("Discount usage rate", 0.0, 1.0, 0.25)
late_payment_count = st.sidebar.slider("Late payment count", 0, 8, 0)
customer_segment = st.sidebar.selectbox("Customer segment", sorted(df["customer_segment"].unique()))
channel = st.sidebar.selectbox("Acquisition channel", sorted(df["acquisition_channel"].unique()))

profile = df.iloc[[0]].copy()
profile.loc[:, "tenure_months"] = tenure_months
profile.loc[:, "monthly_revenue"] = monthly_revenue
profile.loc[:, "visits_last_30d"] = visits_last_30d
profile.loc[:, "days_since_last_visit"] = days_since_last_visit
profile.loc[:, "support_tickets_90d"] = support_tickets_90d
profile.loc[:, "discount_usage_rate"] = discount_usage_rate
profile.loc[:, "late_payment_count"] = late_payment_count
profile.loc[:, "customer_segment"] = customer_segment
profile.loc[:, "acquisition_channel"] = channel

X_profile, _, _ = build_feature_matrix(profile, fit_target=False)
probability = result.best_pipeline.predict_proba(X_profile)[0, 1]

left, right = st.columns([0.8, 1.2])
with left:
    st.metric("Predicted Churn Risk", format_pct(probability))
    if probability >= 0.65:
        st.error("High risk")
    elif probability >= 0.35:
        st.warning("Medium risk")
    else:
        st.success("Low risk")

with right:
    st.subheader("Recommended Action")
    if probability >= 0.65 and monthly_revenue >= 100:
        st.write("Route to high-value retention queue with a personalized offer and direct outreach.")
    elif probability >= 0.65:
        st.write("Trigger reactivation campaign with behavior-based messaging and a limited renewal incentive.")
    elif visits_last_30d <= 3:
        st.write("Send habit-building journey and next-best activity recommendation.")
    else:
        st.write("Maintain engagement with light-touch personalized content.")

st.subheader("Profile Sent to Model")
st.dataframe(profile, hide_index=True, use_container_width=True)


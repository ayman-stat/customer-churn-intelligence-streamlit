import streamlit as st
import plotly.express as px

from src.data import generate_customer_churn_data


st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("Data Explorer")
st.caption("Explore synthetic customer, behavior, commercial, and service-interaction signals.")

sample_size = st.sidebar.slider("Customer sample size", 500, 10000, 2500, step=500)
random_seed = st.sidebar.number_input("Random seed", value=42, step=1)

df = generate_customer_churn_data(n_customers=sample_size, random_seed=random_seed)

st.subheader("Dataset Preview")
st.dataframe(df.head(50), use_container_width=True, hide_index=True)

left, right = st.columns(2)
with left:
    st.subheader("Monthly Revenue Distribution")
    st.plotly_chart(
        px.histogram(df, x="monthly_revenue", color="churned", nbins=35),
        use_container_width=True,
    )

with right:
    st.subheader("Visits vs Churn Risk Drivers")
    st.plotly_chart(
        px.scatter(
            df,
            x="visits_last_30d",
            y="monthly_revenue",
            color="churned",
            size="support_tickets_90d",
            hover_data=["customer_segment", "tenure_months"],
        ),
        use_container_width=True,
    )

st.subheader("Segment Profile")
segment_profile = (
    df.groupby("customer_segment", as_index=False)
    .agg(
        customers=("customer_id", "count"),
        churn_rate=("churned", "mean"),
        avg_tenure=("tenure_months", "mean"),
        avg_revenue=("monthly_revenue", "mean"),
        avg_visits=("visits_last_30d", "mean"),
        avg_tickets=("support_tickets_90d", "mean"),
    )
    .sort_values("churn_rate", ascending=False)
)
st.dataframe(segment_profile, hide_index=True, use_container_width=True)


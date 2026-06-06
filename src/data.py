import numpy as np
import pandas as pd


def generate_customer_churn_data(n_customers: int = 2500, random_seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(random_seed)

    segments = np.array(["Premium", "Core", "Budget", "Corporate", "New Joiner"])
    channels = np.array(["Organic", "Paid Search", "Referral", "Partnership", "Walk-in"])

    customer_segment = rng.choice(segments, size=n_customers, p=[0.18, 0.35, 0.22, 0.10, 0.15])
    acquisition_channel = rng.choice(channels, size=n_customers, p=[0.28, 0.25, 0.18, 0.12, 0.17])

    tenure_months = rng.integers(1, 73, size=n_customers)
    monthly_revenue = np.round(
        rng.gamma(shape=4.2, scale=24, size=n_customers)
        + np.where(customer_segment == "Premium", 80, 0)
        + np.where(customer_segment == "Corporate", 45, 0),
        2,
    )
    visits_last_30d = np.clip(
        rng.poisson(lam=7, size=n_customers)
        + np.where(customer_segment == "Premium", 4, 0)
        - np.where(customer_segment == "Budget", 2, 0),
        0,
        None,
    )
    days_since_last_visit = np.clip(rng.normal(18, 14, size=n_customers).astype(int), 0, 90)
    support_tickets_90d = rng.poisson(lam=1.2, size=n_customers)
    discount_usage_rate = np.clip(rng.beta(2.2, 5.0, size=n_customers), 0, 1)
    late_payment_count = rng.poisson(lam=0.4, size=n_customers)
    app_engagement_score = np.clip(rng.normal(62, 18, size=n_customers), 0, 100)
    nps_score = np.clip(rng.normal(45, 28, size=n_customers), -100, 100)

    logit = (
        -2.2
        - 0.055 * visits_last_30d
        + 0.035 * days_since_last_visit
        + 0.32 * support_tickets_90d
        + 0.55 * discount_usage_rate
        + 0.27 * late_payment_count
        - 0.012 * app_engagement_score
        - 0.006 * nps_score
        - 0.010 * tenure_months
        + np.where(customer_segment == "New Joiner", 0.45, 0)
        + np.where(customer_segment == "Budget", 0.35, 0)
        - np.where(customer_segment == "Premium", 0.25, 0)
    )
    churn_probability = 1 / (1 + np.exp(-logit))
    churned = rng.binomial(1, churn_probability)

    return pd.DataFrame(
        {
            "customer_id": [f"CUST-{i:06d}" for i in range(1, n_customers + 1)],
            "customer_segment": customer_segment,
            "acquisition_channel": acquisition_channel,
            "tenure_months": tenure_months,
            "monthly_revenue": monthly_revenue,
            "visits_last_30d": visits_last_30d,
            "days_since_last_visit": days_since_last_visit,
            "support_tickets_90d": support_tickets_90d,
            "discount_usage_rate": discount_usage_rate,
            "late_payment_count": late_payment_count,
            "app_engagement_score": np.round(app_engagement_score, 1),
            "nps_score": np.round(nps_score, 1),
            "churned": churned,
        }
    )


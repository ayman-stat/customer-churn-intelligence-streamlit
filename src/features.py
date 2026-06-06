import pandas as pd


FEATURE_COLUMNS = [
    "customer_segment",
    "acquisition_channel",
    "tenure_months",
    "monthly_revenue",
    "visits_last_30d",
    "days_since_last_visit",
    "support_tickets_90d",
    "discount_usage_rate",
    "late_payment_count",
    "app_engagement_score",
    "nps_score",
]


def build_feature_matrix(df: pd.DataFrame, fit_target: bool = True):
    X = df[FEATURE_COLUMNS].copy()
    y = df["churned"].copy() if fit_target and "churned" in df.columns else None
    return X, y, FEATURE_COLUMNS


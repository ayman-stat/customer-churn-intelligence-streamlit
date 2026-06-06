from src.data import generate_customer_churn_data
from src.features import build_feature_matrix
from src.modeling import train_candidate_models


def test_data_generation_has_expected_columns():
    df = generate_customer_churn_data(n_customers=100, random_seed=42)
    assert {"customer_id", "customer_segment", "monthly_revenue", "churned"}.issubset(df.columns)
    assert len(df) == 100


def test_model_training_smoke():
    df = generate_customer_churn_data(n_customers=300, random_seed=42)
    X, y, feature_names = build_feature_matrix(df)
    result = train_candidate_models(X, y, feature_names)
    assert result.best_model_name
    assert not result.leaderboard.empty
    assert "churn_probability" in result.scored_data.columns


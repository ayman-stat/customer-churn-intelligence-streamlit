from dataclasses import dataclass

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.data import generate_customer_churn_data
from src.features import build_feature_matrix


@dataclass
class ModelResult:
    best_model_name: str
    best_pipeline: Pipeline
    leaderboard: pd.DataFrame
    feature_importance: pd.DataFrame
    scored_data: pd.DataFrame


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    categorical = X.select_dtypes(include=["object", "category"]).columns.tolist()
    numeric = [c for c in X.columns if c not in categorical]

    return ColumnTransformer(
        transformers=[
            ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical),
            ("numeric", StandardScaler(), numeric),
        ]
    )


def train_candidate_models(X: pd.DataFrame, y: pd.Series, feature_names: list[str]) -> ModelResult:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=42
    )

    candidates = {
        "Logistic Regression": LogisticRegression(max_iter=1000, class_weight="balanced"),
        "Random Forest": RandomForestClassifier(
            n_estimators=120,
            max_depth=8,
            min_samples_leaf=12,
            class_weight="balanced",
            random_state=42,
        ),
        "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    }

    rows = []
    fitted = {}
    for name, estimator in candidates.items():
        pipeline = Pipeline(
            steps=[
                ("preprocessor", build_preprocessor(X_train)),
                ("model", estimator),
            ]
        )
        pipeline.fit(X_train, y_train)
        probabilities = pipeline.predict_proba(X_test)[:, 1]
        predictions = (probabilities >= 0.50).astype(int)

        rows.append(
            {
                "model": name,
                "roc_auc": roc_auc_score(y_test, probabilities),
                "average_precision": average_precision_score(y_test, probabilities),
                "recall_at_threshold": recall_score(y_test, predictions),
            }
        )
        fitted[name] = pipeline

    leaderboard = pd.DataFrame(rows).sort_values("roc_auc", ascending=False).reset_index(drop=True)
    best_model_name = leaderboard.loc[0, "model"]
    best_pipeline = fitted[best_model_name]

    scored_data = generate_customer_churn_data(n_customers=len(X), random_seed=42)
    scored_X, _, _ = build_feature_matrix(scored_data, fit_target=False)
    scored_data["churn_probability"] = best_pipeline.predict_proba(scored_X)[:, 1]

    importance = extract_feature_importance(best_pipeline)

    return ModelResult(
        best_model_name=best_model_name,
        best_pipeline=best_pipeline,
        leaderboard=leaderboard,
        feature_importance=importance,
        scored_data=scored_data,
    )


def extract_feature_importance(pipeline: Pipeline) -> pd.DataFrame:
    preprocessor = pipeline.named_steps["preprocessor"]
    model = pipeline.named_steps["model"]

    try:
        names = preprocessor.get_feature_names_out()
    except Exception:
        names = [f"feature_{i}" for i in range(len(getattr(model, "feature_importances_", [])))]

    if hasattr(model, "feature_importances_"):
        values = model.feature_importances_
    elif hasattr(model, "coef_"):
        values = abs(model.coef_[0])
    else:
        values = [0] * len(names)

    clean_names = [name.replace("categorical__", "").replace("numeric__", "") for name in names]
    return pd.DataFrame({"feature": clean_names, "importance": values})
